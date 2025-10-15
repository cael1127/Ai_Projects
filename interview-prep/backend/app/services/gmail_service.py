import base64
import re
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from app.config import settings
from app.models import InterviewType
import logging

logger = logging.getLogger(__name__)


class GmailService:
    """Service for interacting with Gmail API"""
    
    def __init__(self, credentials: Optional[Credentials] = None, mock_mode: bool = None):
        self.mock_mode = mock_mode if mock_mode is not None else settings.MOCK_MODE
        self.credentials = credentials
        self.service = None
        
        if not self.mock_mode and credentials:
            try:
                self.service = build('gmail', 'v1', credentials=credentials)
            except Exception as e:
                logger.error(f"Failed to build Gmail service: {e}")
                self.mock_mode = True
    
    def get_interview_emails(self, max_results: int = 50) -> List[Dict]:
        """Fetch emails that might contain interview invitations"""
        if self.mock_mode:
            return self._get_mock_interview_emails()
        
        try:
            # Search for emails with interview-related keywords
            query = 'subject:(interview OR "interview invitation" OR "interview scheduled") OR body:(interview OR "looking forward to speaking")'
            results = self.service.users().messages().list(
                userId='me',
                q=query,
                maxResults=max_results
            ).execute()
            
            messages = results.get('messages', [])
            email_data = []
            
            for message in messages:
                msg = self.service.users().messages().get(
                    userId='me',
                    id=message['id'],
                    format='full'
                ).execute()
                
                parsed_email = self._parse_email(msg)
                if parsed_email:
                    email_data.append(parsed_email)
            
            return email_data
        
        except HttpError as error:
            logger.error(f"An error occurred: {error}")
            return []
    
    def _parse_email(self, message: Dict) -> Optional[Dict]:
        """Parse an email message to extract interview details"""
        try:
            headers = message['payload']['headers']
            subject = next((h['value'] for h in headers if h['name'].lower() == 'subject'), '')
            sender = next((h['value'] for h in headers if h['name'].lower() == 'from'), '')
            date = next((h['value'] for h in headers if h['name'].lower() == 'date'), '')
            
            # Get email body
            body = self._get_email_body(message['payload'])
            
            # Extract interview details
            interview_type = self._detect_interview_type(subject, body)
            company = self._extract_company(sender, body)
            position = self._extract_position(subject, body)
            interview_date = self._extract_date(body)
            meeting_link = self._extract_meeting_link(body)
            
            return {
                'message_id': message['id'],
                'subject': subject,
                'sender': sender,
                'date': date,
                'body': body,
                'interview_type': interview_type,
                'company': company,
                'position': position,
                'interview_date': interview_date,
                'meeting_link': meeting_link
            }
        except Exception as e:
            logger.error(f"Error parsing email: {e}")
            return None
    
    def _get_email_body(self, payload: Dict) -> str:
        """Extract the body text from an email payload"""
        body = ""
        if 'parts' in payload:
            for part in payload['parts']:
                if part['mimeType'] == 'text/plain':
                    data = part['body'].get('data', '')
                    body = base64.urlsafe_b64decode(data).decode('utf-8')
                    break
        elif 'body' in payload:
            data = payload['body'].get('data', '')
            if data:
                body = base64.urlsafe_b64decode(data).decode('utf-8')
        return body
    
    def _detect_interview_type(self, subject: str, body: str) -> InterviewType:
        """Detect the type of interview from email content"""
        text = (subject + " " + body).lower()
        
        if any(keyword in text for keyword in ['technical', 'coding', 'algorithm', 'leetcode']):
            return InterviewType.TECHNICAL
        elif any(keyword in text for keyword in ['system design', 'architecture', 'scalability']):
            return InterviewType.SYSTEM_DESIGN
        elif any(keyword in text for keyword in ['behavioral', 'culture fit', 'team fit']):
            return InterviewType.BEHAVIORAL
        elif any(keyword in text for keyword in ['phone screen', 'phone interview', 'initial call']):
            return InterviewType.PHONE_SCREEN
        elif any(keyword in text for keyword in ['hr', 'recruiter', 'screening']):
            return InterviewType.HR_SCREENING
        elif any(keyword in text for keyword in ['final', 'onsite', 'last round']):
            return InterviewType.FINAL_ROUND
        else:
            return InterviewType.OTHER
    
    def _extract_company(self, sender: str, body: str) -> str:
        """Extract company name from email"""
        # Try to extract from sender email domain
        match = re.search(r'@([a-zA-Z0-9-]+)\.(com|org|io|net)', sender)
        if match:
            company = match.group(1)
            # Clean up common variations
            company = company.replace('mail', '').replace('hr', '').replace('jobs', '')
            if company:
                return company.capitalize()
        
        # Try to find company name in body
        match = re.search(r'(?:at|with|from)\s+([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)?)', body)
        if match:
            return match.group(1)
        
        return "Unknown Company"
    
    def _extract_position(self, subject: str, body: str) -> str:
        """Extract job position from email"""
        # Look for common patterns
        patterns = [
            r'(?:for|as)\s+(?:a|an|the)\s+([A-Z][a-zA-Z\s]+(?:Engineer|Developer|Manager|Analyst|Designer))',
            r'([A-Z][a-zA-Z\s]+(?:Engineer|Developer|Manager|Analyst|Designer))\s+(?:position|role)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, subject + " " + body)
            if match:
                return match.group(1).strip()
        
        return "Unknown Position"
    
    def _extract_date(self, body: str) -> Optional[datetime]:
        """Extract interview date from email body"""
        # This is a simplified version - in production you'd want more sophisticated date parsing
        date_patterns = [
            r'(\d{1,2}/\d{1,2}/\d{4})',
            r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}',
        ]
        
        for pattern in date_patterns:
            match = re.search(pattern, body)
            if match:
                try:
                    # Basic date parsing - would need more robust implementation
                    return datetime.now() + timedelta(days=7)  # Placeholder
                except:
                    pass
        
        return None
    
    def _extract_meeting_link(self, body: str) -> Optional[str]:
        """Extract meeting link from email body"""
        # Look for common video conferencing links
        patterns = [
            r'(https?://[\w\-\.]+\.zoom\.us/[^\s<>"]+)',
            r'(https?://meet\.google\.com/[^\s<>"]+)',
            r'(https?://teams\.microsoft\.com/[^\s<>"]+)',
            r'(https?://[\w\-\.]+\.webex\.com/[^\s<>"]+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, body)
            if match:
                return match.group(1)
        
        return None
    
    def _get_mock_interview_emails(self) -> List[Dict]:
        """Return mock interview emails for testing"""
        return [
            {
                'message_id': 'mock_001',
                'subject': 'Technical Interview - Software Engineer Position',
                'sender': 'recruiter@techcorp.com',
                'date': datetime.now().isoformat(),
                'body': 'We would like to schedule a technical interview for the Software Engineer position at TechCorp.',
                'interview_type': InterviewType.TECHNICAL,
                'company': 'TechCorp',
                'position': 'Software Engineer',
                'interview_date': datetime.now() + timedelta(days=3),
                'meeting_link': 'https://zoom.us/j/123456789'
            },
            {
                'message_id': 'mock_002',
                'subject': 'System Design Interview Invitation',
                'sender': 'hr@bigtech.com',
                'date': datetime.now().isoformat(),
                'body': 'Congratulations! You have been selected for a system design interview.',
                'interview_type': InterviewType.SYSTEM_DESIGN,
                'company': 'BigTech',
                'position': 'Senior Software Engineer',
                'interview_date': datetime.now() + timedelta(days=5),
                'meeting_link': 'https://meet.google.com/abc-defg-hij'
            }
        ]

