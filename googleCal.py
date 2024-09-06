import json
import os
from dotenv import load_dotenv

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']

def checkIfGoogleCal():
    with open("setup.json", "r") as f:
        setup = json.load(f)

    
    try:
        if setup["googleCal"] == True:
            return True
        else:
            return False
        
    except:
        setup["googleCal"] = False
        with open("setup.json", "w") as f:
            json.dump(setup, f, indent=4)

        return False
    
def loadGooglCal():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "/Users/norbe/OneDrive/Desktop/StudySync/creds.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)

    return service
    
def makeNewAssignment(name, dueDate):
    load_dotenv()

    DIS_Math = os.environ.get("DIS_Math")

    service = loadGooglCal()

    event = {
        'summary': name,
        'start': {
            'date': dueDate,
            'timeZone': 'America/Chicago',
        },
        'end': {
            'date': dueDate,
            'timeZone': 'America/Chicago',
        }
    }

    event = service.events().insert(calendarId=DIS_Math, body=event).execute()

    
def newEventTest():
    event = {
        'summary': 'Homework',
        'start': {
            'date': f'2024-9-6',
            'timeZone': 'America/Chicago',
        },
        'end': {
            'date': f'2024-9-6',
            'timeZone': 'America/Chicago',
        }
    }

    """
    event = {
        'summary': 'Homework',
        'start': {
            'datetime': f'2024-9-6T06:00:00',
            'timeZone': 'America/Chicago',
        },
        'end': {
            'datetime': f'2024-9-617:00:00',
            'timeZone': 'America/Chicago',
        }
    }

    """



makeNewAssignment("Test: 15A", "2024-9-6")