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


# Admin Prompt actions functionality
def prompt_add_new_course():
    """
        Allow admin to add new courses to db.
    """
    course_name = prompt(" Name of the Course?: ", 
               bottom_toolbar="\n"+ center_text(
                   "Student Management System (Logged In as @Administrator)") + "\n")
    
    course_duration = prompt(" Duration of the Course? (In Hours): ", 
               bottom_toolbar="\n"+ center_text(
                   "Student Management System (Logged In as @Administrator)") + "\n")
    
    course_fee = prompt(" Fee for the Course? (INR): ", 
               bottom_toolbar="\n"+ center_text(
                   "Student Management System (Logged In as @Administrator)") + "\n")
    
    if course_name and course_duration and course_fee:
        print("Add Course Successful!")
        admin_prompt()
    else:
        prompt_add_new_course()

def prompt_view_courses():
    """
        Shows the available courses in db.
    """
    pass


def prompt_view_student():
    """
        View the details of given student rollnumber
    """
    pass


def admin_prompt():
    """
        Starts Receving input from user.
    """
    while True:
        print("\nWelcome Admin.")
        print("\n Choose one option to continue.")
        print("""
            1. Add a new Course
            2. View Courses
            3. View Student
        """)
        text = prompt("user@admin> ", 
               bottom_toolbar="\n"+ center_text(
                   "Student Management System (Logged In as @Administrator)") + "\n")
        
        if text == "1":
            prompt_add_new_course()
        elif text == "2":
            prompt_view_courses()
        elif text == "3":
            prompt_view_student()


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