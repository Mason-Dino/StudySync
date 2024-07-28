from tkinter import messagebox
import customtkinter
import json

from themes.theme import topLevel
from icon import getIcons
from tabs.home import home
from id import makeID

def classAddEdit(self, type: str, name: str = None):
    self.type = type

    self.content = customtkinter.CTkFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure((0,1), weight=1)

    self.title = customtkinter.CTkLabel(master=self.content, text=f"Class {type.capitalize()}",
                                        font=customtkinter.CTkFont(size=20, weight="bold"))
    self.title.grid(row=0, column=0, columnspan=2, pady=10)

    with open("setup.json", "r") as f:
        setupDir = json.load(f)
    
    self.classFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.classFrame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.classFrame.grid_columnconfigure((0), weight=1)

    self.className = customtkinter.CTkEntry(master=self.classFrame)
    self.className.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    self.cosmetics = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.cosmetics.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.cosmetics.grid_columnconfigure((0,1), weight=1)

    self.subject = customtkinter.CTkOptionMenu(master=self.cosmetics, values=["Math", "Science", "English",  "History", "Social Studies", "World Language", "Fine Arts/Music", "Arts", "Physical Education", "Other"],
                                                variable=customtkinter.StringVar(value="Subject"))
    self.subject.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.icon = customtkinter.CTkOptionMenu(master=self.cosmetics, values=getIcons(), variable=customtkinter.StringVar(value="Icon"))
    self.icon.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    self.color = customtkinter.CTkOptionMenu(master=self.cosmetics, values=["Teal", "Orange", "Purple", "Red", "Yellow", "Green", "Blue", "Other"],
                                                variable=customtkinter.StringVar(value="Color"))
    self.color.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.teacherFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.teacherFrame.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.teacherFrame.grid_columnconfigure((0,1), weight=1)

    self.teacher = customtkinter.CTkEntry(master=self.teacherFrame)
    self.teacher.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.email = customtkinter.CTkEntry(master=self.teacherFrame)
    self.email.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    self.breakFrame = customtkinter.CTkFrame(master=self.content, fg_color="transparent", height=10)
    self.breakFrame.grid(row=4, column=0, columnspan=2, sticky="nsew")

    self.updateAdd = customtkinter.CTkButton(master=self.content, text="Update")
    self.updateAdd.grid(row=5, column=0, sticky="nsew", padx=10, pady=10)

    self.cancel = customtkinter.CTkButton(master=self.content, text="Cancel", command=lambda:cancel(self))
    self.cancel.grid(row=5, column=1, sticky="nsew", padx=10, pady=10)

    if type == "add":
        numClass = setupDir["numClasses"]

        self.updateAdd.configure(command=lambda: updateAdd(self, "Added"), text="Add")

        self.className.configure(placeholder_text="Class Name")
        self.teacher.configure(placeholder_text="Teacher")
        self.email.configure(placeholder_text="Email")

    elif type == "edit":
        for i in range(setupDir["numClasses"]):
            if setupDir[f"class{i+1}"]["name"] == name:
                classNum = i + 1

        name = setupDir[f"class{classNum}"]["name"]
        subject = setupDir[f"class{classNum}"]["subject"]
        icon = setupDir[f"class{classNum}"]["icon"]
        color = setupDir[f"class{classNum}"]["color"]
        teacher = setupDir[f"class{classNum}"]["teacher"]
        email = setupDir[f"class{classNum}"]["email"]

        if name == "":
            self.className.configure(placeholder_text="Class Name")

        else:
            self.className.configure(textvariable=customtkinter.StringVar(value=name))

        if teacher == "":
            self.teacher.configure(placeholder_text="Who is the teacher/instructor?")

        else:
            self.teacher.configure(textvariable=customtkinter.StringVar(value=teacher))

        if email == "":
            self.email.configure(placeholder_text="What is their email?")

        else:
            self.email.configure(textvariable=customtkinter.StringVar(value=email))
        
        self.subject.configure(variable=customtkinter.StringVar(value=subject))
        self.icon.configure(variable=customtkinter.StringVar(value=icon))
        self.color.configure(variable=customtkinter.StringVar(value=color.capitalize()))


        self.updateAdd.configure(command=lambda: updateAdd(self, "Edited", classNum=classNum))

def updateAdd(self, type: str, classNum: int = None):
    with open("setup.json", "r") as f:
        setupDir = json.load(f)

    if type == "Edited":
        name = self.className.get()
        subject = self.subject.get()
        icon = self.icon.get()
        color = self.color.get().lower()
        teacher = self.teacher.get()
        email = self.email.get()

        setupDir[f"class{classNum}"]["name"] = name
        setupDir[f"class{classNum}"]["subject"] = subject
        setupDir[f"class{classNum}"]["icon"] = icon
        setupDir[f"class{classNum}"]["color"] = color
        setupDir[f"class{classNum}"]["teacher"] = teacher
        setupDir[f"class{classNum}"]["email"] = email

        with open("setup.json", "w") as f:
            json.dump(setupDir, f, indent=4)

    if type == "Added":
        numClass = setupDir["numClasses"]
        setupDir["numClasses"] = numClass + 1
        numClass = numClass + 1

        name = self.className.get()
        subject = self.subject.get()
        icon = self.icon.get()
        color = self.color.get()
        teacher = self.teacher.get()
        email = self.email.get()

        if subject == "Subject":
            subject = "Other"

        if icon == "Icon":
            icon = "Other"

        if color == "Color":
            color = "blue"

        setupDir[f"class{numClass}"] = {
            "id": makeID(),
            "name": name,
            "subject": subject,
            "icon": icon,
            "color": color,
            "teacher": teacher,
            "email": email
        }

        with open("setup.json", "w") as f:
            json.dump(setupDir, f, indent=4)

    messagebox.showinfo(title="Success", message=f"Class {type.capitalize()}!")
    home(self)

def cancel(self):
    home(self)