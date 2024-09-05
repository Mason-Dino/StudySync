import customtkinter
from tkinter import messagebox
from datetime import *
import pygame

from themes.theme import *
from task import *
from dupTask import findDupTask
from id import makeID

def studyTimer(self):
    global pauseNow
    global stopNow
    global breakNow
    global add5minTime
    global TimeStamp
    global totalSec
    global TimeStampBreak
    global totalSecBreak
    global timer

    self.exit = True

    self.breakTime = 0
    self.studyTime = 0

    try:
        self.after_cancel(timer)

    except:
        pass

    self.content = customtkinter.CTkFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure(0, weight=1)

    self.header = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color="transparent")
    self.header.grid(row=0, column=0, sticky="nsew", pady=5, padx=10)
    self.header.grid_columnconfigure(0, weight=1)

    self.timeLabel = customtkinter.CTkLabel(master=self.header, text="00:00:00", font=customtkinter.CTkFont(size=30, weight="bold"))
    self.timeLabel.grid(row=0, column=0, sticky="nsew")
    self.timeLabel.configure(text="00:00:00")

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

    self.break5 = customtkinter.CTkButton(master=self.breakFrame, text="Break: 5 Min", font=customtkinter.CTkFont(size=15), command=lambda: break5min(self))
    self.break5.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)

    self.add5 = customtkinter.CTkButton(master=self.breakFrame, text="Add: 5 Min", font=customtkinter.CTkFont(size=15), command=lambda: add5min(self))
    self.add5.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)

    self.breakFrame2 = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    #self.breakFrame2.grid(row=1, column=0, sticky="nsew", pady=10, padx=10)
    self.breakFrame2.grid_columnconfigure((0), weight=1)

    self.endBreakEarly = customtkinter.CTkButton(master=self.breakFrame2, text="End Break Early", font=customtkinter.CTkFont(size=15), command=lambda: stopBreakEarly(self))
    self.endBreakEarly.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)

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

    self.reset = customtkinter.CTkButton(master=self.taskFrame, text="Reset", font=customtkinter.CTkFont(size=15), command=lambda: reset(self))
    self.reset.grid(row=1, column=1, sticky="nsew", pady=10, padx=10)

    self.subTaskFrame = customtkinter.CTkScrollableFrame(master=self.content, fg_color=topLevel())
    #self.subTaskFrame.grid(row=2, column=0, sticky="nsew", pady=10, padx=10)
    self.subTaskFrame.grid_columnconfigure((0), weight=1)

    self.controlButtons = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.controlButtons.grid(row=3, column=0, sticky="nsew", pady=10, padx=10)
    self.controlButtons.grid_columnconfigure((0), weight=1)

    self.start = customtkinter.CTkButton(master=self.controlButtons, text="Start", font=customtkinter.CTkFont(size=15), command=lambda: start(self))
    self.start.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)

    self.pause = customtkinter.CTkButton(master=self.controlButtons, text="Pause", font=customtkinter.CTkFont(size=15), command=lambda: pause(self))
    #self.pause.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)
    pauseNow = False

    self.stop = customtkinter.CTkButton(master=self.controlButtons, text="Stop", font=customtkinter.CTkFont(size=15), command=lambda: stop(self))
    #self.stop.grid(row=0, column=2, sticky="nsew", pady=10, padx=10)
    stopNow = False

def confirm(self):
    self.confirmTask = self.taskSel.get()

    if self.confirmTask == "No Task Selected":
        self.confirmTask = None

    messagebox.showinfo(title="Task Selected", message=f"Task Selected: {self.confirmTask}")

def reset(self):
    self.confirmTask = None

    messagebox.showinfo(title="Task Reset", message="Task Reset")

