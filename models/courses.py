from sqlalchemy import Column, String, Date, DateTime, Integer
from .base import Base

class Courses(Base):
    __tablename__ = "courses"

    # Feilds for Courses Table
    course_id = Column('course_id', String(10), primary_key=True)
    name = Column('name', String(64), nullable=False)
    duration_in_hours = Column('duration_in_hours', Integer, nullable=False)
    fee = Column('fee', Integer, nullable=False)
    date_of_creation = Column('date_of_creation', DateTime, nullable=False)
