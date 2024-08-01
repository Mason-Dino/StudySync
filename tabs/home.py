from task import *
from tkinter import messagebox
from id import makeID
import customtkinter
import datetime
import sqlite3
import json

import random

from screen.assignment import showAssignment
from tabs.assignments import assignments
from themes.theme import topLevel

def home(self):
    self.taskFrame = {}

    self.content = customtkinter.CTkFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.content.grid_columnconfigure((0,1,2), weight=1)
    self.content.grid_rowconfigure((5), weight=1)

    with open("setup.json", "r") as f:
        self.setupDir = json.load(f)

    self.classNum = self.setupDir["numClasses"]
    self.progress = self.setupDir["progress"]

    classNameValues = ["None"]

    self.progressbar = customtkinter.CTkProgressBar(master=self.content)
    self.progressbar.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)
    self.progressbar.set(self.progress)

    self.taskName = customtkinter.CTkEntry(master=self.content, placeholder_text="Task Name (max: 30)")
    self.taskName.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.addTask = customtkinter.CTkButton(master=self.content, text="Add Task", command=lambda: makeTask(self))
    self.addTask.grid(row=2, column=2, sticky="nsew", padx=10, pady=10)

    """
    for i in range(self.classNum):
        classNameValues.append(self.setupDir[f"class{i+1}"]["name"])

    self.className = customtkinter.CTkOptionMenu(master=self.content, values=classNameValues, variable=customtkinter.StringVar(value="Pick Class"))
    self.className.grid(row=2, column=2, sticky="nsew", padx=10, pady=10)

    self.day = customtkinter.CTkEntry(master=self.content, placeholder_text="Day")
    self.day.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

    self.month = customtkinter.CTkEntry(master=self.content, placeholder_text="Month")
    self.month.grid(row=3, column=1, sticky="nsew", padx=10, pady=10)

    self.year = customtkinter.CTkEntry(master=self.content, placeholder_text="Year", textvariable=customtkinter.StringVar(value=datetime.datetime.now().year))
    self.year.grid(row=3, column=2, sticky="nsew", padx=10, pady=10)


    self.button = customtkinter.CTkButton(master=self.content, text="Add Task", command=lambda: makeTask(self))
    self.button.grid(row=4, column=1, sticky="nsew", padx=10, pady=10)

    """

    self.task = customtkinter.CTkScrollableFrame(master=self.content, corner_radius=6, fg_color="transparent")
    self.task.grid(row=5, column=0, columnspan=3, sticky="nsew", padx=3)
    self.task.grid_columnconfigure(0, weight=1)

    task = getMainTasks("ORDER BY date ASC")

    if task == []:
        self.task.grid_rowconfigure(0, weight=1)

        self.error = customtkinter.CTkLabel(master=self.task, text="No tasks found", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.error.grid(row=0, column=0, sticky="nsew")

    else:
        for i in range(len(task)):
            self.taskFrame[i] = {}
            self.taskFrame[i]["id"] = task[i][0]

            self.taskFrame[i]["frame"] = customtkinter.CTkFrame(master=self.task, fg_color=topLevel())
            self.taskFrame[i]["frame"].grid(row=i, column=0, sticky="nsew", padx=3, pady=2)

            self.taskFrame[i]["info"] = customtkinter.CTkLabel(master=self.taskFrame[i]["frame"], text=task[i][1], font=customtkinter.CTkFont(size=20, weight="bold"), anchor="w", justify="left", width=400)
            #self.info.place(relx=.01, rely=.1, anchor="nw")
            self.taskFrame[i]["info"].grid(row=0, column=0, padx=5)

            date = datetime.datetime(int(task[i][4]), int(task[i][3]), int(task[i][2]))
            now = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
            if date < now:
                self.taskFrame[i]["info"].configure(text_color="red")


            self.taskFrame[i]["due"] = customtkinter.CTkLabel(master=self.taskFrame[i]["frame"], text=f"Due: {task[i][3]}/{task[i][2]}/{task[i][4]}", anchor="w", justify="left", width=400)
            self.taskFrame[i]["due"].grid(row=1, column=0, padx=5)

            self.taskFrame[i]["done"] = customtkinter.CTkButton(master=self.taskFrame[i]["frame"], text="Done", width=50, command=lambda: finishTask(self, i))
            #self.done.grid(row=0, rowspan=2, column=1, padx=3, sticky="e")
            self.taskFrame[i]["done"].place(relx=.99, rely=0.25, anchor="ne")

        for i in range(len(task)):
            makeButtonWork(self, i)

    self.bind("<Return>", lambda event: makeTask(self))

def makeButtonWork(self, i):
    self.taskFrame[i]["done"].configure(command=lambda: finishTask(self, self.taskFrame[i]["frame"], self.taskFrame[i]["id"]))
    self.taskFrame[i]["frame"].bind("<Button-1>", lambda event: showMainTask(self, event, self.taskFrame[i]["id"]))
    self.taskFrame[i]["info"].bind("<Button-1>", lambda event: showMainTask(self, event, self.taskFrame[i]["id"]))
    self.taskFrame[i]["due"].bind("<Button-1>", lambda event: showMainTask(self, event, self.taskFrame[i]["id"]))

def makeTask(self):
    assignments(self, self.taskName.get())

def finishTask(self, frame, id):
    frame.destroy()

    finishMainTask(self, id)

    task = getMainTasks()
    if task == []:
        self.task.grid_rowconfigure(0, weight=1)

        self.error = customtkinter.CTkLabel(master=self.task, text="No tasks found", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.error.grid(row=0, column=0, sticky="nsew")

def showMainTask(self, event, id):
    showAssignment(self, id)