def start(self):
    self.exit = False

    try:
        task = self.confirmTask
        results = None

    except:
        task = None

    if task == None:
        results = messagebox.askyesno(title="Error", message="No Task Selected\nDo you wish to continue without a task?")
        print(results)

    else:
        allTask = getMainTasks("ORDER BY date ASC")

        task = allTask[self.taskList.index(task)-1]
        moveOn = True

    if results == True:
        moveOn = True

    elif results == False:
        moveOn = False

    if moveOn == True:
        sec = self.second.get()
        min = self.minute.get()
        hour = self.hour.get()


        if sec == "":
            sec = 0

        if min == "":
            min = 0

        if hour == "":
            hour = 0


        try:
            sec = int(sec)
            min = int(min)
            hour = int(hour)
            error = False

            if sec == 0 and min == 0 and hour == 0:
                error = True

        except:
            error = True

        if error == True:
            messagebox.showerror(title="Error", message="Invalid Time Input")

        elif error == False:
            global TimeStamp
            global totalSec
            global timer
            global add5minTime
            global breakNow

            totalSec = sec + (min * 60) + (hour * 3600)
            timeNow = datetime.datetime.now()

            TimeStamp = datetime.datetime.strptime(
                f"""{timeNow.strftime("%m")}/{timeNow.strftime("%d")}/{timeNow.strftime("%Y")} {hour}:{min}:{sec}""",
                "%m/%d/%Y %H:%M:%S"
            )

            add5minTime = False
            breakNow = False
            updateTimer(self)

            self.controlButtons.grid_columnconfigure((0,1), weight=1)
            self.start.grid_forget()
            self.pause.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)
            self.stop.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)

            self.timeInput.grid_forget()
            self.breakFrame.grid(row=1, column=0, sticky="nsew", pady=10, padx=10)

            self.taskFrame.grid_forget()
            self.subTaskFrame.grid(row=2, column=0, sticky="nsew", pady=10, padx=10)

            self.subTaskInfo = {}
            
            if task == None:
                self.addSubTask = customtkinter.CTkButton(master=self.subTaskFrame, text="Add Sub-Task", fg_color="transparent", hover_color=top2Level(), text_color=["gray10", "#DCE4EE"], compound="left", anchor="w",
                                                        font=customtkinter.CTkFont(size=15), command=lambda: addBlankSubTaskDisplay(self))
                self.addSubTask.grid(row=0, column=0, sticky="nsew", padx=10, pady=6)

                self.numSubTask = 0

            else:
                subTask = getSubTasks(task[0])

                self.numSubTask = len(subTask)


                for i in range(len(subTask)):
                    self.subTaskInfo[i] = {}

                    self.subTaskInfo[i]["id"] = subTask[i][0]
                    self.subTaskInfo[i]["classID"] = subTask[i][8]

                    self.subTaskInfo[i]["frame"] = customtkinter.CTkFrame(master=self.subTaskFrame, corner_radius=6, fg_color=top2Level())
                    self.subTaskInfo[i]["frame"].grid(row=i, column=0, sticky="nsew", padx=10, pady=3)
                    self.subTaskInfo[i]["frame"].grid_columnconfigure((0), weight=1)
                    self.subTaskInfo[i]["frame"].grid_rowconfigure((0), weight=1)

                    self.subTaskLabel = customtkinter.CTkLabel(master=self.subTaskInfo[i]["frame"], text=f"{subTask[i][1]}", font=customtkinter.CTkFont(size=15), anchor="w", justify="left")
                    self.subTaskLabel.grid(row=0, column=0, sticky="nsew", padx=10, pady=2)

                    self.subTaskInfo[i]["done"] = customtkinter.CTkButton(master=self.subTaskInfo[i]["frame"], text="Done", width=50, command=lambda: print("done"))
                    self.subTaskInfo[i]["done"].grid(row=0, column=1, sticky="nsew", padx=10, pady=4)

                    makeButtonWork(self, i, self.subTaskInfo[i]["id"])

                self.addSubTask = customtkinter.CTkButton(master=self.subTaskFrame, text="Add Sub-Task", fg_color="transparent", hover_color=top2Level(), text_color=["gray10", "#DCE4EE"], compound="left", anchor="w",
                                                        font=customtkinter.CTkFont(size=15), command=lambda: addSubTaskDisplay(self, task[0], task[8], subTask, self.subTaskInfo))

                self.addSubTask.grid(row=self.numSubTask, column=0, sticky="nsew", padx=10, pady=6)

    self.bind("<Return>", lambda event: print("none"))

