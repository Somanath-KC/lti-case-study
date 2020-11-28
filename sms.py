#!./venv/bin/python3

from __future__ import unicode_literals
import os
from prompt_toolkit import prompt
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import auth, base, students, courses


# Clear Screen
os.system("clear")

# Database Configuration
engine = create_engine("sqlite:///smsapp.db")
base.Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)
session = Session()

# Welcome Message
print("Welcome to Student Manage System!")



text = prompt('Give me some input: ')
print('You said: %s' % text)