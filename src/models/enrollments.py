from sqlalchemy import Column, String, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from .base import Base
from datetime import datetime
from .courses import Course
from .students import Student


class Enrollment(Base):
    __tablename__ = "enrollments"

    # Feilds for Enrollment Table
    course_id = Column('course_id', String(10), ForeignKey(Course.course_id), primary_key=True)
    roll_number = Column('roll_number', String(10), ForeignKey(Student.roll_number), primary_key=True)
    date_of_enrollment = Column('date_of_enrollment', DateTime, nullable=False)

