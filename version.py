import requests
import json

def getMainVersion():
    test = requests.get("https://mason-dino.github.io/StudySync/")
    decode = test.content.decode("utf-8")
    res = json.loads(decode)

    return res["mainVersion"]

def getLittleVersion():
    test = requests.get("https://mason-dino.github.io/StudySync/")
    decode = test.content.decode("utf-8")
    res = json.loads(decode)

    return res["version"]

def getUserVersion():
    with open("setup.json", "r") as f:
        setupDir = json.load(f)

    return setupDir["version"]

def checkIfBeta():
    test = requests.get("https://mason-dino.github.io/StudySync/")
    decode = test.content.decode("utf-8")
    res = json.loads(decode)

    return res["active beta"]

def getJson():
    test = requests.get("https://mason-dino.github.io/StudySync/")
    decode = test.content.decode("utf-8")
    res = json.loads(decode)

    return res

if __name__ == "__main__":
    print(getJson())

