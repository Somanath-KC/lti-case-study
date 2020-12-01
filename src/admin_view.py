from .auth_view import auth
from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit import prompt
import os


# ----- #
# Start Helper Functions
# ----- #

def center_text(text):
    """
        Calculates center based on text length
    """
    total_terminal_columns = os.get_terminal_size().columns
    text_length = len(text)
    space_on_one_side = (total_terminal_columns - text_length)//2
    space = " " * space_on_one_side

    return space + text + space



# ----- #
# Start Validators
# ----- #

# Validates Add new Course Data
def validate_new_course(name, duration, fee):
    """
        Input: Course feilds
        Output: Tuple(Status, Message)
    """

    message = ""

    # Course Name validation
    if not (len(name) > 3):
        message = "Course name must contain atleast 3 Characters."
        return False, message

    # Course Duration Validation
    if not(duration.isnumeric()):
        message = "Duration feild has to be integer."
        return False, message

    # Course Fee Validation
    if not(fee.isnumeric()):
        message = "Fee feild has to be integer."
        return False, message

    return True, message


# ----- #
# Start Admin Prompt Functionalities
# ----- #

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

    # Validates input
    status, message = validate_new_course(course_name, course_duration, course_fee)
    if status:
        print("\nAdd Course Successful!")
        admin_prompt()
    else:
        print("\n ",message," Please try again!")
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
            4. Exit
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
        elif text == "4":
            exit()
        else:
            print("\nInvalid Option! Please try again.")


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
