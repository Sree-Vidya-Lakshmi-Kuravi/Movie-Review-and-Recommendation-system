from utils import *

users_file = r'E:\Vidya Career\Movie_Review_Project\MRS_without_SQL\data\users.csv'

def register(username, password, email):
    '''
    Registers a new user with the provided username, password, and email.
    Returns a success message if registration is successful, 
    or an error message if the username or email already exists.
    '''
    if not username or not password or not email:
        return "All fields are required."
    
    users = read_csv(users_file)
    
    for user in users:
        if user['username'] == username:
            return "Username already exists."
        if user['email'] == email:
            return "Email already registered."
    
    new_user = {
        'id': generate_id(users_file),
        'username': username,
        'password': password,
        'email': email
    }
    
    write_row(users_file, new_user)
    return "User registered successfully."

# register("sailaja2", "saila", "sail2.k@gmail.com")


# ----------- User login ------------
def login(credential, log_password):
    '''
    Logs in a user using either their username or email and password.
    Returns a success message if login is successful,
    or an error message if the credentials are invalid.
    '''
    users = read_csv(users_file)

    for user in users:
        if (user['username'] == credential or user['email'] == credential) and user['password'] == log_password:
            return "Login successful.", user
    return "Invalid credentials."

# ----------- Get user by ID  ------------
def get_user_by_id(user_id):
    users = read_csv(users_file)
    
    for user in users:
        if user['id'] == str(user_id):
            return user
    return None

# ----------- Get user by username ------------
def get_user_by_username(username):
    users = read_csv(users_file)
    
    for user in users:
        if user['username'] == username:
            return user
    return None

# ----------- Get user by email ------------
def get_user_by_email(email):
    users = read_csv(users_file)
    
    for user in users:
        if user['email'] == email:
            return user
    return None