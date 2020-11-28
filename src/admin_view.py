from .auth_view import auth
from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit import prompt
import os


def center_text(text):
    """
        Calculates center based on text length
    """
    total_terminal_columns = os.get_terminal_size().columns
    text_length = len(text)
    space_on_one_side = (total_terminal_columns - text_length)//2
    space = " " * space_on_one_side

    return space + text + space    


def admin_prompt():
    """
        Starts Receving input from user.
    """
    while True:
        text = prompt("user@admin> ", 
               bottom_toolbar="\n"+ center_text(
                   "Student Management System (Logged In as @Administrator)") + "\n")
        print(text)


def main(session):
    """
        Entry Point for admin view.
    """

    # Authenticate admin user
    while True:
        if auth(session, is_admin=True):
            break
        else:    
            message_dialog(
                title='Authentication Failed',
                text='Invalid Username/Password. Press ENTER to try again.').run()


    # Start Admin Prompt
    admin_prompt()