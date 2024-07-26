import customtkinter
from task import *

from themes.theme import topLevel
from id import makeID

def showAssignment(self, id):
    self.content = customtkinter.CTkFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure((0, 1), weight=1)
    self.content.grid_rowconfigure((1), weight=1)

    taskInfo = getMainTaskSingle(id)
    subTask = getSubTasks(id)

    print(subTask)
    classID = taskInfo[0][8]

    self.header = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.header.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)
    self.header.grid_columnconfigure((0), weight=1)

    self.mainHeader = customtkinter.CTkFrame(master=self.header, fg_color="transparent")
    self.mainHeader.grid(row=0, column=0, sticky="nsew")

    self.subHeader = customtkinter.CTkFrame(master=self.header, fg_color="transparent")
    self.subHeader.grid(row=1, column=0, sticky="nsew")

    self.subTaskFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.subTaskFrame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)
    self.subTaskFrame.grid_columnconfigure((0), weight=1)

    self.buttonFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.buttonFrame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)
    self.buttonFrame.grid_columnconfigure((0, 1, 2), weight=1)

    self.assignment = customtkinter.CTkLabel(master=self.mainHeader, text=f"{taskInfo[0][1]}", font=customtkinter.CTkFont(size=20, weight="bold"), anchor="w", justify="left")
    self.assignment.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.due = customtkinter.CTkLabel(master=self.subHeader, text=f"Due: {taskInfo[0][3]}/{taskInfo[0][2]}/{taskInfo[0][4]}", font=customtkinter.CTkFont(size=15), anchor="w", justify="left")
    self.due.grid(row=0, column=0, sticky="nsew", padx=10, pady=4)

    self.classContent = customtkinter.CTkLabel(master=self.subHeader, text=f"Class: {taskInfo[0][7]}", font=customtkinter.CTkFont(size=15), anchor="w", justify="left")
    self.classContent.grid(row=0, column=1, sticky="nsew", padx=10, pady=4)

    for i in range(len(subTask)):
        self.subTaskMiniFrame = customtkinter.CTkFrame(master=self.subTaskFrame, corner_radius=6, fg_color=["gray90", "gray21"])
        self.subTaskMiniFrame.grid(row=i, column=0, sticky="nsew", padx=10, pady=3)
        self.subTaskMiniFrame.grid_columnconfigure((0), weight=1)

        self.subTask = customtkinter.CTkLabel(master=self.subTaskMiniFrame, text=f"{subTask[i][1]}", font=customtkinter.CTkFont(size=15), anchor="w", justify="left")
        self.subTask.grid(row=0, column=0, sticky="nsew", padx=10, pady=2)

        self.done = customtkinter.CTkButton(master=self.subTaskMiniFrame, text="Done", width=50)
        self.done.grid(row=0, column=1, sticky="nsew", padx=10, pady=4)
        #self.done.place(relx=0.8, rely=0)

    self.addSubTask = customtkinter.CTkButton(master=self.subTaskFrame, text="Add Sub-Task", fg_color="transparent", hover_color=["gray90", "gray21"], compound="left", anchor="w",
                                                font=customtkinter.CTkFont(size=15), command=lambda: addSubTaskDisplay(self, id, classID, taskInfo))
    self.addSubTask.grid(row=len(subTask), column=0, sticky="nsew", padx=10, pady=6)

    self.edit = customtkinter.CTkButton(master=self.buttonFrame, text="Edit")
    self.edit.grid(row=0, column=0, sticky="nsew", padx=10, pady=6)

    self.delete = customtkinter.CTkButton(master=self.buttonFrame, text="Delete")
    self.delete.grid(row=0, column=2, sticky="nsew", padx=10, pady=6)

    self.complete = customtkinter.CTkButton(master=self.buttonFrame, text="Complete")
    self.complete.grid(row=0, column=1, sticky="nsew", padx=10, pady=6)

def addSubTaskDisplay(self, parentID, classID, taskInfo):
    self.addSubTaskFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.addSubTaskFrame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)
    self.addSubTaskFrame.grid_columnconfigure((0), weight=1)

    self.subTaskEntry = customtkinter.CTkEntry(master=self.addSubTaskFrame, placeholder_text="Sub-Task Name (max: 30)")
    self.subTaskEntry.grid(row=0, column=0, sticky="nsew", padx=10, pady=6)

    self.subTaskButton = customtkinter.CTkButton(master=self.addSubTaskFrame, text="Add Sub-Task", command=lambda: addSubTaskFunction(self, parentID, classID, taskInfo))
    self.subTaskButton.grid(row=0, column=1, sticky="nsew", padx=10, pady=6)

def addSubTaskFunction(self, parentID, classID, taskInfo):
    subTaskName = self.subTaskEntry.get()

    self.addSubTaskFrame.destroy()
    self.addSubTask.grid(row=1, column=0, sticky="nsew")

    id = makeID(20)
    addSubTask(subTaskName, id, taskInfo[0][7], taskInfo[0][8], taskInfo[0][2], taskInfo[0][3], taskInfo[0][4], parentID)

    showAssignment(self, parentID)