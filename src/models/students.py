from sqlalchemy import Column, String, Date, DateTime
from .base import Base

class Student(Base):
    __tablename__ = "students"

    # Feilds for Students Table
    roll_number = Column('roll_number', String(10), primary_key=True)
    name = Column('name', String(32), nullable=False)
    dob = Column('dob', Date, nullable=False)
    registration_date = Column('registration_date', DateTime, nullable=False)


    def __repr__(self) -> str:
        return "RollNumber-{}, Name-{}, DOB-{}, DATE_OF_REGISTRATION-{} ".format(
                self.roll_number, self.name, self.dob, self.registration_date)
    

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
    def view_students(session):
        """
            Input: Session
            Output: Query Result
        """

        result = session.query(Course).all()

        return result
