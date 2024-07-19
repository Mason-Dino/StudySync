import customtkinter
from tkinter import messagebox
import json


def settings(self):
    classes = []
    overallPadyOutside = 8
    overallPadyInside = 9

    self.content = customtkinter.CTkScrollableFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.content.grid_columnconfigure(0, weight=1)

    with open("setup.json", "r") as f:
        self.setupDir = json.load(f)

    self.appearanceFrame = customtkinter.CTkFrame(master=self.content, fg_color=["gray88", "gray19"])
    self.appearanceFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=overallPadyOutside)
    self.appearanceFrame.grid_columnconfigure((1), weight=1)

    self.appearance = customtkinter.CTkOptionMenu(master=self.appearanceFrame, values=["System", "Light", "Dark"], command=changeAppearanceMode, width=200)
    self.appearance.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.currentAppearance = customtkinter.CTkLabel(master=self.appearanceFrame, text="Appearance Mode: " + self.setupDir["mode"])
    self.currentAppearance.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    self.themeFrame = customtkinter.CTkFrame(master=self.content, fg_color=["gray88", "gray19"])
    self.themeFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=overallPadyInside)
    self.themeFrame.grid_columnconfigure((1), weight=1)

    self.theme = customtkinter.CTkOptionMenu(master=self.themeFrame, values=["Teal", "Orange", "Purple", "Red", "Yellow", "Green", "Blue", "Grey"], command=changeTheme, width=200, variable=customtkinter.StringVar(value=self.setupDir["theme"]))
    self.theme.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.currentTheme = customtkinter.CTkLabel(master=self.themeFrame, text="Current Theme: " + self.setupDir["theme"])
    self.currentTheme.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    self.classEditFrame = customtkinter.CTkFrame(master=self.content, fg_color=["gray88", "gray19"])
    self.classEditFrame.grid(row=2, column=0, sticky="nsew", padx=10, pady=overallPadyInside)
    self.classEditFrame.grid_columnconfigure((1), weight=1)

    for i in range(self.setupDir["numClasses"]):
        classes.append(self.setupDir[f"class{i+1}"]["name"])

    if classes == []:
        classes.append("No Classes Available")

    self.classEdit = customtkinter.CTkOptionMenu(master=self.classEditFrame, values=classes, command=lambda x: editClass(self, x), width=200)
    self.classEdit.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.newClassName = customtkinter.CTkEntry(master=self.classEditFrame, placeholder_text="New Class Name", textvariable=customtkinter.StringVar(value=classes[0]))
    self.newClassName.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    self.newClassType = customtkinter.CTkOptionMenu(master=self.classEditFrame, 
                                                    values=["Math", "Science", "English",  "History", "Social Studies", "World Language", "Fine Arts/Music", "Arts", "Physical Education", "Other"], 
                                                    width=200)
    self.newClassType.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    self.newInstructor = customtkinter.CTkEntry(master=self.classEditFrame, placeholder_text="Instructor Name", textvariable=customtkinter.StringVar(value="Instructor Name"))
    self.newInstructor.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

    if classes == ["No Classes Available"]:
        self.newInstructor.configure(textvariable=customtkinter.StringVar(value="No Classes Available"))
        self.newClassType.configure(variable=customtkinter.StringVar(value="No Classes Available"))

    else:
        self.newInstructor.configure(textvariable=customtkinter.StringVar(value=self.setupDir["class1"]["teacher"]))
        self.newClassType.configure(variable=customtkinter.StringVar(value=self.setupDir["class1"]["subject"]))

    self.classEditButtons = customtkinter.CTkFrame(master=self.classEditFrame, fg_color="transparent")
    self.classEditButtons.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.classEditButtons.grid_columnconfigure((0,1), weight=1)

    self.edit = customtkinter.CTkButton(master=self.classEditButtons, text="Edit Class", command=lambda: editClassSave(self, self.newClassName.get()))
    self.edit.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.delete = customtkinter.CTkButton(master=self.classEditButtons, text="Delete Class", command=lambda: deleteClass(self, self.classEdit.get()))
    self.delete.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    self.level = customtkinter.CTkFrame(master=self.content, fg_color=["gray88", "gray19"])
    self.level.grid(row=3, column=0, sticky="nsew", padx=10, pady=overallPadyOutside)
    self.level.grid_columnconfigure((0,1), weight=1)

    self.currentProgress = customtkinter.CTkLabel(master=self.level, text="Current Progress: " + str(round(round(self.setupDir["progress"], 3) * 100, 2)) + "%")
    self.currentProgress.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    
    self.currentLevel = customtkinter.CTkLabel(master=self.level, text="Current Level: " + str(self.setupDir["level"]))
    self.currentLevel.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

def changeAppearanceMode(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)

    with open("setup.json", "r") as f:
        setupDir = json.load(f)

    setupDir["mode"] = new_appearance_mode
    with open("setup.json", "w") as f:
        json.dump(setupDir, f, indent=4)


def changeTheme(new_theme: str):
    with open("setup.json", "r") as f:
        setupDir = json.load(f)

    setupDir["theme"] = new_theme
    with open("setup.json", "w") as f:
        json.dump(setupDir, f, indent=4)

    messagebox.showinfo("Success", "Theme Changed!\nRestart StudySync for changes to take effect.")

def editClass(self, new_class: str):
    with open("setup.json", "r") as f:
        setupDir = json.load(f)

    for i in range(setupDir["numClasses"]):
        if setupDir[f"class{i+1}"]["name"] == new_class:
            classNum = i + 1

    self.newClassName.configure(textvariable=customtkinter.StringVar(value=setupDir[f"class{classNum}"]["name"]))
    self.newInstructor.configure(textvariable=customtkinter.StringVar(value=setupDir[f"class{classNum}"]["teacher"]))
    self.newClassType.configure(variable=customtkinter.StringVar(value=setupDir[f"class{classNum}"]["subject"]))


def deleteClass(self, className: str):
    with open("setup.json", "r") as f:
        setupDir = json.load(f)

    for i in range(setupDir["numClasses"]):
        if setupDir[f"class{i+1}"]["name"] == className:
            deleteNum = i + 1
            del setupDir[f"class{i+1}"]

    for i in range(deleteNum, setupDir["numClasses"]):
        tempClass = setupDir[f"class{i+1}"]
        setupDir[f"class{i}"] = tempClass
        del setupDir[f"class{i+1}"]

    setupDir["numClasses"] -= 1
    with open("setup.json", "w") as f:
        json.dump(setupDir, f, indent=4)

    messagebox.showinfo("Success", "Class Deleted!")

def editClassSave(self, newClassName: str):
    print(newClassName)

    oldClassName = self.classEdit.get()

    with open("setup.json", "r") as f:
        setupDir = json.load(f)

    for i in range(setupDir["numClasses"]):
        if setupDir[f"class{i+1}"]["name"] == oldClassName:
            setupDir[f"class{i+1}"]["name"] = newClassName
            setupDir[f"class{i+1}"]["teacher"] = self.newInstructor.get()
            setupDir[f"class{i+1}"]["subject"] = self.newClassType.get()

    with open("setup.json", "w") as f:
        json.dump(setupDir, f, indent=4)

    messagebox.showinfo("Success", "Class Edited!")