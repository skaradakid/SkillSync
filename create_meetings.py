import os.path
import datetime as dt

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
    creds= None

    if os.path.exists('token.json'):
        creds=Credentials.from_authorized_user_file('token.json')

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json',SCOPES)
            creds= flow.run_local_server(port=0)

        with open('token.json','w') as token:
            token.write(creds.to_json())

    try:
        service=build('calendar','v3',credentials=creds)


        event= {
            'summary': "test_my_event",
            'location':'Online',
            'description':'more details about test event',
            'colorId': 6,
            'start':{
                'dateTime':'2025-02-01T14:00:00',
                'timeZone':'Africa/Johannesburg'
            },
            'end':{
                'dateTime':'2025-02-01T15:00:00',
                'timeZone':'Africa/Johannesburg',
            },
            'reccurrence':[
                "RULE:FREQ=DAILY;count=1"

            ],
            'attendees':[
                {'email':'hashaikjhb024@student.wethinkcode.co.za'},
                {'email':'hrehhferjjnjjsd@gmail.com'},
                {'email':'nhdsinsudihufnvnfirdnr@gmail.com'}
            ]
        }

        event= service.events().insert(calendarId='primary',body=event).execute()
        print(f"Event created {event.get('htmlLink')}")

    except HttpError as error:
        print("an error has occurred",  error)



if __name__== "__main__":
    main()