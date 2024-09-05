import json

def checkIfGoogleCal():
    with open("setup.json", "r") as f:
        setup = json.load(f)

    if setup["googleCal"] == True:
        return True
    else:
        return False