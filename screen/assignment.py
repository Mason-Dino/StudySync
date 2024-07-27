from tkinter import messagebox
import customtkinter
from task import *
import datetime

from themes.theme import topLevel
from id import makeID


def showAssignment(self, id):
    self.content = customtkinter.CTkFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure((0, 1), weight=1)
    self.content.grid_rowconfigure((1), weight=1)

    taskInfo = getMainTaskSingle(id)
    subTask = getSubTasks(id)

    classID = taskInfo[0][8]
    self.numSubTask = len(subTask)
    self.subTaskInfo = {}

    self.header = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.header.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)
    self.header.grid_columnconfigure((0), weight=1)

    self.mainHeader = customtkinter.CTkFrame(master=self.header, fg_color="transparent", corner_radius=6)
    self.mainHeader.grid(row=0, column=0, sticky="nsew")

    self.subHeader = customtkinter.CTkFrame(master=self.header, fg_color="transparent", corner_radius=6)
    self.subHeader.grid(row=1, column=0, sticky="nsew")

    self.subTaskFrame = customtkinter.CTkScrollableFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.subTaskFrame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)
    self.subTaskFrame.grid_columnconfigure((0), weight=1)

    self.buttonFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.buttonFrame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)
    self.buttonFrame.grid_columnconfigure((0, 1, 2), weight=1)

    self.assignment = customtkinter.CTkLabel(master=self.mainHeader, text=f"{taskInfo[0][1]}", font=customtkinter.CTkFont(size=20, weight="bold"), anchor="w", justify="left",
                                                corner_radius=6)
    self.assignment.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.assignment.grid_info()

    self.due = customtkinter.CTkLabel(master=self.subHeader, text=f"Due: {taskInfo[0][3]}/{taskInfo[0][2]}/{taskInfo[0][4]}", font=customtkinter.CTkFont(size=15), 
                                        anchor="w", justify="left", corner_radius=6)
    self.due.grid(row=0, column=0, sticky="nsew", padx=10, pady=4)

    self.classContent = customtkinter.CTkLabel(master=self.subHeader, text=f"Class: {taskInfo[0][7]}", font=customtkinter.CTkFont(size=15), 
                                                anchor="w", justify="left", corner_radius=6)
    self.classContent.grid(row=0, column=1, sticky="nsew", padx=10, pady=4)

    for i in range(len(subTask)):
        self.subTaskInfo[i] = {}

        self.subTaskInfo[i]["frame"] = customtkinter.CTkFrame(master=self.subTaskFrame, corner_radius=6, fg_color=["gray90", "gray21"])
        self.subTaskInfo[i]["frame"].grid(row=i, column=0, sticky="nsew", padx=10, pady=3)
        self.subTaskInfo[i]["frame"].grid_columnconfigure((0), weight=1)

        self.subTask = customtkinter.CTkLabel(master=self.subTaskInfo[i]["frame"], text=f"{subTask[i][1]}", font=customtkinter.CTkFont(size=15), anchor="w", justify="left")
        self.subTask.grid(row=0, column=0, sticky="nsew", padx=10, pady=2)

        self.subTaskInfo[i]["done"] = customtkinter.CTkButton(master=self.subTaskInfo[i]["frame"], text="Done", width=50)
        self.subTaskInfo[i]["done"].grid(row=0, column=1, sticky="nsew", padx=10, pady=4)
        taskID = subTask[i][0]
        makeButtonWork(self, i, taskID)

    self.addSubTask = customtkinter.CTkButton(master=self.subTaskFrame, text="Add Sub-Task", fg_color="transparent", hover_color=["gray90", "gray21"], compound="left", anchor="w",
                                                font=customtkinter.CTkFont(size=15), command=lambda: addSubTaskDisplay(self, id, classID, taskInfo))
    self.addSubTask.grid(row=len(subTask), column=0, sticky="nsew", padx=10, pady=6)

    self.edit = customtkinter.CTkButton(master=self.buttonFrame, text="Edit", command=lambda: editAssignment(self, id))
    self.edit.grid(row=0, column=0, sticky="nsew", padx=10, pady=6)

    self.delete = customtkinter.CTkButton(master=self.buttonFrame, text="Delete", command=lambda: deleteAssignment(self, id))
    self.delete.grid(row=0, column=2, sticky="nsew", padx=10, pady=6)

    self.complete = customtkinter.CTkButton(master=self.buttonFrame, text="Complete", command=lambda: completeAssignment(self, id))
    self.complete.grid(row=0, column=1, sticky="nsew", padx=10, pady=6)

    self.bind("<Return>", lambda event: addSubTaskFunction(self, id, taskInfo))

def addSubTaskDisplay(self, parentID, classID, taskInfo):
    self.addSubTaskFrame = customtkinter.CTkFrame(master=self.subTaskFrame, corner_radius=6, fg_color=topLevel())
    self.addSubTaskFrame.grid(row=self.numSubTask, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)
    self.addSubTaskFrame.grid_columnconfigure((0), weight=1)

    self.subTaskEntry = customtkinter.CTkEntry(master=self.addSubTaskFrame, placeholder_text="Sub-Task Name (max: 30)")
    self.subTaskEntry.grid(row=0, column=0, sticky="nsew", padx=10, pady=6)
    self.subTaskEntry.focus()

    self.subTaskButton = customtkinter.CTkButton(master=self.addSubTaskFrame, text="Add Sub-Task", command=lambda: addSubTaskFunction(self, parentID, taskInfo))
    self.subTaskButton.grid(row=0, column=1, sticky="nsew", padx=0, pady=6)

