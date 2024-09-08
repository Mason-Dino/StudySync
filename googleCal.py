import json
import os
from dotenv import load_dotenv

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from tkinter import messagebox

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
                f"{os.getcwd()}/creds.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)

    return service
    
def makeNewAssignment(name, year, month, day, classID):
    with open("setup.json", "r") as f:
        setup = json.load(f)

    calID = setup["calendar"][classID]

    service = loadGooglCal()

    event = {
        'summary': name,
        'start': {
            'date': f'{year}-{month}-{day}',
            'timeZone': 'America/Chicago',
        },
        'end': {
            'date': f'{year}-{month}-{day}',
            'timeZone': 'America/Chicago',
        },
        "description": "Import from StudySync"
    }

    event = service.events().insert(calendarId=calID, body=event).execute()

    return event

def deleteEvent(eventID, classID):
    service = loadGooglCal()

    with open("setup.json", "r") as f:
        setup = json.load(f)

    calID = setup["calendar"][classID]

    service.events().delete(calendarId=calID, eventId=eventID).execute()

def editEvent(eventID, classID, summary, year, month, day):
    service = loadGooglCal()

    with open("setup.json", "r") as f:
        setup = json.load(f)

    calID = setup["calendar"][classID]

    event = service.events().get(calendarId=calID, eventId=eventID).execute()

    event["summary"] = summary
    event["start"]["date"] = f"{year}-{month}-{day}"
    event["end"]["date"] = f"{year}-{month}-{day}"

    service.events().update(calendarId=calID, eventId=eventID, body=event).execute()

    
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

def testEvent(calID):
    service = loadGooglCal()

    event = {
        'summary': 'Test Event',
        'start': {
            'date': f'2006-2-1',
            'timeZone': 'America/Chicago',
        },
        'end': {
            'date': f'2006-2-1',
            'timeZone': 'America/Chicago',
        }
    }

    error = False

    try:
        event = service.events().insert(calendarId=calID, body=event).execute()
        print(event["id"])
        event = service.events().delete(calendarId=calID, eventId=event["id"]).execute()
    except:
        error = True

    print(event)

    return error

