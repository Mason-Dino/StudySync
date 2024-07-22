import os

def getIcons():
    icons = os.listdir("./icons")
    
    for i in range(len(icons)):
        icons[i] = icons[i].replace(".png", "")

    for i in range(len(icons)):
        icons[i] = icons[i].replace("_", " ")

    icons.remove("settings")
    icons.remove("Other")

    icons.append("Other")

    return icons

if __name__ == "__main__":
    print(getIcons())