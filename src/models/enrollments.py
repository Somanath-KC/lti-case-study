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


    def __repr__(self) -> str:
        return "|{:<21} |{:<21} |{:<21} |".format(self.course_id,
                                                  self.roll_number,
                                                  self.date_of_enrollment)

    
    def insert(self, session):
        """
            Input: Session
            Output: Status of transaction.
        """

        session.add(self)
        try:
            session.commit()
        except Exception as e:
            print(e)
            input()
            session.rollback()
            return False
        
        return True


    @staticmethod
    def view_all_enrollments(session):
        """
            Input: Session
            Output: Query Result
        """

        result = session.query(Enrollment).all()

        return result


    @staticmethod
    def view_student_enrollments(session, roll_number):
        """
            Querys the enrollments with given roll number.
        """

        result = session.query(Enrollment).filter_by(roll_number = roll_number).all()

        return result

