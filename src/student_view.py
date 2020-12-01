from prompt_toolkit.shortcuts import message_dialog, prompt, button_dialog
import os
from .auth_view import stu_auth
import datetime
from src.models.students import Student

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
def validate_new_course(stu_rollNum, stu_dob, date):
    """
        Input: student feilds
        Output: Tuple(Status, Message)
    """

    message = ""

    # Roll Number validation
    if not (len(stu_rollNum) == 10 ):
        message = "Roll Number must contain 10 Characters."
        return False, message
        

    # Date Validation
    date_format = '%d-%m-%Y'
    if not( datetime.datetime.strptime(date, date_format )):
        message = "Incorrect data format, should be DD-MM-YYYY"
        return False, message
    
    # DOB Validation
    
    if not( datetime.datetime.strptime(date, date_format )):
        message = "Incorrect data format, should be DD-MM-YYYY"
        return False, message
    return True, message


def main(session):
    
    # Choose the role
    is_stu_role = button_dialog(
        title='Student Login',
        text='Choose Login to Continue or get register ',
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

    addTask = print(" Enter details to register \n ")
    stu_rollNum = prompt("Roll Number : ")
    # while(True):        
    #     if len(stu_rollNum)==10:
    #         rollNumber = stu_rollNum
    #         break
    #     else:
    #         rollNum = prompt(" Enter valid 10 digit roll number : ")

    # name = prompt("Name        > ")
    # dob = prompt("DateOfBirth > ")
    # date = prompt("DateOfJoining > ")

    # dic[addTask] = 0      
    # Query for insertion into db required here 
    """
        Allow admin to add new courses to db.
    """
    stu_name = prompt(" Name of the Student: ", 
               bottom_toolbar="\n"+ center_text(
                   "Student Management System (Logged In as @Student)") + "\n")
    
    stu_dob = prompt(" Date of Birth: ", 
               bottom_toolbar="\n"+ center_text(
                   "Student Management System (Logged In as @Student)") + "\n")
    
    date = prompt(" Joining Date: ", 
               bottom_toolbar="\n"+ center_text(
                   "Student Management System (Logged In as @Student)") + "\n")

    # Validates input
    status, message = validate_new_course(stu_rollNum, stu_dob, date)
    if status:
        Student(
               name = stu_name,
               dob = stu_dob,
               registration_date = date,
               roll_number = stu_rollNum).insert(session)
        print("\nRegisterd  Successful!")
        if(evaluate()):

            main(session)
    else:
        print("\n ",message," Please try again!")
        register(session)


    #print(dic)
    if(evaluate()):
        main(session)

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
    