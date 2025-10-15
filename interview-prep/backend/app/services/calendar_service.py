from datetime import datetime, timedelta
from typing import Optional, Dict
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from app.config import settings
import logging

logger = logging.getLogger(__name__)


class CalendarService:
    """Service for interacting with Google Calendar API"""
    
    def __init__(self, credentials: Optional[Credentials] = None, mock_mode: bool = None):
        self.mock_mode = mock_mode if mock_mode is not None else settings.MOCK_MODE
        self.credentials = credentials
        self.service = None
        
        if not self.mock_mode and credentials:
            try:
                self.service = build('calendar', 'v3', credentials=credentials)
            except Exception as e:
                logger.error(f"Failed to build Calendar service: {e}")
                self.mock_mode = True
    
    def create_prep_session(
        self,
        title: str,
        start_time: datetime,
        end_time: datetime,
        description: Optional[str] = None
    ) -> Optional[str]:
        """Create a prep session event in Google Calendar"""
        if self.mock_mode:
            return self._create_mock_event(title, start_time, end_time)
        
        try:
            event = {
                'summary': title,
                'description': description or 'Interview preparation session',
                'start': {
                    'dateTime': start_time.isoformat(),
                    'timeZone': 'UTC',
                },
                'end': {
                    'dateTime': end_time.isoformat(),
                    'timeZone': 'UTC',
                },
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                        {'method': 'email', 'minutes': 24 * 60},
                        {'method': 'popup', 'minutes': 30},
                    ],
                },
            }
            
            created_event = self.service.events().insert(
                calendarId='primary',
                body=event
            ).execute()
            
            return created_event.get('id')
        
        except HttpError as error:
            logger.error(f"An error occurred: {error}")
            return None
    
    def schedule_prep_blocks(
        self,
        interview_date: datetime,
        interview_title: str,
        days_before: int = 3,
        session_duration: int = 90
    ) -> list[str]:
        """Automatically schedule prep blocks before an interview"""
        event_ids = []
        
        # Create multiple prep sessions leading up to the interview
        for day in range(days_before, 0, -1):
            prep_date = interview_date - timedelta(days=day)
            # Schedule in the evening (7 PM)
            prep_start = prep_date.replace(hour=19, minute=0, second=0, microsecond=0)
            prep_end = prep_start + timedelta(minutes=session_duration)
            
            title = f"Prep Session #{days_before - day + 1} - {interview_title}"
            description = f"Preparation session for {interview_title} interview scheduled on {interview_date.strftime('%Y-%m-%d')}"
            
            event_id = self.create_prep_session(title, prep_start, prep_end, description)
            if event_id:
                event_ids.append(event_id)
        
        return event_ids
    
    def update_event(self, event_id: str, updates: Dict) -> bool:
        """Update an existing calendar event"""
        if self.mock_mode:
            logger.info(f"Mock: Would update event {event_id} with {updates}")
            return True
        
        try:
            event = self.service.events().get(
                calendarId='primary',
                eventId=event_id
            ).execute()
            
            # Apply updates
            for key, value in updates.items():
                if key in ['start', 'end']:
                    event[key] = {
                        'dateTime': value.isoformat(),
                        'timeZone': 'UTC',
                    }
                else:
                    event[key] = value
            
            updated_event = self.service.events().update(
                calendarId='primary',
                eventId=event_id,
                body=event
            ).execute()
            
            return True
        
        except HttpError as error:
            logger.error(f"An error occurred: {error}")
            return False
    
    def delete_event(self, event_id: str) -> bool:
        """Delete a calendar event"""
        if self.mock_mode:
            logger.info(f"Mock: Would delete event {event_id}")
            return True
        
        try:
            self.service.events().delete(
                calendarId='primary',
                eventId=event_id
            ).execute()
            return True
        
        except HttpError as error:
            logger.error(f"An error occurred: {error}")
            return False
    
    def _create_mock_event(self, title: str, start_time: datetime, end_time: datetime) -> str:
        """Create a mock event ID"""
        import hashlib
        event_str = f"{title}_{start_time.isoformat()}"
        return hashlib.md5(event_str.encode()).hexdigest()[:16]

