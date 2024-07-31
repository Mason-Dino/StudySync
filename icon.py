import customtkinter
from PIL import Image
import os

def getIcons():
    icons = os.listdir("./icons")
    
    for i in range(len(icons)):
        icons[i] = icons[i].replace(".png", "")

    for i in range(len(icons)):
        icons[i] = icons[i].replace("_", " ")

    icons.remove("settings")
    icons.remove("Other")
    icons.remove("flag")

    icons.append("Other")

    return icons

def loadIcon(icon):
    icon = icon.replace(" ", "_")
    return customtkinter.CTkImage(light_image=Image.open(f"./icons/{icon}.png"), dark_image=Image.open(f"./icons/{icon}.png"), size=(20, 20))

if __name__ == "__main__":
    print(getIcons())