def updateTimer(self):
    global TimeStamp
    global totalSec
    global timer
    global add5minTime
    global TimeStampBreak
    global totalSecBreak
    global breakNow
    global pauseNow
    global stopNow

    timer = self.after(1000, lambda: updateTimer(self))

    if breakNow == True and pauseNow == False:
        totalSecBreak -= 1
        TimeStampBreak = TimeStampBreak - timedelta(seconds=1)

        self.timeLabel.configure(text="Break: " + TimeStampBreak.strftime("%H:%M:%S"))

        if totalSecBreak <= 0 or breakNow == False:
            breakNow = False

    if breakNow == False and pauseNow == False:
        totalSec -= 1
        TimeStamp = TimeStamp - timedelta(seconds=1)

        self.breakFrame2.grid_forget()
        self.breakFrame.grid(row=1, column=0, sticky="nsew", pady=10, padx=10)

        self.timeLabel.configure(text=TimeStamp.strftime("%H:%M:%S"))


    if totalSec <= 0 or stopNow == True or self.exit == True:
        self.after_cancel(timer)
        self.timeLabel.configure(text="00:00:00")

        if stopNow == True:
            messagebox.showinfo(title="Timer Stopped", message="Timer Stopped")
            studyTimer(self)

        elif self.exit == True:
            #exists so alarm wont run
            pass

        else:
            pygame.mixer.init()
            sounda= pygame.mixer.Sound("alarm.mp3")
            sounda.play()

            messagebox.showinfo(title="Timer Done", message="Timer Done. Good job!")

            studyTimer(self)

def add5min(self):
    global add5minTime
    global TimeStamp
    global totalSec

    TimeStamp = TimeStamp + timedelta(minutes=300)
    totalSec += 300
    self.timeLabel.configure(text=TimeStamp.strftime("%H:%M:%S"))

def break5min(self):
    global add5minTime
    global TimeStampBreak
    global totalSecBreak
    global breakNow

    breakNow = True

    totalSecBreak = 300
    timeNow = datetime.datetime.now()

    TimeStampBreak = datetime.datetime.strptime(
        f"""{timeNow.strftime("%m")}/{timeNow.strftime("%d")}/{timeNow.strftime("%Y")} 00:05:00""",
        "%m/%d/%Y %H:%M:%S"
    )

    self.breakFrame.grid_forget()
    self.breakFrame2.grid(row=1, column=0, sticky="nsew", pady=10, padx=10)

def stopBreakEarly(self):
    global breakNow
    breakNow = False

def addSubTaskDisplay(self, parentID, classID, taskInfo, frameInfo):
    self.addSubTask.destroy()

    self.addSubTaskFrame = customtkinter.CTkFrame(master=self.subTaskFrame, corner_radius=6, fg_color=topLevel())
    self.addSubTaskFrame.grid(row=self.numSubTask, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)
    self.addSubTaskFrame.grid_columnconfigure((0), weight=1)

    self.subTaskEntry = customtkinter.CTkEntry(master=self.addSubTaskFrame, placeholder_text="Sub-Task Name (max: 30)")
    self.subTaskEntry.grid(row=0, column=0, sticky="nsew", padx=10, pady=6)
    self.subTaskEntry.focus()

    self.subTaskButton = customtkinter.CTkButton(master=self.addSubTaskFrame, text="Add Sub-Task", command=lambda: addSubTaskFunction(self, parentID, taskInfo, frameInfo))
    self.subTaskButton.grid(row=0, column=1, sticky="nsew", padx=0, pady=6)

    self.bind("<Return>", lambda event: addSubTaskFunction(self, parentID, taskInfo, frameInfo))
    self.bind("<Escape>", lambda event: print("escape"))

