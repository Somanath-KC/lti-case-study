from sqlalchemy import Column, String, Date, DateTime
from .base import Base

class Auth(Base):
    __tablename__ = "auth"

    # Feilds for Auth table
    username = Column('username', String(10), primary_key=True)
    password = Column('password', String, nullable=False)
    last_login = Column('last_login', DateTime, nullable=False)
