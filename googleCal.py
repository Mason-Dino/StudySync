import json

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