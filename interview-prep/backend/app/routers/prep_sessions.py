from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas, auth
from datetime import datetime

router = APIRouter(prefix="/api/prep-sessions", tags=["prep_sessions"])


@router.get("/", response_model=List[schemas.PrepSessionResponse])
def get_prep_sessions(
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get all prep sessions for the current user"""
    sessions = db.query(models.PrepSession).filter(
        models.PrepSession.user_id == current_user.id
    ).offset(skip).limit(limit).all()
    
    return sessions


@router.get("/{session_id}", response_model=schemas.PrepSessionResponse)
def get_prep_session(
    session_id: int,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get a specific prep session"""
    session = db.query(models.PrepSession).filter(
        models.PrepSession.id == session_id,
        models.PrepSession.user_id == current_user.id
    ).first()
    
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Prep session not found"
        )
    
    return session


@router.post("/", response_model=schemas.PrepSessionResponse)
def create_prep_session(
    session: schemas.PrepSessionCreate,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Create a new prep session"""
    db_session = models.PrepSession(
        **session.dict(),
        user_id=current_user.id
    )
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    
    return db_session


@router.put("/{session_id}", response_model=schemas.PrepSessionResponse)
def update_prep_session(
    session_id: int,
    session_update: schemas.PrepSessionUpdate,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Update a prep session"""
    db_session = db.query(models.PrepSession).filter(
        models.PrepSession.id == session_id,
        models.PrepSession.user_id == current_user.id
    ).first()
    
    if not db_session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Prep session not found"
        )
    
    update_data = session_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_session, field, value)
    
    db_session.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_session)
    
    return db_session


@router.post("/{session_id}/start")
def start_prep_session(
    session_id: int,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Mark a prep session as started"""
    db_session = db.query(models.PrepSession).filter(
        models.PrepSession.id == session_id,
        models.PrepSession.user_id == current_user.id
    ).first()
    
    if not db_session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Prep session not found"
        )
    
    db_session.actual_start = datetime.utcnow()
    db_session.status = models.PrepSessionStatus.IN_PROGRESS
    db.commit()
    db.refresh(db_session)
    
    return {"message": "Prep session started", "session": db_session}


@router.post("/{session_id}/complete")
def complete_prep_session(
    session_id: int,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Mark a prep session as completed"""
    db_session = db.query(models.PrepSession).filter(
        models.PrepSession.id == session_id,
        models.PrepSession.user_id == current_user.id
    ).first()
    
    if not db_session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Prep session not found"
        )
    
    db_session.actual_end = datetime.utcnow()
    db_session.status = models.PrepSessionStatus.COMPLETED
    db.commit()
    db.refresh(db_session)
    
    return {"message": "Prep session completed", "session": db_session}

