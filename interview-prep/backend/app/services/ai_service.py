from typing import List, Dict
from openai import OpenAI
from app.config import settings
from app.models import InterviewType
import logging

logger = logging.getLogger(__name__)


class AIService:
    """Service for AI-powered question generation and analysis"""
    
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
            base_url=settings.OPENAI_BASE_URL
        )
        self.model = settings.OPENAI_MODEL
    
    def generate_questions(
        self,
        interview_type: InterviewType,
        position: str,
        company: str,
        num_questions: int = 10
    ) -> List[Dict[str, any]]:
        """Generate tailored interview questions using AI"""
        
        prompt = self._build_prompt(interview_type, position, company, num_questions)
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert interview coach who creates highly relevant, tailored interview questions. Return questions in a structured JSON format."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            # Parse the response
            questions = self._parse_questions(response.choices[0].message.content)
            return questions
        
        except Exception as e:
            logger.error(f"Error generating questions: {e}")
            return self._get_fallback_questions(interview_type)
    
    def _build_prompt(
        self,
        interview_type: InterviewType,
        position: str,
        company: str,
        num_questions: int
    ) -> str:
        """Build a prompt for question generation"""
        
        type_descriptions = {
            InterviewType.TECHNICAL: "coding and algorithmic problem-solving",
            InterviewType.BEHAVIORAL: "past experiences, soft skills, and situational",
            InterviewType.SYSTEM_DESIGN: "system architecture and scalability",
            InterviewType.CASE_STUDY: "business problem-solving and analytical",
            InterviewType.HR_SCREENING: "background, motivation, and cultural fit",
            InterviewType.PHONE_SCREEN: "initial screening and basic qualifications",
            InterviewType.FINAL_ROUND: "comprehensive evaluation and decision-making",
        }
        
        description = type_descriptions.get(interview_type, "general interview")
        
        prompt = f"""Generate {num_questions} interview questions for a {position} position at {company}.
This is a {interview_type.value} interview focusing on {description}.

For each question, provide:
1. The question text
2. Category/topic
3. Difficulty level (Easy, Medium, Hard)
4. 2-3 helpful hints
5. A sample answer or approach

Format your response as a JSON array of objects with these fields:
- question_text
- category
- difficulty
- hints (array of strings)
- sample_answer

Make the questions specific, relevant, and appropriately challenging for the position level."""
        
        return prompt
    
    def _parse_questions(self, response_text: str) -> List[Dict[str, any]]:
        """Parse AI response into structured questions"""
        import json
        import re
        
        try:
            # Try to extract JSON from the response
            json_match = re.search(r'\[.*\]', response_text, re.DOTALL)
            if json_match:
                questions_data = json.loads(json_match.group())
                return [
                    {
                        'question_text': q.get('question_text', ''),
                        'category': q.get('category', 'General'),
                        'difficulty': q.get('difficulty', 'Medium'),
                        'hints': q.get('hints', []),
                        'sample_answer': q.get('sample_answer', '')
                    }
                    for q in questions_data
                ]
        except Exception as e:
            logger.error(f"Error parsing questions: {e}")
        
        return []
    
    def _get_fallback_questions(self, interview_type: InterviewType) -> List[Dict[str, any]]:
        """Return fallback questions if AI generation fails"""
        
        technical_questions = [
            {
                'question_text': 'Explain the difference between a process and a thread.',
                'category': 'Operating Systems',
                'difficulty': 'Easy',
                'hints': ['Think about memory space', 'Consider resource sharing'],
                'sample_answer': 'A process is an independent program in execution with its own memory space, while a thread is a lightweight unit of execution within a process that shares the process memory space.'
            },
            {
                'question_text': 'Implement a function to reverse a linked list.',
                'category': 'Data Structures',
                'difficulty': 'Medium',
                'hints': ['Consider using three pointers', 'Think iterative or recursive'],
                'sample_answer': 'Use three pointers (prev, current, next) to iteratively reverse the direction of links in the list.'
            },
            {
                'question_text': 'Design a rate limiter for an API.',
                'category': 'System Design',
                'difficulty': 'Hard',
                'hints': ['Consider token bucket algorithm', 'Think about distributed systems'],
                'sample_answer': 'Use a token bucket algorithm with Redis for distributed rate limiting, tracking requests per user/IP with configurable limits.'
            }
        ]
        
        behavioral_questions = [
            {
                'question_text': 'Tell me about a time you had to deal with a difficult team member.',
                'category': 'Teamwork',
                'difficulty': 'Medium',
                'hints': ['Use STAR method', 'Focus on resolution'],
                'sample_answer': 'Describe Situation, Task, Action taken to address the issue professionally, and positive Result achieved.'
            },
            {
                'question_text': 'Describe a project where you had to learn a new technology quickly.',
                'category': 'Adaptability',
                'difficulty': 'Easy',
                'hints': ['Show learning approach', 'Highlight outcomes'],
                'sample_answer': 'Explain your learning methodology, resources used, and how you successfully applied the new technology.'
            }
        ]
        
        system_design_questions = [
            {
                'question_text': 'Design a URL shortening service like bit.ly.',
                'category': 'System Design',
                'difficulty': 'Medium',
                'hints': ['Think about hashing', 'Consider scalability'],
                'sample_answer': 'Use base62 encoding, NoSQL database for fast lookups, load balancers, caching layer, and analytics tracking.'
            }
        ]
        
        question_map = {
            InterviewType.TECHNICAL: technical_questions,
            InterviewType.BEHAVIORAL: behavioral_questions,
            InterviewType.SYSTEM_DESIGN: system_design_questions,
        }
        
        return question_map.get(interview_type, technical_questions)
    
    def analyze_performance(self, user_responses: List[str]) -> Dict[str, any]:
        """Analyze user's practice responses and provide feedback"""
        try:
            prompt = f"""Analyze these interview practice responses and provide constructive feedback:

Responses:
{chr(10).join([f'{i+1}. {resp}' for i, resp in enumerate(user_responses)])}

Provide:
1. Overall confidence score (1-10)
2. Strengths identified
3. Areas for improvement
4. Specific recommendations

Format as JSON."""
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert interview coach providing constructive feedback."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            
            # Parse and return analysis
            return {"analysis": response.choices[0].message.content}
        
        except Exception as e:
            logger.error(f"Error analyzing performance: {e}")
            return {"analysis": "Unable to generate analysis at this time."}

