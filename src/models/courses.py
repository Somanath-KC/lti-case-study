from sqlalchemy import Column, String, Date, DateTime, Integer
from .base import Base

class Course(Base):
    __tablename__ = "courses"

    # Feilds for Courses Table
    course_id = Column('course_id', String(10), primary_key=True)
    name = Column('name', String(64), nullable=False)
    duration_in_hours = Column('duration_in_hours', Integer, nullable=False)
    fee = Column('fee', Integer, nullable=False)
    date_of_creation = Column('date_of_creation', DateTime, nullable=False)

    
    def __repr__(self) -> str:
        return "COURSE_ID-{}, NAME-{}, DURAION-{}Hrs., FEE-{}, COURSE_CREATION_DATE-{}".format(self.course_id, self.name,
                     self.duration_in_hours, 
                     self.fee, self.date_of_creation)


    def insert(self, session):
        """
            Input: Session
            Output: Status of transaction.
        """

        session.add(self)
        try:
            session.commit()
        except:
            session.rollback()
            return False
        
        return True

    @staticmethod
    def view_courses(session):
        """
            Input: Session
            Output: Query Result
        """

        result = session.query(Course).all()

        return result