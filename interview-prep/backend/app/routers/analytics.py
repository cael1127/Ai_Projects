from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db
from app import models, schemas, auth
from datetime import datetime, timedelta

router = APIRouter(prefix="/api/analytics", tags=["analytics"])


@router.get("/dashboard", response_model=schemas.DashboardStats)
def get_dashboard_stats(
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get dashboard statistics for the current user"""
    
    # Total interviews
    total_interviews = db.query(func.count(models.Interview.id)).filter(
        models.Interview.user_id == current_user.id
    ).scalar()
    
    # Upcoming interviews
    upcoming_interviews = db.query(func.count(models.Interview.id)).filter(
        models.Interview.user_id == current_user.id,
        models.Interview.status == models.InterviewStatus.UPCOMING,
        models.Interview.scheduled_date > datetime.utcnow()
    ).scalar()
    
    # Completed interviews
    completed_interviews = db.query(func.count(models.Interview.id)).filter(
        models.Interview.user_id == current_user.id,
        models.Interview.status == models.InterviewStatus.COMPLETED
    ).scalar()
    
    # Total prep hours
    total_prep_hours = db.query(func.sum(models.Performance.prep_hours)).filter(
        models.Performance.interview_id.in_(
            db.query(models.Interview.id).filter(
                models.Interview.user_id == current_user.id
            )
        )
    ).scalar() or 0
    
    # Average confidence
    avg_confidence = db.query(func.avg(models.Performance.confidence_level)).filter(
        models.Performance.interview_id.in_(
            db.query(models.Interview.id).filter(
                models.Interview.user_id == current_user.id
            )
        )
    ).scalar()
    
    # Success rate (passed / total completed)
    passed_count = db.query(func.count(models.Performance.id)).filter(
        models.Performance.interview_id.in_(
            db.query(models.Interview.id).filter(
                models.Interview.user_id == current_user.id,
                models.Interview.status == models.InterviewStatus.COMPLETED
            )
        ),
        models.Performance.outcome == 'passed'
    ).scalar()
    
    success_rate = (passed_count / completed_interviews * 100) if completed_interviews > 0 else None
    
    return schemas.DashboardStats(
        total_interviews=total_interviews,
        upcoming_interviews=upcoming_interviews,
        completed_interviews=completed_interviews,
        total_prep_hours=total_prep_hours,
        avg_confidence=float(avg_confidence) if avg_confidence else None,
        success_rate=success_rate
    )


@router.get("/performance/{interview_id}", response_model=schemas.PerformanceResponse)
def get_interview_performance(
    interview_id: int,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get performance data for a specific interview"""
    
    # Verify interview belongs to user
    interview = db.query(models.Interview).filter(
        models.Interview.id == interview_id,
        models.Interview.user_id == current_user.id
    ).first()
    
    if not interview:
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found"
        )
    
    performance = db.query(models.Performance).filter(
        models.Performance.interview_id == interview_id
    ).first()
    
    if not performance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Performance data not found"
        )
    
    return performance


@router.post("/performance", response_model=schemas.PerformanceResponse)
def create_performance_record(
    performance: schemas.PerformanceCreate,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Create a performance record for an interview"""
    
    # Verify interview belongs to user
    interview = db.query(models.Interview).filter(
        models.Interview.id == performance.interview_id,
        models.Interview.user_id == current_user.id
    ).first()
    
    if not interview:
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found"
        )
    
    db_performance = models.Performance(**performance.dict())
    db.add(db_performance)
    db.commit()
    db.refresh(db_performance)
    
    return db_performance


@router.put("/performance/{interview_id}", response_model=schemas.PerformanceResponse)
def update_performance_record(
    interview_id: int,
    performance_update: schemas.PerformanceUpdate,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Update performance data for an interview"""
    
    # Verify interview belongs to user
    interview = db.query(models.Interview).filter(
        models.Interview.id == interview_id,
        models.Interview.user_id == current_user.id
    ).first()
    
    if not interview:
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found"
        )
    
    performance = db.query(models.Performance).filter(
        models.Performance.interview_id == interview_id
    ).first()
    
    if not performance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Performance data not found"
        )
    
    update_data = performance_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(performance, field, value)
    
    performance.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(performance)
    
    return performance