def addBlankSubTaskDisplay(self):
    self.addSubTask.destroy()

    self.addSubTaskFrame = customtkinter.CTkFrame(master=self.subTaskFrame, corner_radius=6, fg_color=topLevel())
    self.addSubTaskFrame.grid(row=self.numSubTask, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)
    self.addSubTaskFrame.grid_columnconfigure((0), weight=1)

    self.subTaskEntry = customtkinter.CTkEntry(master=self.addSubTaskFrame, placeholder_text="Sub-Task Name (max: 30)")
    self.subTaskEntry.grid(row=0, column=0, sticky="nsew", padx=10, pady=6)
    self.subTaskEntry.focus()

    self.subTaskButton = customtkinter.CTkButton(master=self.addSubTaskFrame, text="Add Sub-Task", command=lambda: addBlankSubTaskFunction(self))
    self.subTaskButton.grid(row=0, column=1, sticky="nsew", padx=0, pady=6)

    self.bind("<Return>", lambda event: addBlankSubTaskFunction(self))

def addSubTaskFunction(self, parentID, taskInfo, frameInfo):
    if len(self.subTaskEntry.get()) > 30:
        messagebox.showerror("Error", "Sub-Task Name is too long")

    else:
        subTaskName = self.subTaskEntry.get()

        self.addSubTaskFrame.destroy()
        self.addSubTask.destroy()

        id = makeID(20)
        #can't make subtask unless there already exists a task this is because taskInfo doesn't have any info

        taskInfo = getMainTaskSingle(parentID)
        addSubTask(subTaskName, id, taskInfo[0][7], taskInfo[0][8], taskInfo[0][2], taskInfo[0][3], taskInfo[0][4], parentID)
        print(self.numSubTask)

        for i in range(self.numSubTask):
            frameInfo[i]["frame"].grid_forget()

        subTask = getSubTasks(parentID)

        self.numSubTask = len(subTask)

        self.subTaskInfo = {}
        self.subTaskInfo["type"] = "task"

        for i in range(len(subTask)):
            self.subTaskInfo[i] = {}

            self.subTaskInfo[i]["id"] = subTask[i][0]
            self.subTaskInfo[i]["classID"] = subTask[i][8]

            self.subTaskInfo[i]["frame"] = customtkinter.CTkFrame(master=self.subTaskFrame, corner_radius=6, fg_color=top2Level())
            self.subTaskInfo[i]["frame"].grid(row=i, column=0, sticky="nsew", padx=10, pady=3)
            self.subTaskInfo[i]["frame"].grid_columnconfigure((0), weight=1)

            self.subTaskLabel = customtkinter.CTkLabel(master=self.subTaskInfo[i]["frame"], text=f"{subTask[i][1]}", font=customtkinter.CTkFont(size=15), anchor="w", justify="left")
            self.subTaskLabel.grid(row=0, column=0, sticky="nsew", padx=10, pady=2)

            self.subTaskInfo[i]["done"] = customtkinter.CTkButton(master=self.subTaskInfo[i]["frame"], text="Done", width=50, command=lambda: print("done"))
            self.subTaskInfo[i]["done"].grid(row=0, column=1, sticky="nsew", padx=10, pady=4)

            makeButtonWork(self, i, self.subTaskInfo[i]["id"])

        self.addSubTask = customtkinter.CTkButton(master=self.subTaskFrame, text="Add Sub-Task", fg_color="transparent", hover_color=top2Level(), text_color=["gray10", "#DCE4EE"], compound="left", anchor="w",
                                                font=customtkinter.CTkFont(size=15), command=lambda: addSubTaskDisplay(self, parentID, taskInfo[0][8], subTask, self.subTaskInfo))

        self.addSubTask.grid(row=self.numSubTask, column=0, sticky="nsew", padx=10, pady=6)

