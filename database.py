import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("/home/karabo/Desktop/workspace/SkillSync/service_account_key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://skillsync-706d4-default-rtdb.firebaseio.com/'})


def save(uid,name,email,password,role):
    ref = db.reference('users')

    ref.set({
        uid: {
            'name': name,
            'email': email,
            'password': password,
            'role': role
        }
    })