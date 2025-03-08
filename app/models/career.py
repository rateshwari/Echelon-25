from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Career(Base):
    __tablename__ = "careers"

    id = Column(Integer, primary_key=True, index=True)
    job_role = Column(String, nullable=False)
    skill_match_percentage = Column(Integer, nullable=False)
    hiring_demand_score = Column(Integer, nullable=False)  
    required_skills = Column(String, nullable=False)  # Comma-separated skills
