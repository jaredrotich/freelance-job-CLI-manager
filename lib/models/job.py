from sqlalchemy import Column, Integer, String , ForeignKey, Date
from sqlalchemy.orm import relationship
from config import Base

class Job(Base):
    __tablename__ ='jobs'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    deadline = Column(Date)
    status = Column(String)

    freelancer_id = Column(Integer, ForeignKey)