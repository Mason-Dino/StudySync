import customtkinter

from themes.theme import *
from task import *

def studyTimer(self):
    self.breakTime = 0
    self.studyTime = 0

    self.content = customtkinter.CTkFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure(0, weight=1)

    self.header = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color="transparent")
    self.header.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)
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

    self.taskFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.taskFrame.grid(row=2, column=0, sticky="nsew", pady=10, padx=10)
    self.taskFrame.grid_columnconfigure((0,1), weight=1)

    tasks = getMainTasks()
    taskList = ["None"]

    for task in tasks:
        taskList.append(task[1])

    self.taskSel = customtkinter.CTkOptionMenu(master=self.taskFrame, values=taskList, font=customtkinter.CTkFont(size=15))
    self.taskSel.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=10, padx=10)

    self.confirm = customtkinter.CTkButton(master=self.taskFrame, text="Confirm", font=customtkinter.CTkFont(size=15))
    self.confirm.grid(row=1, column=0, sticky="nsew", pady=10, padx=10)

    self.reset = customtkinter.CTkButton(master=self.taskFrame, text="Reset", font=customtkinter.CTkFont(size=15))
    self.reset.grid(row=1, column=1, sticky="nsew", pady=10, padx=10)

    self.miniContent = customtkinter.CTkFrame(master=self.content, fg_color="transparent")
    #self.miniContent.grid(row=3, column=0, sticky="nsew")
    self.miniContent.grid_rowconfigure((0), weight=1)
    self.miniContent.grid_columnconfigure((0), weight=1)

    self.breakFrame = customtkinter.CTkFrame(master=self.miniContent, fg_color=topLevel(), height=168)
    self.breakFrame.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)
    self.breakFrame.grid_columnconfigure((0,1), weight=1)

    self.break5 = customtkinter.CTkButton(master=self.breakFrame, text="5 Min Break")
    self.break5.grid(row=0, column=0, sticky="nsew", pady=7, padx=10)

    self.break10 = customtkinter.CTkButton(master=self.breakFrame, text="10 Min Break")
    self.break10.grid(row=0, column=1, sticky="nsew", pady=7, padx=10)

    self.add5 = customtkinter.CTkButton(master=self.breakFrame, text="5 Min Add")
    self.add5.grid(row=1, column=0, sticky="nsew", pady=7, padx=10)

    self.add10 = customtkinter.CTkButton(master=self.breakFrame, text="10 Min Add")
    self.add10.grid(row=1, column=1, sticky="nsew", pady=7, padx=10)

    self.subFrame = customtkinter.CTkScrollableFrame(master=self.miniContent, corner_radius=6, fg_color=topLevel(), height=100)
    self.subFrame.grid(row=1, column=0, rowspan=2, sticky="nsew", pady=10, padx=10)
    self.subFrame.grid_columnconfigure((0), weight=1)
    self.subFrame._scrollbar.configure(height=0)

    self.noTasks = customtkinter.CTkLabel(master=self.subFrame, text="Waiting to confirm main task", font=customtkinter.CTkFont(size=15))
    self.noTasks.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)

    self.controlButtons = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.controlButtons.grid(row=4, column=0, sticky="nsew", pady=10, padx=10)
    self.controlButtons.grid_columnconfigure((0), weight=1)

    self.start = customtkinter.CTkButton(master=self.controlButtons, text="Start", font=customtkinter.CTkFont(size=15), command=lambda:test(self))
    self.start.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)

    self.stop = customtkinter.CTkButton(master=self.controlButtons, text="Stop", font=customtkinter.CTkFont(size=15))
    #self.stop.grid(row=0, column=2, sticky="nsew", pady=10, padx=10)

def confirm(self):
    print("hey")

def test(self):
    self.miniContent.grid(row=3, column=0, sticky="nsew")
    self.taskFrame.grid_forget()
    self.timeInput.grid_forget()

    self.controlButtons.grid_columnconfigure((0,1), weight=1)
    self.stop.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)

    for time in self.timeOption:
        time.configure(state="disabled")