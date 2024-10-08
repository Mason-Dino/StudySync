import customtkinter
import json

from screen.classroom import classroom
from icon import loadIcon

def isodd(value: int):
    return ((value % 2) == 1)


def classes(self):
    self.exit = True
    
    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.content.grid_columnconfigure(0, weight=1)
    self.content.grid_rowconfigure(0, weight=1)

    self.classFrame = customtkinter.CTkFrame(master=self.content, fg_color="transparent")
    self.classFrame.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

    self.classFrame.grid_columnconfigure((0,1), weight=1)

    with open("setup.json", "r") as f:
        self.setupDir = json.load(f)

    numClasses = int(self.setupDir["numClasses"])
    odd = isodd(numClasses)

    classButton = {}
    width = 200

    if odd == True:
        c = 0
        row = 0

        while (c < numClasses):
            c += 1

            classButton[c] = {}

            classButton[c]["id"] = self.setupDir[f"class{c}"]["id"]

            if c == numClasses:
                classButton[c]["button"] = customtkinter.CTkButton(master=self.classFrame, text=self.setupDir[f"class{c}"]["name"], width=width, image=loadIcon(self.setupDir[f"class{c}"]["icon"]))
                classButton[c]["button"].grid(row=row, column=0, columnspan=2, pady=10)

            elif c % 2 == 0:
                classButton[c]["button"] = customtkinter.CTkButton(master=self.classFrame, text=self.setupDir[f"class{c}"]["name"], width=width, image=loadIcon(self.setupDir[f"class{c}"]["icon"]))
                classButton[c]["button"].grid(row=row, column=1, pady=15)
                row += 1

            else:
                classButton[c]["button"] = customtkinter.CTkButton(master=self.classFrame, text=self.setupDir[f"class{c}"]["name"], width=width, image=loadIcon(self.setupDir[f"class{c}"]["icon"]))
                classButton[c]["button"].grid(row=row, column=0, pady=15)

    elif odd == False:
        c = 0
        row = 0

        while (c < numClasses):
            c += 1

            classButton[c] = {}

            classButton[c]["id"] = self.setupDir[f"class{c}"]["id"]

            if c == 1:
                classButton[c]["button"] = customtkinter.CTkButton(master=self.classFrame, text=self.setupDir[f"class{c}"]["name"], width=width, image=loadIcon(self.setupDir[f"class{c}"]["icon"]))
                classButton[c]["button"].grid(row=row, column=0, pady=15)

            elif c % 2 == 0: 
                classButton[c]["button"] = customtkinter.CTkButton(master=self.classFrame, text=self.setupDir[f"class{c}"]["name"], width=width, image=loadIcon(self.setupDir[f"class{c}"]["icon"]))
                classButton[c]["button"].grid(row=row, column=1, pady=15)
                row += 1

            else:
                classButton[c]["button"] = customtkinter.CTkButton(master=self.classFrame, text=self.setupDir[f"class{c}"]["name"], width=width, image=loadIcon(self.setupDir[f"class{c}"]["icon"]))
                classButton[c]["button"].grid(row=row, column=0, pady=15)

    for i in range(numClasses):
        configScreen(self, i, classButton)

def configScreen(self, c, classButton):
    classButton[c+1]["button"].configure(command=lambda: classScreen(self, classButton[c+1]["button"]._text, classButton[c+1]["id"]))

def classScreen(self, button, id):
    classroom(self, id, button)