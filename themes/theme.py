import json
import os
import re

def loadColor(color):
    if "#" in color:
        return color
    
    else:
        current = os.getcwd()
        with open(f"{current}/themes/{color.lower()}.json", "r") as f:
            color = json.load(f)

        return color["CTkButton"]["fg_color"]

def isValidColorCode(code):
    pattern = r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
    match = re.match(pattern, code)
    return bool(match)

def topLevel():
    return ["gray88", "gray19"]

def top2Level():
    return ["gray90", "gray21"]

if __name__ == "__main__":
    loadColor("purple")