from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from config import Base

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    deadline = Column(Date)
    status = Column(String, default="pending") 
    created_at = Column(DateTime(timezone=True), server_default=func.now()) 

    freelancer_id = Column(Integer, ForeignKey('freelancers.id'))
    freelancer = relationship("Freelancer", back_populates="jobs")
    payments = relationship("Payment", back_populates="job")

    def __repr__(self):
        return f"<Job(id={self.id}, title='{self.title}', status='{self.status}')>"