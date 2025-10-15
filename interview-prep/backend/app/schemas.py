from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List
from app.models import InterviewType, InterviewStatus, PrepSessionStatus


# User Schemas
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: Optional[str] = None


class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


# Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


# Interview Schemas
class InterviewBase(BaseModel):
    company: str
    position: str
    interview_type: InterviewType
    scheduled_date: datetime
    duration_minutes: int = 60
    location: Optional[str] = None
    meeting_link: Optional[str] = None
    description: Optional[str] = None
    recruiter_email: Optional[str] = None


class InterviewCreate(InterviewBase):
    pass


class InterviewUpdate(BaseModel):
    company: Optional[str] = None
    position: Optional[str] = None
    interview_type: Optional[InterviewType] = None
    status: Optional[InterviewStatus] = None
    scheduled_date: Optional[datetime] = None
    duration_minutes: Optional[int] = None
    location: Optional[str] = None
    meeting_link: Optional[str] = None
    description: Optional[str] = None
    notes: Optional[str] = None


class InterviewResponse(InterviewBase):
    id: int
    user_id: int
    status: InterviewStatus
    gmail_message_id: Optional[str]
    calendar_event_id: Optional[str]
    notes: Optional[str]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


# Question Schemas
class QuestionBase(BaseModel):
    question_text: str
    category: Optional[str] = None
    difficulty: Optional[str] = None
    hints: Optional[List[str]] = None
    sample_answer: Optional[str] = None


class QuestionCreate(QuestionBase):
    interview_id: int


class QuestionResponse(QuestionBase):
    id: int
    interview_id: int
    order_index: int
    created_at: datetime
    
    class Config:
        from_attributes = True


# Prep Session Schemas
class PrepSessionBase(BaseModel):
    title: str
    scheduled_start: datetime
    scheduled_end: datetime


class PrepSessionCreate(PrepSessionBase):
    interview_id: int


class PrepSessionUpdate(BaseModel):
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    status: Optional[PrepSessionStatus] = None
    notes: Optional[str] = None


class PrepSessionResponse(PrepSessionBase):
    id: int
    user_id: int
    interview_id: int
    actual_start: Optional[datetime]
    actual_end: Optional[datetime]
    status: PrepSessionStatus
    calendar_event_id: Optional[str]
    notes: Optional[str]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


# Performance Schemas
class PerformanceBase(BaseModel):
    prep_hours: int = 0
    confidence_level: Optional[int] = Field(None, ge=1, le=10)
    outcome: Optional[str] = None
    feedback: Optional[str] = None
    questions_practiced: int = 0


class PerformanceCreate(PerformanceBase):
    interview_id: int


class PerformanceUpdate(BaseModel):
    prep_hours: Optional[int] = None
    confidence_level: Optional[int] = Field(None, ge=1, le=10)
    outcome: Optional[str] = None
    feedback: Optional[str] = None
    questions_practiced: Optional[int] = None


class PerformanceResponse(PerformanceBase):
    id: int
    interview_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


# Interview with Questions
class InterviewWithQuestions(InterviewResponse):
    questions: List[QuestionResponse] = []


# Dashboard Stats
class DashboardStats(BaseModel):
    total_interviews: int
    upcoming_interviews: int
    completed_interviews: int
    total_prep_hours: int
    avg_confidence: Optional[float]
    success_rate: Optional[float]

