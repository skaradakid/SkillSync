import datetime


def find_users_document(user, db):
    id = user['localId']
    user_data = db.child("users").child(id).get()

# Check if the user exists
    if user_data.val():
        role = user_data.val()['role']
        print(role)
        mentor_schedular(user, db)
    else:
        print("User not found.")
        
def mentor_schedular(user,db):
    date = input("input a date to schedule a mentor> ")
    start_time = input("input the start time > ")
    end_time = input("input the end time > ")
    
    start_datetime = generate_datetime(start_time, date)
    end_datetime = generate_datetime(end_time, date)
    
def generate_datetime(time_str: str, date_str: str) -> datetime:
    
    try:
        # Combine the date and time into a single string
        datetime_str = f"{date_str} {time_str}"
        
        # Parse the combined string into a datetime object
        result = datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")
        return result
    except ValueError as e:
        raise ValueError(f"Invalid date or time format: {e}")
    
    


    