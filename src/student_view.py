import os
from src.models.enrollments import Enrollment
from prompt_toolkit.shortcuts import message_dialog, prompt, button_dialog
from .auth_view import stu_auth
from src.models.students import Student
from src.models.courses import Course
from src.models.auth import Auth
from datetime import datetime


def center_text(text):
    """
        Calculates center based on text length
    """
    total_terminal_columns = os.get_terminal_size().columns
    text_length = len(text)
    space_on_one_side = (total_terminal_columns - text_length)//2
    space = " " * space_on_one_side

    return space + text + space


# Validates Add new Course Data
def validate_new_course(roll_number, stu_dob, password, retype_password):
    """
        Input: student feilds
        Output: Tuple(Status, Message)
    """

    message = ""

    # Roll Number validation
    if not (len(roll_number) == 10):
        message = "Roll Number must contain 10 Characters."
        return False, message

    # DOB Validation
    date_format = '%d-%m-%Y'
    if not(datetime.strptime(stu_dob, date_format)):
        message = "Incorrect date format, should be DD-MM-YYYY"
        return False, message

    # Password validations
    if (password != retype_password):
        message = " Password Mismatch "
        return False, message

    return True, message


def main(session):

    # Choose option Login/Register

    student_register = button_dialog(
        title='Student Login',
        text='Choose Login to Continue or Get registered ',
        buttons=[
            ('Login', False),
            ('Register', True),
        ],
    ).run()

    if student_register:
        register(session)
    else:
        auth_status, username = stu_auth(session, is_stu=True)

        if auth_status:
            session.student_username = username
            stu_prompt(session)
        else:
            message_dialog(
                title='Authentication Failed',
                text='Invalid Username/Password. Press ENTER to try again.').run()
            main(session)


def register(session):
    """
        Invokes the student registration form.
    """

    addTask = print(" Enter details to register \n ")

    roll_number = prompt(" Enter your Roll Number: ",
               bottom_toolbar="\n" + center_text(
                   "Student Management System (Logged In as @Student)") + "\n")

    stu_name = prompt(" Name of the Student: ",
               bottom_toolbar="\n" + center_text(
                   "Student Management System (Logged In as @Student)") + "\n")

    stu_dob = prompt(" Date of Birth (DD-MM-YYYY): ",
               bottom_toolbar="\n" + center_text(
                   "Student Management System (Logged In as @Student)") + "\n")

    password = prompt(" Password: ",
               is_password=True,
               bottom_toolbar="\n" + center_text(
                   "Student Management System (Logged In as @Student)") + "\n")

    retype_password = prompt(" Re-type Password: ",
               is_password=True,
               bottom_toolbar="\n" + center_text(
                   "Student Management System (Logged In as @Student)") + "\n")

    date_of_registration = datetime.now()

    # Input Validation
    status, message = validate_new_course(roll_number,
                                          stu_dob, password,
                                          retype_password)
    if status:
        status_1 = Student(
               name=stu_name,
               dob=stu_dob,
               registration_date=date_of_registration,
               roll_number=roll_number).insert(session)

        status_2 = Auth(username=roll_number,
             password=password,
             last_login=datetime.now()).insert(session)

        if status_1 and status_2:
            message_dialog(
                title='Registration Successful.',
                text='Press ENTER to Login.').run()
        else:
            message_dialog(title='Error in Registration',
                           text='Please Try again!. Press ENTER to Continue.').run()
            register(session)

        main(session)
    else:
        print("\n ", message, " Please try again!")
        register(session)


def prompt_view_courses(session):
    """
        Shows the available courses in db.
    """
    result = Course.view_courses(session)
    Course.print_header()

    for i in result:
        print(i)

    stu_prompt(session)


def prompt_enroll_for_course(session):
    """
        Enrolls student to available courses
    """
    # Displays the available courses
    result = Course.view_courses(session)
    Course.print_header()
    for i in result:
        print(i)

    # Course registration prompt
    course_id = prompt("\n Enter Course ID from above list to enroll: ",
                    bottom_toolbar="\n" + center_text(
                    "Student Management System (Logged In as @Student)") + "\n")

    if session.query(Course).get(course_id) is not None:
        new_enroll = Enrollment()
        new_enroll.roll_number = session.student_username
        new_enroll.course_id = course_id
        new_enroll.date_of_enrollment = datetime.now()

        if new_enroll.insert(session):
            print("\nEnrollment Success!")
        else:
            print("\n Error enrolling course. Please try again!")
            stu_prompt(session)
    else:
        print("Please Enter Valid Course ID.")

    stu_prompt(session)


def prompt_view_my_courses(session):
    """
        Displays the enrolled courses
    """
    data = Enrollment.view_student_enrollments(session)

    if len(data) < 1:
        print("\n No Enrollments Found!")
        stu_prompt(session)
    else:
        Enrollment.print_header()
        for i in data:
            print(i)
        stu_prompt(session)


def stu_prompt(session):
    """
        Starts Receving input from user.
    """

    while True:
        print("\nWelcome Student.")
        print("\n Choose one option to continue.")
        print("""
            1. View Available Courses
            2. Enroll for Course
            3. View my Courses
            4. Exit
        """)
        text = prompt("user@student\\{}> ".format(session.student_username),
                       bottom_toolbar="\n" + center_text(
                   "Student Management System (Logged In as @Student)") + "\n")

        if text == "1":
            prompt_view_courses(session)
        elif text == "2":
            prompt_enroll_for_course(session)
        elif text == "3":
            prompt_view_my_courses(session)
        elif text == "4":
            exit()
        else:
            print("\nInvalid Option! Please try again.")
