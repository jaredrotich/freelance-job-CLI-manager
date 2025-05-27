from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from config import Base

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    amount = Column(Float)

    job_id = Column(Integer, ForeignKey('jobs.id'))
    job = relationship("Job", back_populates="payments")

    def __repr__(self):
         return f"<Payment(id={self.id}, amount={self.amount})>"
