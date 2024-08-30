import customtkinter
from tkinter import messagebox

from themes.theme import *
from task import *
from dupTask import findDupTask

def studyTimer(self):
    self.breakTime = 0
    self.studyTime = 0

    self.content = customtkinter.CTkFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure(0, weight=1)

    self.header = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color="transparent")
    self.header.grid(row=0, column=0, sticky="nsew", pady=5, padx=10)
    self.header.grid_columnconfigure(0, weight=1)

    self.timeLabel = customtkinter.CTkLabel(master=self.header, text="00:00:00", font=customtkinter.CTkFont(size=30, weight="bold"))
    self.timeLabel.grid(row=0, column=0, sticky="nsew")

    self.timeInput = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.timeInput.grid(row=1, column=0, sticky="nsew", pady=10, padx=10)
    self.timeInput.grid_columnconfigure((0, 1, 2), weight=1)

    self.hour = customtkinter.CTkEntry(master=self.timeInput, placeholder_text="Hour", font=customtkinter.CTkFont(size=15))
    self.hour.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)

    self.minute = customtkinter.CTkEntry(master=self.timeInput, placeholder_text="Minute", font=customtkinter.CTkFont(size=15))
    self.minute.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)

    self.second = customtkinter.CTkEntry(master=self.timeInput, placeholder_text="Second", font=customtkinter.CTkFont(size=15))
    self.second.grid(row=0, column=2, sticky="nsew", pady=10, padx=10)

    self.timeOption = [self.hour, self.minute, self.second]

    self.breakFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    #self.breakFrame.grid(row=1, column=0, sticky="nsew", pady=10, padx=10)
    self.breakFrame.grid_columnconfigure((0,1), weight=1)

    self.break5 = customtkinter.CTkButton(master=self.breakFrame, text="Break: 5 Min", font=customtkinter.CTkFont(size=15))
    self.break5.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)

    self.add5 = customtkinter.CTkButton(master=self.breakFrame, text="Add: 5 Min", font=customtkinter.CTkFont(size=15))
    self.add5.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)

    self.taskFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.taskFrame.grid(row=2, column=0, sticky="nsew", pady=10, padx=10)
    self.taskFrame.grid_columnconfigure((0,1), weight=1)

    tasks = getMainTasks("ORDER BY date ASC")
    dupTask = findDupTask(tasks)

    self.taskList = ["No Task Selected"]

    for task in tasks:
        self.taskList.append(task[1])

    if dupTask == False:
        pass

    elif dupTask != True:
        for i in range(dupTask["groupNum"]):
            counter = 1
            for c in range(len(dupTask[f"group{i+1}"])):
                self.taskList[dupTask[f"group{i+1}"][c][2]+1] = f"{dupTask[f"group{i+1}"][c][1]} - {counter}"

                counter += 1

    self.taskSel = customtkinter.CTkOptionMenu(master=self.taskFrame, values=self.taskList, font=customtkinter.CTkFont(size=15))
    self.taskSel.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=10, padx=10)

    self.confirm = customtkinter.CTkButton(master=self.taskFrame, text="Confirm", font=customtkinter.CTkFont(size=15), command=lambda: confirm(self))
    self.confirm.grid(row=1, column=0, sticky="nsew", pady=10, padx=10)

    self.reset = customtkinter.CTkButton(master=self.taskFrame, text="Reset", font=customtkinter.CTkFont(size=15))
    self.reset.grid(row=1, column=1, sticky="nsew", pady=10, padx=10)

    self.subTaskFrame = customtkinter.CTkScrollableFrame(master=self.content, fg_color=topLevel())
    #self.subTaskFrame.grid(row=2, column=0, sticky="nsew", pady=10, padx=10)
    self.subTaskFrame.grid_columnconfigure((0), weight=1)

    self.controlButtons = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.controlButtons.grid(row=3, column=0, sticky="nsew", pady=10, padx=10)
    self.controlButtons.grid_columnconfigure((0), weight=1)

    self.start = customtkinter.CTkButton(master=self.controlButtons, text="Start", font=customtkinter.CTkFont(size=15), command=lambda: start(self))
    self.start.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)

    self.pause = customtkinter.CTkButton(master=self.controlButtons, text="Pause", font=customtkinter.CTkFont(size=15))
    #self.pause.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)

    self.stop = customtkinter.CTkButton(master=self.controlButtons, text="Stop", font=customtkinter.CTkFont(size=15))
    #self.stop.grid(row=0, column=2, sticky="nsew", pady=10, padx=10)

def confirm(self):
    self.confirmTask = self.taskSel.get()

    if self.confirmTask == "No Task Selected":
        self.confirmTask = None

def start(self):
    try:
        task = self.confirmTask
        results = None

    except:
        task = None

    if task == None:
        results = messagebox.askyesno(title="Error", message="No Task Selected\nDo you wish to continue without a task?")
        print(results)

    else:
        allTask = getMainTasks()

        task = allTask[self.taskList.index(task)-1]
        moveOn = True

    if results == True:
        moveOn = True

    elif results == False:
        moveOn = False

    if moveOn == True:
        self.controlButtons.grid_columnconfigure((0,1,2), weight=1)
        self.stop.grid(row=0, column=2, sticky="nsew", pady=10, padx=10)
        self.pause.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)

        self.timeInput.grid_forget()
        self.breakFrame.grid(row=1, column=0, sticky="nsew", pady=10, padx=10)

        self.taskFrame.grid_forget()
        self.subTaskFrame.grid(row=2, column=0, sticky="nsew", pady=10, padx=10)

