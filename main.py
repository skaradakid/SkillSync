import pyrebase
from firebase import(firebaseconfig)

firebase = pyrebase.initialize_app(firebaseconfig)
auth=firebase.auth()

def login():
    print("log in")
    email = input("input your email account>> ")
    password = input("input password>>")
    try:
        user = auth.create_user_with_email_and_password(email, password)
    except:
        print("email already exists or in incorrect")
    return

def signup():
    print("sign up")
    email = input("input your email account>> ")
    password = input("input password>>")
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("log in successful")
    except:
        print("invalid email or password")
    return

respond = input("1-login\n2-create new account")

while respond not in ["1", "2"]:
    respond = input("pick 1 to login\npick 2 to sign up")
if respond == "1":
    login()
else:
    signup()