from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.career import Career

router = APIRouter()

@router.get("/")
def get_career_paths(db: Session = Depends(get_db)):
    careers = db.query(Career).all()
    return careers
