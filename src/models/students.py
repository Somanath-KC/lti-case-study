from sqlalchemy import Column, String, Date, DateTime
from .base import Base

class Students(Base):
    __tablename__ = "students"

    # Feilds for Students Table
    roll_number = Column('roll_number', String(10), primary_key=True)
    name = Column('name', String(32), nullable=False)
    dob = Column('dob', Date, nullable=False)
    registration_date = Column('registration_date', DateTime, nullable=False)
