from sqlalchemy import Column, String, Date, DateTime
from .base import Base
import bcrypt

password_salt = b"$2a$10$vI8aWBnW3fID.ZQ4/zo1G.q1lRps.9cGLcZEiGDMVr5yUP1KUOYTa"

class Auth(Base):
    __tablename__ = "auth"

    # Feilds for Auth table
    username = Column('username', String(10), primary_key=True)
    password = Column('password', String, nullable=False)
    last_login = Column('last_login', DateTime, nullable=False)


    def insert(self, session):
        """
            Insert new record to DB.
        """

        self.password = bcrypt.hashpw(self.password.encode('utf-8'), password_salt)

        session.add(self)
        
        try:
            session.commit()
        except:
            session.rollback()
            return False
        
        return True

    
    @staticmethod
    def check_auth(session, username, password):
        pass
