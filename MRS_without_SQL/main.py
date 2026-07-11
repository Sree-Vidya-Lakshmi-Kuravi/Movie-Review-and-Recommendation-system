from utils import *
from users import *

def dashboard(user):
    pass

while True:
    print("----------- WELCOME TO MOVIE REVIEW SYSTEM -----------")
    print("0. Exit\n1. Register\n2. Login")

    ch = int(input("Please enter a choice (0/1/2): "))

    if ch == 0:
        break

    elif ch == 1:
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        email = input("Enter the email: ")

        register_user = register(username, password, email)
        print("User has been registered successfully..")

    elif ch == 2:
        print("Enter your details to login")
        credential = input("Enter your credential(username or email): ")
        log_password = input("Enter your password: ")

        output = login(credential, log_password)
        if output[0] == 'Login successful.':
            user = output[1]
            dashboard(user)
        else:
            print("Login failed..", output[0])
        

    else:
        print("Wrong Choice...")