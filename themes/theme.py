import json
import os

def loadColor(color):
    current = os.getcwd()
    with open(f"{current}/themes/{color.lower()}.json", "r") as f:
        color = json.load(f)

    print(color["CTkButton"]["fg_color"])

if __name__ == "__main__":
    loadColor("purple")