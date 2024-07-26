from task import *
from tkinter import messagebox
from id import makeID
import customtkinter
import datetime
import sqlite3
import json

import random

from screen.assignment import showAssignment

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

            self.taskFrame[i]["frame"] = customtkinter.CTkFrame(master=self.task, fg_color=["gray88", "gray19"])
            self.taskFrame[i]["frame"].grid(row=i, column=0, sticky="nsew", padx=3, pady=2)

            self.taskFrame[i]["info"] = customtkinter.CTkLabel(master=self.taskFrame[i]["frame"], text=task[i][1], font=customtkinter.CTkFont(size=20, weight="bold"), anchor="w", justify="left", width=400)
            #self.info.place(relx=.01, rely=.1, anchor="nw")
            self.taskFrame[i]["info"].grid(row=0, column=0, padx=5)

            date = datetime.datetime(int(task[i][4]), int(task[i][3]), int(task[i][2]))
            if date.day < datetime.datetime.now().day and date.month <= datetime.datetime.now().month and date.year <= datetime.datetime.now().year:
                self.taskFrame[i]["info"].configure(text_color="red")


            self.taskFrame[i]["due"] = customtkinter.CTkLabel(master=self.taskFrame[i]["frame"], text=f"Due: {task[i][3]}/{task[i][2]}/{task[i][4]}", anchor="w", justify="left", width=400)
            self.taskFrame[i]["due"].grid(row=1, column=0, padx=5)

            self.taskFrame[i]["done"] = customtkinter.CTkButton(master=self.taskFrame[i]["frame"], text="Done", width=50, command=lambda: finishTask(self, i))
            #self.done.grid(row=0, rowspan=2, column=1, padx=3, sticky="e")
            self.taskFrame[i]["done"].place(relx=.99, rely=0.25, anchor="ne")

        for i in range(len(task)):
            makeButtonWork(self, i)

    #self.bind("<Button-1>", makeTask)

def makeButtonWork(self, i):
    self.taskFrame[i]["done"].configure(command=lambda: finishTask(self, self.taskFrame[i]["frame"], self.taskFrame[i]["id"]))
    self.taskFrame[i]["frame"].bind("<Button-1>", lambda event: showMainTask(self, event, self.taskFrame[i]["id"]))
    self.taskFrame[i]["info"].bind("<Button-1>", lambda event: showMainTask(self, event, self.taskFrame[i]["id"]))
    self.taskFrame[i]["due"].bind("<Button-1>", lambda event: showMainTask(self, event, self.taskFrame[i]["id"]))

def makeTask(self):
    taskName = self.taskName.get()
    className = self.className.get()
    day = self.day.get()
    month = self.month.get()
    year = self.year.get()

    if len(taskName) > 30:
        messagebox.showerror(title="Error", message="Task name too long")

    elif len(taskName) == 0 or className == "Pick Class" or day == "" or month == "" or year == "":
        messagebox.showerror(title="Error", message="You are missing a required field")

    elif day.isdigit() == False or month.isdigit() == False or year.isdigit() == False or (int(month) > 12 or int(month) < 1) or (int(month) == 2 and isLeapYear(int(year)) == False and int(day) == 29):
        messagebox.showerror(title="Error", message="Invalid date")

    else:
        month30 = [4, 6, 9, 11]
        month31 = [1, 3, 5, 7, 8, 10, 12] 

        if int(month) in month30 and int(day) > 30:
            messagebox.showerror(title="Error", message="Invalid date")

        elif int(month) in month31 and int(day) > 31:
            messagebox.showerror(title="Error", message="Invalid date")

        else:
            with open("setup.json", "r") as f:
                self.setupDir = json.load(f)

            self.classNum = self.setupDir["numClasses"]
            id = ""

            for i in range(self.classNum):
                if self.setupDir[f"class{i+1}"]["name"] == className:
                    id = self.setupDir[f"class{i+1}"]["id"]

            if id == "":
                id = "0000000000"

            taskID = makeID(20)
            addMainTask(taskName, taskID, className, id, day, month, year)

            self.taskName.delete(0, "end")
            self.className.set("Pick Class")
            self.day.delete(0, "end")
            self.month.delete(0, "end")
            self.year.delete(0, "end")

            home(self)

def finishTask(self, frame, id):
    frame.destroy()

    finishMainTask(self, id)

    task = getMainTasks()
    if task == []:
        self.task.grid_rowconfigure(0, weight=1)

        self.error = customtkinter.CTkLabel(master=self.task, text="No tasks found", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.error.grid(row=0, column=0, sticky="nsew")

def showMainTask(self, event, id):
    print("showing main task")
    print(event)
    print(id)
    showAssignment(self, id)
