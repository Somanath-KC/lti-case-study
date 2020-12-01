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
                   "admin Management System (Logged In as @Administrator)") + "\n")

def evaluate():
    value = int(prompt("\n Do you want to visit main menu \n 1.Yes \n 2.No \n \n > "))
    if (value ==1):
        return True
    else:

        # write code to clear session if present 

        print(" Session terminated succesfully \n")
        exit()
        

def admin():
    dic = dict({"CSE":0,"ECE":0,"EEE":0,"MBA":0,"MECH":0})
    newlist = list()

    opt = int(prompt("Select one to perform \n 1.Add new course \n 2.View Courses \n 3.View admin\n > "))
    if opt ==1:
        course = prompt(" Enter course to add Ex:CSE,ECE.. \n > ")
        if  len(course) ==3:

            # query to insert course required here 
            print(" Added Sucessfully \n ")
            
        else:
            course = prompt(" Please Enter valid course of lenght 3 characters \n > ")

        if(evaluate()):
            admin()

    elif opt ==2:
        print(" List of Courses ") 

        # query to fetch courses from db 
        i=1
        for key,value in dic.items():
            if dic[key] ==0:
                print(" "+str(i)+":"+ key)
                i+=1
        if(evaluate()):
            admin()    
    elif opt==3:
        print(" List of Registered Studendts ")

        # query to get list of  admins from db and display here 
        if(evaluate()):
            admin()
    else:
        print("invalid option ")
        if(evaluate()):
            admin() 


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
    admin()
