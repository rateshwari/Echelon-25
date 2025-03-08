from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.learning import LearningPath
from pydantic import BaseModel

router = APIRouter()

@router.get("/")
def get_dashboard(user_id: int, db: Session = Depends(get_db)):
    learning_progress = db.query(LearningPath).filter(LearningPath.user_id == user_id).all()
    return {"progress": learning_progress}
