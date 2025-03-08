from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Community(Base):
    __tablename__ = "community"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    topic = Column(String, nullable=False)
    peer_feedback_score = Column(Integer, default=0)