def addBlankSubTaskFunction(self):
    print("blank")
    if len(self.subTaskEntry.get()) > 30:
        messagebox.showerror("Error", "Sub-Task Name is too long")  

    else:
        print(self.subTaskEntry.get())
        subTaskName = self.subTaskEntry.get()
        self.addSubTaskFrame.destroy()
        id = makeID(20)

        day = datetime.datetime.now().day
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year

        addSubTask(subTaskName, id, "StudyTimer", "None", day, month, year, "StudyTimer")

        subTask = getStudySubTasks()

        self.numSubTask = len(subTask)

        self.subTaskInfo = {}
        self.subTaskInfo["type"] = "blank"

        for i in range(len(subTask)):
            self.subTaskInfo[i] = {}

            self.subTaskInfo[i]["id"] = subTask[i][0]
            self.subTaskInfo[i]["classID"] = subTask[i][8]

            self.subTaskInfo[i]["frame"] = customtkinter.CTkFrame(master=self.subTaskFrame, corner_radius=6, fg_color=top2Level(), height=50)
            self.subTaskInfo[i]["frame"].grid(row=i, column=0, sticky="nsew", padx=10, pady=3)
            self.subTaskInfo[i]["frame"].grid_columnconfigure((0), weight=1)

            self.subTask = customtkinter.CTkLabel(master=self.subTaskInfo[i]["frame"], text=f"{subTask[i][1]}", font=customtkinter.CTkFont(size=15), anchor="w", justify="left")
            self.subTask.grid(row=0, column=0, sticky="nsew", padx=10, pady=2)

            self.subTaskInfo[i]["done"] = customtkinter.CTkButton(master=self.subTaskInfo[i]["frame"], text="Done", width=50, command=lambda: print("done"))
            self.subTaskInfo[i]["done"].grid(row=0, column=1, sticky="nsew", padx=10, pady=4)

            makeButtonWork(self, i, self.subTaskInfo[i]["id"])

        self.addSubTask = customtkinter.CTkButton(master=self.subTaskFrame, text="Add Sub-Task", fg_color="transparent", hover_color=top2Level(), text_color=["gray10", "#DCE4EE"], compound="left", anchor="w",
                                                font=customtkinter.CTkFont(size=15), command=lambda: addBlankSubTaskDisplay(self))

        self.addSubTask.grid(row=self.numSubTask, column=0, sticky="nsew", padx=10, pady=6)

def makeButtonWork(self, i, id):
    self.subTaskInfo[i]["done"].configure(command=lambda: doneSubTaskClick(self, id, i))

