from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    learning_level = Column(String, nullable=False)  # Beginner, Intermediate, Advanced
    career_goal = Column(String, nullable=False)  
    preferred_learning_style = Column(String, nullable=True)  # Visual, Auditory, Hands-on
    available_study_hours = Column(Integer, nullable=True)  
