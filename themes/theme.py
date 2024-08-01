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
    return ["gray90", "gray19"]

def top2Level():
    return ["gray92", "gray21"]

def loadLevelColor(level: int):
    if level == 1:
        return "#CE353C"
    
    if level == 2:
        return "#E96A26"
    
    if level == 3:
        return "#EBB82D"
    
    if level == 4:
        return "#2FBB25"
    
    if level == 5:
        with open("setup.json", "r") as f:
            setupDir = json.load(f)

        color = setupDir["theme"]

        return loadColor(color)
    

if __name__ == "__main__":
    loadColor("purple")