def doneSubTaskClick(self, id: str, i):
    #code isn't deleting the task from the list all the time so its being a little wired right now
    print(id)
    print(i)
    parentID = getSubTaskParentID(id)[0][0]
    finishSubTask(self, id)
    self.subTaskInfo[i]["frame"].grid_forget()

    typeOfTask = self.subTaskInfo["type"]

    self.subTaskFrame.destroy()

    self.subTaskFrame = customtkinter.CTkScrollableFrame(master=self.content, fg_color=topLevel())
    self.subTaskFrame.grid(row=2, column=0, sticky="nsew", pady=10, padx=10)
    self.subTaskFrame.grid_columnconfigure((0), weight=1)

    if typeOfTask == "blank":
        subTask = getStudySubTasks()

        self.numSubTask = len(subTask)

        self.subTaskInfo = {}
        self.subTaskInfo["type"] = "blank"

        for i in range(len(subTask)):
            self.subTaskInfo[i] = {}

            self.subTaskInfo[i]["id"] = subTask[i][0]
            self.subTaskInfo[i]["classID"] = subTask[i][8]

            self.subTaskInfo[i]["frame"] = customtkinter.CTkFrame(master=self.subTaskFrame, corner_radius=6, fg_color=top2Level(), height=50)
            self.subTaskInfo[i]["frame"].grid(row=i, column=0, sticky="nsew", padx=10, pady=3)
            self.subTaskInfo[i]["frame"].grid_columnconfigure((0), weight=1)

            self.subTask = customtkinter.CTkLabel(master=self.subTaskInfo[i]["frame"], text=f"{subTask[i][1]}", font=customtkinter.CTkFont(size=15), anchor="w", justify="left")
            self.subTask.grid(row=0, column=0, sticky="nsew", padx=10, pady=2)

            self.subTaskInfo[i]["done"] = customtkinter.CTkButton(master=self.subTaskInfo[i]["frame"], text="Done", width=50, command=lambda: print("done"))
            self.subTaskInfo[i]["done"].grid(row=0, column=1, sticky="nsew", padx=10, pady=4)

            makeButtonWork(self, i, self.subTaskInfo[i]["id"])

        self.addSubTask = customtkinter.CTkButton(master=self.subTaskFrame, text="Add Sub-Task", fg_color="transparent", hover_color=top2Level(), text_color=["gray10", "#DCE4EE"], compound="left", anchor="w",
                                                font=customtkinter.CTkFont(size=15), command=lambda: addBlankSubTaskDisplay(self))

        self.addSubTask.grid(row=self.numSubTask, column=0, sticky="nsew", padx=10, pady=6)

    if typeOfTask == "task":
        subTask = getSubTasks(parentID)
        mainTask = getMainTaskSingle(parentID)

        print(mainTask)

        self.numSubTask = len(subTask)

        self.subTaskInfo = {}
        self.subTaskInfo["type"] = "task"

        for i in range(len(subTask)):
            self.subTaskInfo[i] = {}

            self.subTaskInfo[i]["id"] = subTask[i][0]
            self.subTaskInfo[i]["classID"] = subTask[i][8]

            self.subTaskInfo[i]["frame"] = customtkinter.CTkFrame(master=self.subTaskFrame, corner_radius=6, fg_color=top2Level(), height=50)
            self.subTaskInfo[i]["frame"].grid(row=i, column=0, sticky="nsew", padx=10, pady=3)
            self.subTaskInfo[i]["frame"].grid_columnconfigure((0), weight=1)

            self.subTask = customtkinter.CTkLabel(master=self.subTaskInfo[i]["frame"], text=f"{subTask[i][1]}", font=customtkinter.CTkFont(size=15), anchor="w", justify="left")
            self.subTask.grid(row=0, column=0, sticky="nsew", padx=10, pady=2)

            self.subTaskInfo[i]["done"] = customtkinter.CTkButton(master=self.subTaskInfo[i]["frame"], text="Done", width=50, command=lambda: print("done"))
            self.subTaskInfo[i]["done"].grid(row=0, column=1, sticky="nsew", padx=10, pady=4)

            makeButtonWork(self, i, self.subTaskInfo[i]["id"])

        #def addSubTaskDisplay(self, parentID, classID, taskInfo, frameInfo):
        self.addSubTask = customtkinter.CTkButton(master=self.subTaskFrame, text="Add Sub-Task", fg_color="transparent", hover_color=top2Level(), text_color=["gray10", "#DCE4EE"], compound="left", anchor="w",
                                                font=customtkinter.CTkFont(size=15), command=lambda: addSubTaskDisplay(self, parentID, mainTask[0][8], mainTask, self.subTaskInfo))

        self.addSubTask.grid(row=self.numSubTask, column=0, sticky="nsew", padx=10, pady=6)

def pause(self):
    global pauseNow

    if pauseNow == True:
        pauseNow = False
        self.pause.configure(text="Pause")

    elif pauseNow == False:
        pauseNow = True
        self.pause.configure(text="Resume")

def stop(self):
    global stopNow

    stopNow = True