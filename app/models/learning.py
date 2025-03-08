from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class LearningPath(Base):
    __tablename__ = "learning_paths"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    course_title = Column(String, nullable=False)
    progress_percentage = Column(Integer, default=0)
    completion_status = Column(String, default="In Progress")  # In Progress, Completed
