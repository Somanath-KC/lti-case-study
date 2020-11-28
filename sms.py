#!./venv/bin/python3

from __future__ import unicode_literals
import os
from prompt_toolkit import prompt

# Clear Screen
os.system("clear")

# Welcome Message
print("Welcome to Student Manage System!")



text = prompt('Give me some input: ')
print('You said: %s' % text)