
# Student Management System(SMS) LTI Case Study

**Overview**

XYZ College has come up with the requirement of developing a console based application to basically
manage the details of all the students who register with the college.

You need to develop a standalone console based application using Java/C#/Python which will be
responsible for taking care of the above requirement. You can use any database of choice for this case
study

**Admin View Demo 👇**

[![Admin View Demo](https://img.youtube.com/vi/ohIAJWyYAPE/0.jpg)](https://www.youtube.com/watch?v=ohIAJWyYAPE)

**Student View Demo 👇**

[![Student View Demo](https://img.youtube.com/vi/W_U5pyTPitI/0.jpg)](https://www.youtube.com/watch?v=W_U5pyTPitI)

**Tech Stack**

The tech stack used for this project includes

- Python3
- SqlAlchamey
- Prompt Toolkit
- SQLite3



**Project Structure** 
```

├── README.md
├── sms.py
├── requirements.txt
└── src
    ├─ __init__.py
    ├── admin_view.py
    ├── auth_view.py
    ├── student_view.py
    ├── models
	    ├── ├── __init__.py
	 	├── auth.py
		├── base.py
		├── courses.py
	 	├── students.py   
 ``` 
 
**Environment Setup**
1. Clone this repo
	 ```
	 $ git clone https://github.com/Somanath-KC/lti-case-study.git
	 ```
 
2. Get into project directory
	 ```
	 $ cd lit-case-study
	 ```
4. Installing Dependencies
	 ```
	 $ pip3 install -r requirements.txt
	 ```
	 
4. Run the Application
	 ```
	 $ python3 sms.py
	 ```
**Things to Keep in mind :**

- For Student | Admin
   - Roll Number must contains length of 10 Characters
   - Date should be in DD-MM-YYY format 
    - Course characters length  should be >= 3 
 
 **Default Login Credentials**
 
 - For Admin
 ```
   - Username: admin
   - Password: 1234
 ```
 - For Student
  ```
   - Username: 16me1a0579
   - Password: 1234
 ```
 
**Developers**
-
Follow us  for more updates
 1. https://github.com/Somanath-KC
 2. https://github.com/pavankalyannv
