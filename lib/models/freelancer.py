from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config import Base

class Freelancer(Base):
    __tablename__ = 'freelancers'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True) 
    skills = Column(String)

    jobs = relationship("Job", back_populates="freelancer")

    def total_earnings(self):
        """Calculate total earnings from all completed jobs."""
        return sum(payment.amount for job in self.jobs for payment in job.payments if job.status == "completed")

    def __repr__(self):
        return f"<Freelancer(id={self.id}, name='{self.name}', skills='{self.skills}')>"