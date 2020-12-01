import os
from prompt_toolkit.shortcuts import message_dialog, prompt, button_dialog
from .auth_view import stu_auth
from src.models.students import Student
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
    if not (len(roll_number) == 10 ):
        message = "Roll Number must contain 10 Characters."
        return False, message
    
    # DOB Validation
    date_format = '%d-%m-%Y'
    if not( datetime.strptime(stu_dob, date_format )):
        message = "Incorrect date format, should be DD-MM-YYYY"
        return False, message

    #password validations
    if (password != retype_password):
        message = " Password Mismatch "
        return False, message

    return True, message


def main(session):
    
    # Choose the role
    is_stu_role = button_dialog(
        title='Student Login',
        text='Choose Login to Continue or Get registered ',
        buttons=[
            ('Login', True),
            ('Register', False),
        ],
    ).run()
    if is_stu_role:
        studentLogin(session)
    else:
        register(session)


def register(session):
    """
        Invokes the student registration form.
    """

    addTask = print(" Enter details to register \n ")
    
    roll_number = prompt(" Enter your Roll Number: ", 
               bottom_toolbar="\n"+ center_text(
                   "Student Management System (Logged In as @Student)") + "\n")
    

    stu_name = prompt(" Name of the Student: ", 
               bottom_toolbar="\n"+ center_text(
                   "Student Management System (Logged In as @Student)") + "\n")
    
    stu_dob = prompt(" Date of Birth (DD-MM-YYYY): ", 
               bottom_toolbar="\n"+ center_text(
                   "Student Management System (Logged In as @Student)") + "\n")

    password = prompt(" Password: ",
               is_password=True, 
               bottom_toolbar="\n"+ center_text(
                   "Student Management System (Logged In as @Student)") + "\n")

    retype_password = prompt(" Re-type Password: ",
               is_password=True, 
               bottom_toolbar="\n"+ center_text(
                   "Student Management System (Logged In as @Student)") + "\n")

    date_of_registration = datetime.now()

    # Input Validation
    status, message = validate_new_course(roll_number, stu_dob, password, retype_password)
    if status:
        Student(
               name = stu_name,
               dob = stu_dob,
               registration_date = date_of_registration,
               roll_number = roll_number).insert(session)

        Auth(username = roll_number,
             password = password,
             last_login = datetime.now()).insert(session)
        
        message_dialog(
            title='Registration Successful.',
            text='Press ENTER to Login.').run()
       
        main(session)
    else:
        print("\n ",message," Please try again!")
        register(session)


def stu_prompt():
    """
        Starts Receving input from user.
    """
    while True:
        text = prompt("user@student> ", 
               bottom_toolbar="\n"+ center_text(
                   "Student Management System (Logged In as @Student)") + "\n")
        print(text)


def studentLogin(session):
   
    if stu_auth(session, is_stu=True):
        print(" Press any key to continue .. \n")
        student()
        
        
    else:
        print(" Invalid credentials \n")

def evaluate():
    print("\n Do you want to visit main menu \n 1.Yes \n 2.No \n  ")

    value = int(prompt("user@student> ", 
               bottom_toolbar="\n"+ center_text(
                   "Student Management System (Logged In as @Student)") + "\n"))
    

    if (value ==1):
        return True
    else:

        # write code to clear session if present 
        

        print(" Session terminated succesfully \n")
        exit()
        
def student():

    dic = dict({"CSE":0,"ECE":0,"EEE":0,"MBA":0,"MECH":0})
    newlist = list()
    #dic1 = dict()
    
    
    a=True
    while(a):
        print(""" Choose to Perfrom \n
            1. View Courses
            2. Enroll for a Course
            3. Exit
        """)
        opt = int(prompt("user@student> ", 
               bottom_toolbar="\n"+ center_text(
                   "Student Management System (Logged In as @Student)") + "\n"))
    
        if (opt) == 1:
            print("\n View Courses ")
            i=1
            for key,value in dic.items():
                if dic[key] ==0:
                    print(" "+str(i)+":"+ key)
                    i+=1
            if(evaluate()):
                student()
            
        elif(opt) == 2:

            print("\n Enroll for a Course \n")
            i=0
            for (key),value in dic.items():
                i+=1
                newlist.append(key)
                print("  "+str(i)+":"+str(key))

            print("\nselect to Course to Apply ")

            opt = int(prompt("user@student> ", 
               bottom_toolbar="\n"+ center_text(
                   "Student Management System (Logged In as @Student)") + "\n")) -1
    
            if opt < len(newlist):
                print(len(newlist))
                origkey = newlist[opt]
                dic[origkey] = 1
            else:
                print(" \n select a valid course ")
                
                if(evaluate()):
                    student()
            # Student(
            #   course = origkey).insert(session)
            print(" \n Applied Succesfully \n ")
            if(evaluate()):
                student()
            
        elif(opt) ==3 :
            print(" \nLogged out Succesfully ")
            exit()
        else:
            print(" \n invalid opiton") 
    