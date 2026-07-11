from utils import *
from users import *

# User Dashboard
def dashboard(user):
    while True:
        print("Select a choice(0-5):")
        print("0. Logout\n1. Add a movie\n2. List all movies\n3. Add a review\n4. Edit a review\n5. Delete a review")

        c = input("Enter the choice: ")
        
        if c == '0':
            print("You have logged out successfully...")
            exit()

        elif c == '1':
            pass

        elif c == '2':
            pass

        elif c == '3':
            pass

        elif c == '4':
            pass

        elif c == '5':
            pass

        else:
            print("Invalid Choice. Please enter your choice between 0-5")


while True:
    print("----------- WELCOME TO MOVIE REVIEW SYSTEM -----------")
    print("0. Exit\n1. Register\n2. Login")

    ch = input("Please enter a choice (0/1/2): ")

    if ch == '0':
        break

    elif ch == '1':
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        email = input("Enter the email: ")

        register_user = register(username, password, email)
        print("User has been registered successfully..")

    elif ch == '2':
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