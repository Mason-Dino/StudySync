import json
import os

def loadColor(color):
    current = os.getcwd()
    with open(f"{current}/themes/{color.lower()}.json", "r") as f:
        color = json.load(f)

    return color["CTkButton"]["fg_color"]

def topLevel():
    return ["gray88", "gray19"]

if __name__ == "__main__":
    loadColor("purple")