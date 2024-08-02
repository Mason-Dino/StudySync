from tkinter import messagebox
import customtkinter
from task import *
import datetime
import webbrowser

from themes.theme import topLevel, loadLevelColor, top2Level
from id import makeID
from icon import loadIcon


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

    self.flagFrame = customtkinter.CTkFrame(master=self.mainHeader, fg_color=loadLevelColor(taskInfo[0][11]), width=30, height=30)
    self.flagFrame.place(relx=0.92, rely=0.2)

    self.flagImage = customtkinter.CTkLabel(master=self.flagFrame, image=loadIcon("flag"), text="", height=25, width=25)
    #self.flagImage.grid(row=0, column=0)
    self.flagImage.place(anchor="center", relx=0.48, rely=0.45)

    self.subHeader = customtkinter.CTkFrame(master=self.header, fg_color="transparent", corner_radius=6)
    self.subHeader.grid(row=1, column=0, sticky="nsew")

    # ADD TASK INFO SUB-SCREEN INTO A TABVIEW

    self.subTaskFrame = customtkinter.CTkTabview(master=self.content, corner_radius=6, fg_color=topLevel())
    self.subTaskFrame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=0)
    self.subTaskFrame.grid_columnconfigure((0), weight=1)
    self.task = self.subTaskFrame.add("Task")
    self.info = self.subTaskFrame.add("Info")

    self.subTaskFrame.set("Task")

    self.task.grid_columnconfigure(0, weight=1)
    self.task.grid_rowconfigure(0, weight=1)

    self.info.grid_columnconfigure(0, weight=1)
    self.info.grid_rowconfigure(0, weight=1)

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

    self.taskScroll = customtkinter.CTkScrollableFrame(master=self.task, corner_radius=6, fg_color="transparent", height=200)
    self.taskScroll.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
    self.taskScroll.grid_columnconfigure((0), weight=1)

    self.infoFrame = customtkinter.CTkFrame(master=self.info, corner_radius=6, fg_color="transparent")
    self.infoFrame.grid(row=0, column=0, sticky="nsew")
    self.infoFrame.grid_columnconfigure((0,1), weight=1)

    #I need to provide a way to show a text version of:
    #[ ] importance
    #[ ] type of project
    #[ ] PTS value
    #[ ] Submission button

    self.importance = customtkinter.CTkLabel(master=self.infoFrame, text="Importance: ", font=customtkinter.CTkFont(size=15))
    self.importance.grid(row=0, column=0, sticky="nsew", pady=10)

    self.level = customtkinter.CTkFrame(master=self.infoFrame, fg_color=loadLevelColor(taskInfo[0][11]), corner_radius=6, height=20)
    self.level.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)
    self.level.grid_columnconfigure(0, weight=1)
    self.level.grid_rowconfigure(0, weight=1)

    self.level2 = customtkinter.CTkLabel(master=self.level, text=f"Level {taskInfo[0][11]}", font=customtkinter.CTkFont(size=15))
    self.level2.grid(row=0, column=0, sticky="nsew", padx=20, pady=2)

    self.type = customtkinter.CTkLabel(master=self.infoFrame, text="Type: ", font=customtkinter.CTkFont(size=15))
    self.type.grid(row=1, column=0, sticky="nsew", pady=10)

    self.type2 = customtkinter.CTkLabel(master=self.infoFrame, text=taskInfo[0][12], font=customtkinter.CTkFont(size=15))
    self.type2.grid(row=1, column=1, sticky="nsew", pady=10)

    self.pts = customtkinter.CTkLabel(master=self.infoFrame, text="Points: ", font=customtkinter.CTkFont(size=15))
    self.pts.grid(row=2, column=0, sticky="nsew", pady=10)

    if taskInfo[0][10] == "None" or taskInfo[0][10] == 0 or taskInfo[0][10] == "":
        self.pts2 = customtkinter.CTkLabel(master=self.infoFrame, text="No Points", font=customtkinter.CTkFont(size=15))
        self.pts2.grid(row=2, column=1, sticky="nsew", pady=10)

    else:
        if taskInfo[0][10] == 1:
            point = "Point"

        else:
            point = "Points"

        self.pts2 = customtkinter.CTkLabel(master=self.infoFrame, text=f"{taskInfo[0][10]} {point}", font=customtkinter.CTkFont(size=15))
        self.pts2.grid(row=2, column=1, sticky="nsew", pady=10)
    
    if taskInfo[0][9] == "None":
        self.submission = customtkinter.CTkLabel(master=self.infoFrame, text="Submission: ", font=customtkinter.CTkFont(size=15))
        self.submission.grid(row=3, column=0, sticky="nsew", pady=10)

        self.submission2 = customtkinter.CTkLabel(master=self.infoFrame, text="No Submission Link", font=customtkinter.CTkFont(size=15))
        self.submission2.grid(row=3, column=1, sticky="nsew", pady=10)
        self.noSubButton = True

    else:
        self.subButton = customtkinter.CTkButton(master=self.infoFrame, text="Submit Assignment", command=lambda: submitURL(taskInfo[0][9]), height=28)
        self.subButton.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=10, padx=40)
        self.noSubButton = False

    self.lenSubTask = len(subTask)

    for i in range(len(subTask)):
        self.subTaskInfo[i] = {}

        self.subTaskInfo[i]["frame"] = customtkinter.CTkFrame(master=self.taskScroll, corner_radius=6, fg_color=top2Level())
        self.subTaskInfo[i]["frame"].grid(row=i, column=0, sticky="nsew", padx=10, pady=3)
        self.subTaskInfo[i]["frame"].grid_columnconfigure((0), weight=1)

        self.subTask = customtkinter.CTkLabel(master=self.subTaskInfo[i]["frame"], text=f"{subTask[i][1]}", font=customtkinter.CTkFont(size=15), anchor="w", justify="left")
        self.subTask.grid(row=0, column=0, sticky="nsew", padx=10, pady=2)

        self.subTaskInfo[i]["done"] = customtkinter.CTkButton(master=self.subTaskInfo[i]["frame"], text="Done", width=50)
        self.subTaskInfo[i]["done"].grid(row=0, column=1, sticky="nsew", padx=10, pady=4)
        taskID = subTask[i][0]
        makeButtonWork(self, i, taskID)

    self.addSubTask = customtkinter.CTkButton(master=self.taskScroll, text="Add Sub-Task", fg_color="transparent", hover_color=top2Level(), text_color=["gray10", "#DCE4EE"], compound="left", anchor="w",
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
    self.addSubTaskFrame = customtkinter.CTkFrame(master=self.taskScroll, corner_radius=6, fg_color=topLevel())
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

    self.level2.grid_forget()
    self.type2.grid_forget()
    self.pts2.grid_forget()

    self.level.configure(fg_color="transparent")
    self.levelInput = customtkinter.CTkOptionMenu(master=self.level, values=["None", "1 (most)", "2", "3", "4 (least)"], width=100)
    self.levelInput.grid(row=0, column=0, sticky="nsew", padx=10, pady=4)

    self.tempFrame = customtkinter.CTkFrame(master=self.infoFrame, fg_color="transparent", corner_radius=6, height=20)
    self.tempFrame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
    self.tempFrame.grid_columnconfigure((0), weight=1)
    self.tempFrame.grid_rowconfigure((0), weight=1)

    self.projectType = customtkinter.CTkOptionMenu(master=self.tempFrame, values=["Test", "Assignment", "Group", "Essay"], width=100)
    self.projectType.grid(row=0, column=0, sticky="nsew", padx=10, pady=4)

    self.tempFrame2 = customtkinter.CTkFrame(master=self.infoFrame, fg_color="transparent", corner_radius=6, height=20)
    self.tempFrame2.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)
    self.tempFrame2.grid_columnconfigure((0), weight=1)
    self.tempFrame2.grid_rowconfigure((0), weight=1)

    self.pointsEntry = customtkinter.CTkEntry(master=self.tempFrame2, placeholder_text="Points", width=100)
    self.pointsEntry.grid(row=0, column=0, sticky="nsew", padx=10, pady=4)

    self.tempFrame3 = customtkinter.CTkFrame(master=self.infoFrame, fg_color="transparent", corner_radius=6, height=20)
    self.tempFrame3.grid(row=3, column=1, sticky="nsew", padx=10, pady=10)
    self.tempFrame3.grid_columnconfigure((0), weight=1)
    self.tempFrame3.grid_rowconfigure((0), weight=1)

    self.subEntry = customtkinter.CTkEntry(master=self.tempFrame3, placeholder_text="Submission", width=100)
    self.subEntry.grid(row=0, column=0, sticky="nsew", padx=10, pady=4)

    for i in range(self.lenSubTask):
        self.subTaskInfo[i]["done"].configure(text="Delete")

    print(self.noSubButton)

    if self.noSubButton == False:
        self.subButton.grid_forget()
        
        self.submission = customtkinter.CTkLabel(master=self.infoFrame, text="Submission: ", font=customtkinter.CTkFont(size=15))
        self.submission.grid(row=3, column=0, sticky="nsew", pady=10)

    elif self.noSubButton == True:
        self.submission.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

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

    self.beforeDueDate = self.beforeDueDate.split(" ")[1]

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

def submitURL(url):
    try:
        webbrowser.open(url)

    except:
        messagebox.showerror(title="Error", message="Invalid URL")