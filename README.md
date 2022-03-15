Django project application

The aim of the project is to write a web-based application using djang and Python. 
Tools
•	The Python programming language
•	The Django web framework
•	The PostgreSQL database for persisting data
•	The Postages extension for supporting spatial features in the PostgreSQL database
•	pip for installing dependencies
•	The venv module for managing a virtual environment
Setup
The first thing to do is to clone the repository:
$ git clone https://github.com/molotomt/.git

Create a virtual environment to install dependencies in and activate it
   

Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.
Once pip has finished downloading the dependencies:
(env)$ cd project
(env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000/.

Walkthrough
When you navigate to:
http://127.0.0.1:8000/admin/ - you will be able to add or delete user profile
				see the longitude and latitude 

http://127.0.0.1:8000/admin/auth/user/add/ “
•	you will be able to register by entering the 
•	username
•	password
•	confirm password
•	home address
•	phone number
•	location (point geometry)

http://127.0.0.1:8000/admin/kortazaapp/userdetails/

•	You will be able to see the user details
•	Dropdown to delete the details
•	add button on the side

http://127.0.0.1:8000/admin/kortazaapp/userprofile/add/ 
•	choose user
•	upload a map.png
Tests
To run the tests, cd into the directory where manage.py is:
(env)$ python manage.py runserver
 

