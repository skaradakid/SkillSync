import pyrebase
import booking
from database import save

# Firebase configuration
FirebaseConfig = {
    "apiKey": "AIzaSyAWzyRl5iSWIcu8K2uN5Avzwoz2h9IeE-I",
  "authDomain": "skillsync-706d4.firebaseapp.com",
  "databaseURL": "https://skillsync-706d4-default-rtdb.firebaseio.com",
  "projectId": "skillsync-706d4",
  "storageBucket": "skillsync-706d4.firebasestorage.app",
  "messagingSenderId": "822785045283",
  "appId": "1:822785045283:web:84b3de62fe16a15db45296"
}

firebase = pyrebase.initialize_app(FirebaseConfig)
auth=firebase.auth()
db = firebase.database()

def login():
    print("login here!")
    email = input("enter your email here> ")
    password = input("input a password> ")
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("login successful!")
        booking.find_users_document(user, db)
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
        save(user['localId'],name, email, password, role)
        booking.find_users_document(user, db)
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