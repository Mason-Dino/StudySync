import customtkinter
import json
from tkinter import messagebox
import datetime

from themes.theme import topLevel, top2Level, getRadioInfo
from id import makeID
from task import addMainTask



def assignments(self, taskName: str = None):
    self.exit = True
    
    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure((0), weight=1)
    self.content.grid_rowconfigure((0), weight=1)

    self.overallTaskFrame = customtkinter.CTkFrame(master=self.content, fg_color="transparent")
    self.overallTaskFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    self.overallTaskFrame.grid_columnconfigure((0), weight=1)
    self.overallTaskFrame.grid_rowconfigure((0, 1,2,3,4), weight=1)

    self.taskNameFrame = customtkinter.CTkFrame(master=self.overallTaskFrame, fg_color="transparent")
    self.taskNameFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=7)
    self.taskNameFrame.grid_columnconfigure((0), weight=1)

    self.taskNameEntry = customtkinter.CTkEntry(master=self.taskNameFrame)
    self.taskNameEntry.grid(row=1, column=0,  sticky="nsew", padx=10, pady=0)

    if taskName is not None:
        self.taskNameEntry.configure(textvariable=customtkinter.StringVar(value=taskName))

    self.taskNameEntry.configure(placeholder_text="Task Name (max: 30)")

    self.classFrame = customtkinter.CTkFrame(master=self.overallTaskFrame, fg_color="transparent")
    self.classFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=7)
    self.classFrame.grid_columnconfigure((0), weight=1)

    classes = ["None"]

    with open("setup.json", "r") as f:
        self.setupDir = json.load(f)

    numClasses = int(self.setupDir["numClasses"])
    theme = self.setupDir["theme"]

    for i in range(numClasses):
        classes.append(self.setupDir[f"class{i+1}"]["name"])

    self.classOption = customtkinter.CTkOptionMenu(master=self.classFrame, values=classes,
                                                    variable=customtkinter.StringVar(value="Pick Class"))
    self.classOption.grid(row=0, column=0, sticky="nsew", padx=10, pady=0)

    self.dateFrame = customtkinter.CTkFrame(master=self.overallTaskFrame, fg_color="transparent")
    self.dateFrame.grid(row=2, column=0, sticky="nsew", padx=10, pady=7)
    self.dateFrame.grid_columnconfigure((0,1,2), weight=1)

    self.day = customtkinter.CTkEntry(master=self.dateFrame, placeholder_text="Day")
    self.day.grid(row=0, column=0, sticky="nsew", padx=10, pady=0)

    self.month = customtkinter.CTkEntry(master=self.dateFrame, placeholder_text="Month")
    self.month.grid(row=0, column=1, sticky="nsew", padx=10, pady=0)

    self.year = customtkinter.CTkEntry(master=self.dateFrame, placeholder_text="Year", textvariable=customtkinter.StringVar(value=datetime.datetime.now().year))
    self.year.grid(row=0, column=2, sticky="nsew", padx=10, pady=0)

    self.miniContent = customtkinter.CTkFrame(master=self.overallTaskFrame, fg_color="transparent")
    self.miniContent.grid(row=3, column=0, sticky="nsew", padx=10, pady=7)
    self.miniContent.grid_columnconfigure((0,1), weight=1)

    self.sideLeft = customtkinter.CTkFrame(master=self.miniContent, fg_color=topLevel())
    self.sideLeft.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    self.sideLeft.grid_columnconfigure((0), weight=1)

    self.sideRight = customtkinter.CTkFrame(master=self.miniContent, fg_color=topLevel())
    self.sideRight.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    self.sideRight.grid_columnconfigure((0), weight=1)
    
    self.project = customtkinter.StringVar(value="project")

    radio = getRadioInfo(theme)

    """
    "CTkRadioButton": {
        "corner_radius": 1000,
        "border_width_checked": 6,
        "border_width_unchecked": 3,
        "fg_color": ["#17979E", "#10676B"],
        "border_color": ["#3E454A", "#949A9F"],
        "hover_color":["#0A7E85", "#064B4E"],
        "text_color": ["gray10", "#DCE4EE"],
        "text_color_disabled": ["gray60", "gray45"]
    },
    """

    self.testType = customtkinter.CTkRadioButton(master=self.sideRight, text="Test", variable=self.project, value="test",
                                                fg_color=radio["fg_color"], border_color=radio["border_color"], hover_color=radio["hover_color"], text_color=radio["text_color"], text_color_disabled=radio["text_color_disabled"],
                                                corner_radius=radio["corner_radius"], border_width_checked=radio["border_width_checked"], border_width_unchecked=radio["border_width_unchecked"])
    self.testType.grid(row=0, column=0, sticky="nsew", padx=10, pady=7)

    self.assignment = customtkinter.CTkRadioButton(master=self.sideRight, text="Assignment", variable=self.project, value="assignment",
                                                    fg_color=radio["fg_color"], border_color=radio["border_color"], hover_color=radio["hover_color"], text_color=radio["text_color"], text_color_disabled=radio["text_color_disabled"],
                                                    corner_radius=radio["corner_radius"], border_width_checked=radio["border_width_checked"], border_width_unchecked=radio["border_width_unchecked"])
    self.assignment.grid(row=2, column=0, sticky="nsew", padx=10, pady=7)

    self.groupType = customtkinter.CTkRadioButton(master=self.sideRight, text="Group", variable=self.project, value="group",
                                                fg_color=radio["fg_color"], border_color=radio["border_color"], hover_color=radio["hover_color"], text_color=radio["text_color"], text_color_disabled=radio["text_color_disabled"],
                                                corner_radius=radio["corner_radius"], border_width_checked=radio["border_width_checked"], border_width_unchecked=radio["border_width_unchecked"])
    self.groupType.grid(row=3, column=0, sticky="nsew", padx=10, pady=7)

    self.essayType = customtkinter.CTkRadioButton(master=self.sideRight, text="Essay", variable=self.project, value="essay",
                                                fg_color=radio["fg_color"], border_color=radio["border_color"], hover_color=radio["hover_color"], text_color=radio["text_color"], text_color_disabled=radio["text_color_disabled"],
                                                corner_radius=radio["corner_radius"], border_width_checked=radio["border_width_checked"], border_width_unchecked=radio["border_width_unchecked"])
    self.essayType.grid(row=4, column=0, sticky="nsew", padx=10, pady=7)

    self.submission = customtkinter.CTkEntry(master=self.sideLeft, placeholder_text="Submission Link")
    self.submission.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.pts = customtkinter.CTkEntry(master=self.sideLeft, placeholder_text="Point Value")
    self.pts.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    self.importance = customtkinter.CTkOptionMenu(master=self.sideLeft, values=["1 (most)", "2", "3", "4 (least)"], variable=customtkinter.StringVar(value="Importance Level"))
    self.importance.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

    self.addTask = customtkinter.CTkButton(master=self.overallTaskFrame, text="Add Task", command=lambda: makeTask(self), height=20)
    self.addTask.grid(row=4, column=0, sticky="nsew", padx=10, pady=10)

