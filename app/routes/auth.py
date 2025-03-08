from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from passlib.context import CryptContext
from pydantic import BaseModel

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserSignup(BaseModel):
    name: str
    email: str
    password: str
    learning_level: str
    career_goal: str
    preferred_learning_style: str
    available_study_hours: int

@router.post("/signup")
def signup(user: UserSignup, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = pwd_context.hash(user.password)
    new_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password,
        learning_level=user.learning_level,
        career_goal=user.career_goal,
        preferred_learning_style=user.preferred_learning_style,
        available_study_hours=user.available_study_hours
    )
    
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully"}
