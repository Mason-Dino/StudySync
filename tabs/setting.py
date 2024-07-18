import customtkinter
import json


def settings(self):
    classes = []

    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.content.grid_columnconfigure(0, weight=1)

    with open("setup.json", "r") as f:
        self.setupDir = json.load(f)

    self.appearanceFrame = customtkinter.CTkFrame(master=self.content)
    self.appearanceFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    self.appearanceFrame.grid_columnconfigure((1), weight=1)

    self.appearance = customtkinter.CTkOptionMenu(master=self.appearanceFrame, values=["System", "Light", "Dark"], command=changeAppearanceMode)
    self.appearance.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.currentAppearance = customtkinter.CTkLabel(master=self.appearanceFrame, text="Current Appearance Mode: " + self.setupDir["mode"])
    self.currentAppearance.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    self.classEditFrame = customtkinter.CTkFrame(master=self.content)
    self.classEditFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    self.classEditFrame.grid_columnconfigure((1), weight=1)

    for i in range(self.setupDir["numClasses"]):
        classes.append(self.setupDir[f"class{i+1}"]["name"])

    self.classEdit = customtkinter.CTkOptionMenu(master=self.classEditFrame, values=classes, command=editClass)
    self.classEdit.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.dueFrame = customtkinter.CTkFrame(master=self.content)
    self.dueFrame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
    self.dueFrame.grid_columnconfigure((1), weight=1)


def changeAppearanceMode(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)

    with open("setup.json", "r") as f:
        setupDir = json.load(f)

    setupDir["mode"] = new_appearance_mode
    with open("setup.json", "w") as f:
        json.dump(setupDir, f, indent=4)

def editClass(new_class: str):
    with open("setup.json", "r") as f:
        setupDir = json.load(f)