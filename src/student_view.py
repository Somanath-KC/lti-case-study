from prompt_toolkit.shortcuts import message_dialog, prompt, button_dialog
import os
from .stu_auth import auth

def center_text(text):
    """
        Calculates center based on text length
    """
    total_terminal_columns = os.get_terminal_size().columns
    text_length = len(text)
    space_on_one_side = (total_terminal_columns - text_length)//2
    space = " " * space_on_one_side

    return space + text + space    

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
    rollNum = prompt("Roll Number >> ")
    while(True):        
        if len(rollNum)==10:
            rollNumber = rollNum
            break
        else:
            rollNum = prompt(" Enter valid 10 digit roll number >> ")

    name = prompt("Name        >> ")
    dob = prompt("DateOfBirth >> ")
    date = " Today date "

    # dic[addTask] = 0      
    # Query for insertion into db required here 

    #print(dic)
    if(evaluate()):
        main(session)


def studentLogin(session):
   
    if auth(session, is_stu=True):
        text = prompt("user@student>> press enter to continue ", 
                bottom_toolbar="\n"+ center_text(
                    "Student Management System (Logged In as @Student)") + "\n")
        print(text)
        student()
    else:
        print(" Invalid credentials ")

def evaluate():
    value = int(prompt("\nDo you want to visit main menu \n1.Yes \n2.No \n"))
    if (value ==1):
        return True
    else:

        # write code to clear session if present 

        print(" Session terminated succesfully ")
        exit()
        
def student():

    dic = dict({"CSE":0,"ECE":0,"EEE":0,"MBA":0,"MECH":0})
    newlist = list()
    #dic1 = dict()
    
    
    a=True
    while(a):
        opt= int(prompt("choose to perform \n 1.View Courses \n 2.Enroll for a Course \n 3.Sign out  \n>>"))

        
        if (opt) == 1:
            print("\n View Courses ")
            i=1
            for key,value in dic.items():
                if dic[key] ==0:
                    print(str(i)+":"+ key)
                    i+=1
            if(evaluate()):
                student()
            
        elif(opt) == 2:

            print("\n Enroll for a Course \n")
            i=0
            for (key),value in dic.items():
                i+=1
                newlist.append(key)
                print("  "+str(i)+" : "+str(key))

            opt = int(prompt("select to Course to Apply \n >>"))-1
            origkey = newlist[opt]
            dic[origkey] = 1

            print(" Applied Succesfully \n ")
            if(evaluate()):
                student()
            
        elif(opt) ==3 :
            print(" \nLogged out Succesfully ")
            break
        else:
            print(" \n invalid opiton") 
            