def makeTask(self):
    #def addMainTask(taskName, taskID, className, classID, day, month, year):
    name = self.taskNameEntry.get()
    id = makeID(20)
    classOption = self.classOption.get()
    classID = "0000000000"

    with open("setup.json", "r") as f:
        setupDir = json.load(f)

    for i in range(setupDir["numClasses"]):
        if setupDir[f"class{i+1}"]["name"] == classOption:
            classID = setupDir[f"class{i+1}"]["id"]

    day = self.day.get()
    month = self.month.get()
    year = self.year.get()

    subLink = self.submission.get()
    ptsValue = self.pts.get()
    importance = self.importance.get()
    type = self.project.get()

    error = False

    if importance == "1 (most)" or importance == "4 (least)":
        importance = int(importance.split(" ")[0])

    if len(name) > 30:
        messagebox.showerror(title="Error", message="Task name too long")
        error = True

    elif day == "" or month == "" or year == "" or name == "" or classOption == "Pick Class":
        messagebox.showerror(title="Error", message="Missing required field")
        error = True

    elif "-" in name:
        messagebox.showerror(title="Error", message="""you cannot have an "-" in your task/assignment name""")
        error = True

    elif day.isdigit() == False or month.isdigit() == False or year.isdigit() == False:
        messagebox.showerror(title="Error", message="Invalid date")
        error = True

    try:
        datetime.datetime(int(year), int(month), int(day))

    except:
        messagebox.showerror(title="Error", message="Invalid date")
        error = True

    if ptsValue.isdigit() == False and ptsValue != "":
        messagebox.showerror(title="Error", message="Invalid point value")
        error = True

    if importance == "Importance Level":
        importance = 5

    if type == "project":
        type = "None"

    if subLink == "":
        subLink = "None"

    if error == False:
        importance = int(importance)

        addMainTask(name, id, classOption, classID, day, month, year, subLink, ptsValue, importance, type.capitalize())

        self.taskNameEntry.delete(0, "end")
        self.taskNameEntry.configure(placeholder_text="Task Name (max: 30)")
        self.classOption.set("Pick Class")
        self.day.delete(0, "end")
        self.day.configure(placeholder_text="Day")
        self.month.delete(0, "end")
        self.month.configure(placeholder_text="Month")
        self.year.delete(0, "end")
        self.year.configure(textvariable=customtkinter.StringVar(value=datetime.datetime.now().year))
        self.submission.delete(0, "end")
        self.submission.configure(placeholder_text="Submission Link")
        self.pts.delete(0, "end")
        self.pts.configure(placeholder_text="Point Value")
        self.importance.set("Importance Level")
        self.project.set("project")

        messagebox.showinfo(title="Success", message="Task added!")