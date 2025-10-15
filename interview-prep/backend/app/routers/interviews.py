from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas, auth
from app.services.gmail_service import GmailService
from app.services.calendar_service import CalendarService
from app.services.ai_service import AIService
from google.oauth2.credentials import Credentials
from datetime import datetime
import logging

router = APIRouter(prefix="/api/interviews", tags=["interviews"])
logger = logging.getLogger(__name__)


def get_user_credentials(user: models.User) -> Credentials:
    """Get Google credentials for user"""
    if not user.google_access_token:
        return None
    
    return Credentials(
        token=user.google_access_token,
        refresh_token=user.google_refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=user.google_id,
        client_secret=""
    )


@router.get("/", response_model=List[schemas.InterviewResponse])
def get_interviews(
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get all interviews for the current user"""
    interviews = db.query(models.Interview).filter(
        models.Interview.user_id == current_user.id
    ).offset(skip).limit(limit).all()
    
    return interviews


@router.get("/{interview_id}", response_model=schemas.InterviewWithQuestions)
def get_interview(
    interview_id: int,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get a specific interview with questions"""
    interview = db.query(models.Interview).filter(
        models.Interview.id == interview_id,
        models.Interview.user_id == current_user.id
    ).first()
    
    if not interview:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found"
        )
    
    return interview


@router.post("/", response_model=schemas.InterviewResponse)
def create_interview(
    interview: schemas.InterviewCreate,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Create a new interview"""
    db_interview = models.Interview(
        **interview.dict(),
        user_id=current_user.id
    )
    db.add(db_interview)
    db.commit()
    db.refresh(db_interview)
    
    return db_interview


@router.put("/{interview_id}", response_model=schemas.InterviewResponse)
def update_interview(
    interview_id: int,
    interview_update: schemas.InterviewUpdate,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Update an interview"""
    db_interview = db.query(models.Interview).filter(
        models.Interview.id == interview_id,
        models.Interview.user_id == current_user.id
    ).first()
    
    if not db_interview:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found"
        )
    
    # Update fields
    update_data = interview_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_interview, field, value)
    
    db_interview.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_interview)
    
    return db_interview


@router.delete("/{interview_id}")
def delete_interview(
    interview_id: int,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Delete an interview"""
    db_interview = db.query(models.Interview).filter(
        models.Interview.id == interview_id,
        models.Interview.user_id == current_user.id
    ).first()
    
    if not db_interview:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found"
        )
    
    db.delete(db_interview)
    db.commit()
    
    return {"message": "Interview deleted successfully"}


@router.post("/{interview_id}/questions", response_model=List[schemas.QuestionResponse])
def generate_questions(
    interview_id: int,
    num_questions: int = 10,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Generate AI-powered questions for an interview"""
    interview = db.query(models.Interview).filter(
        models.Interview.id == interview_id,
        models.Interview.user_id == current_user.id
    ).first()
    
    if not interview:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found"
        )
    
    # Generate questions using AI
    ai_service = AIService()
    questions_data = ai_service.generate_questions(
        interview_type=interview.interview_type,
        position=interview.position,
        company=interview.company,
        num_questions=num_questions
    )
    
    # Save questions to database
    db_questions = []
    for idx, q_data in enumerate(questions_data):
        db_question = models.Question(
            interview_id=interview_id,
            question_text=q_data['question_text'],
            category=q_data['category'],
            difficulty=q_data['difficulty'],
            hints=q_data['hints'],
            sample_answer=q_data['sample_answer'],
            order_index=idx
        )
        db.add(db_question)
        db_questions.append(db_question)
    
    db.commit()
    for q in db_questions:
        db.refresh(q)
    
    return db_questions


@router.post("/sync-from-gmail")
def sync_interviews_from_gmail(
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Sync interviews from Gmail"""
    credentials = get_user_credentials(current_user)
    gmail_service = GmailService(credentials)
    
    emails = gmail_service.get_interview_emails()
    
    synced_count = 0
    for email_data in emails:
        # Check if interview already exists
        existing = db.query(models.Interview).filter(
            models.Interview.gmail_message_id == email_data['message_id']
        ).first()
        
        if not existing and email_data.get('interview_date'):
            interview = models.Interview(
                user_id=current_user.id,
                company=email_data['company'],
                position=email_data['position'],
                interview_type=email_data['interview_type'],
                scheduled_date=email_data['interview_date'],
                meeting_link=email_data.get('meeting_link'),
                recruiter_email=email_data['sender'],
                gmail_message_id=email_data['message_id'],
                description=email_data['body'][:500]
            )
            db.add(interview)
            synced_count += 1
    
    db.commit()
    
    return {"message": f"Synced {synced_count} interviews from Gmail"}


@router.post("/{interview_id}/schedule-prep")
def schedule_prep_sessions(
    interview_id: int,
    days_before: int = 3,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Schedule prep sessions for an interview"""
    interview = db.query(models.Interview).filter(
        models.Interview.id == interview_id,
        models.Interview.user_id == current_user.id
    ).first()
    
    if not interview:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found"
        )
    
    credentials = get_user_credentials(current_user)
    calendar_service = CalendarService(credentials)
    
    interview_title = f"{interview.company} - {interview.position}"
    event_ids = calendar_service.schedule_prep_blocks(
        interview_date=interview.scheduled_date,
        interview_title=interview_title,
        days_before=days_before
    )
    
    # Create prep session records
    from datetime import timedelta
    prep_sessions = []
    for day, event_id in enumerate(event_ids, start=1):
        prep_date = interview.scheduled_date - timedelta(days=days_before - day + 1)
        prep_start = prep_date.replace(hour=19, minute=0, second=0, microsecond=0)
        prep_end = prep_start + timedelta(minutes=90)
        
        prep_session = models.PrepSession(
            user_id=current_user.id,
            interview_id=interview_id,
            title=f"Prep Session #{day} - {interview_title}",
            scheduled_start=prep_start,
            scheduled_end=prep_end,
            calendar_event_id=event_id
        )
        db.add(prep_session)
        prep_sessions.append(prep_session)
    
    db.commit()
    
    return {
        "message": f"Scheduled {len(prep_sessions)} prep sessions",
        "sessions": len(prep_sessions)
    }

