import pyrebase
from Firebase import firebaseConfig
from database import save

firebase = pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

def login():
    print("login here!")
    email = input("enter your email here> ")
    password = input("input a password> ")
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("login successful!")
    except:
        print("something went wrong, check spelling and try again")
    return

def signup():
    print("signup here!")
    name = input("enter your full name> ")
    email = input("enter your email here> ")
    password = input("input a password> ")
    while True:
        role = input("input your role here, choose from either mentor or peer>")
        if role.lower() in ("mentor", "peer"):
            break
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("signup successful!")
        save(name, email, password, role)
    except:
        print("email already exists")
    return

def check():
    choice = input("are you a new user y/n> ")
    if not choice in ["y", "n"]:
        while True:
            choice = input("please choose from y/n> ")
            if choice in ["y", "n"]:
                break
    if choice == "y":
        signup()
    else:
        login()
    return