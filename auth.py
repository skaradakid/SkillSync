import pyrebase
from Firebase import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

def login():
    pass

def signup():
    print("signup here!")
    email = input("enter your email here> ")
    password = input("input a password> ")
    while True:
        role = input("input your role here, choose from either mentor or peer>")
        if role.lower() in ("mentor", "peer"):
            break
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("login successful!")
    except:
        print("email already exists")
    return

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