def addSubTaskFunction(self, parentID, taskInfo):
    if len(self.subTaskEntry.get()) > 30:
        messagebox.showerror("Error", "Sub-Task Name is too long")

    else:
        subTaskName = self.subTaskEntry.get()

        self.addSubTaskFrame.destroy()
        self.addSubTask.grid(row=self.numSubTask, column=0, sticky="nsew")

        id = makeID(20)
        addSubTask(subTaskName, id, taskInfo[0][7], taskInfo[0][8], taskInfo[0][2], taskInfo[0][3], taskInfo[0][4], parentID)

    showAssignment(self, parentID)

def makeButtonWork(self, i, id):
    self.subTaskInfo[i]["done"].configure(command=lambda: doneSubTaskClick(self, id, i))

def doneSubTaskClick(self, id: str, i):
    finishSubTask(self, id)

    self.subTaskInfo[i]["frame"].destroy()

def editAssignment(self, id):
    self.beforeTaskName = self.assignment.cget("text")
    self.beforeDueDate = self.due.cget("text")
    taskInfo = getMainTaskSingle(id)
    print(taskInfo)

    self.editTaskName = customtkinter.CTkEntry(master=self.mainHeader, placeholder_text="Edit Task Name (max: 30)", width=400, 
                                            font=customtkinter.CTkFont(size=18), textvariable=customtkinter.StringVar(value=taskInfo[0][1]))
    self.editTaskName.grid(row=0, column=0, sticky="nsew", padx=10, pady=4)

    self.buttonFrame.grid_forget()
    self.subHeader.grid_forget()

    self.buttonFrame2 = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.buttonFrame2.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)
    self.buttonFrame2.grid_columnconfigure((0, 1), weight=1)

    self.save = customtkinter.CTkButton(master=self.buttonFrame2, text="Save", command=lambda: save(self, id))
    self.save.grid(row=0, column=0, sticky="nsew", padx=10, pady=6)

    self.cancel = customtkinter.CTkButton(master=self.buttonFrame2, text="Cancel", command=lambda: cancel(self, id))
    self.cancel.grid(row=0, column=1, sticky="nsew", padx=10, pady=6)

    self.subHeader2 = customtkinter.CTkFrame(master=self.header, fg_color="transparent", corner_radius=6)
    self.subHeader2.grid(row=1, column=0, sticky="nsew")

    self.due2 = customtkinter.CTkLabel(master=self.subHeader2, text="Due: ", font=customtkinter.CTkFont(size=15))
    self.due2.grid(row=0, column=0, sticky="nsew", padx=10, pady=4)

    self.dueDate2 = customtkinter.CTkEntry(master=self.subHeader2, font=customtkinter.CTkFont(size=15), placeholder_text="DD/MM/YYYY",
                                            textvariable=customtkinter.StringVar(value=f"{taskInfo[0][3]}/{taskInfo[0][2]}/{taskInfo[0][4]}"))
    self.dueDate2.grid(row=0, column=1, sticky="nsew", padx=10, pady=4)

    self.classContent = customtkinter.CTkLabel(master=self.subHeader2, text=f"Class: {taskInfo[0][7]}", font=customtkinter.CTkFont(size=15), 
                                                anchor="w", justify="left", corner_radius=6)
    self.classContent.grid(row=0, column=2, sticky="nsew", pady=4)

    self.subTaskFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())


def completeAssignment(self, id):
    from tabs.home import home

    finishMainTask(self, id)

    messagebox.showinfo(title="Success", message="Assignment Completed")

    home(self)

def deleteAssignment(self, id):
    from tabs.home import home

    deleteTask(id)
    deleteSubTask(id)

    messagebox.showinfo(title="Success", message="Assignment Deleted")

    home(self)

def cancel(self, id):
    showAssignment(self, id)

def save(self, id):
    afterTaskName = self.editTaskName.get()
    afterDueDate = self.dueDate2.get()

    print(self.beforeDueDate)
    print(afterDueDate)

    self.beforeDueDate = self.beforeDueDate.split(" ")[1]
    print(self.beforeDueDate)

    if len(afterTaskName) > 30:
        messagebox.showerror(title="Error", message="Task name too long")

    try:
        datetime.datetime.strptime(afterDueDate, "%m/%d/%Y")
    
    except:
        messagebox.showerror(title="Error", message="Invalid due date")

    if afterTaskName == "" or afterDueDate == "":
        messagebox.showerror(title="Error", message="You are missing a required field")

    if afterTaskName == self.beforeTaskName:
        changeTaskName = False

    else:
        editTask(id, "name", afterTaskName)
        changeTaskName = True

    if self.beforeDueDate == afterDueDate:
        changeDueDate = False

    else:
        editTask(id, "date", afterDueDate)
        changeDueDate = True

    if changeTaskName == True or changeDueDate == True:
        messagebox.showinfo(title="Success", message="Changes saved!")

    showAssignment(self, id)