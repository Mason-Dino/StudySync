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

    self.taskFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.taskFrame.grid(row=2, column=0, sticky="nsew", pady=10, padx=10)
    self.taskFrame.grid_columnconfigure((0,1), weight=1)

    #working on trying to get index value of selected element, incase of duplicate values
    #trying to make each option have a unique value if it is a dup task, not really working

    tasks = getMainTasks()
    self.taskList = ["None"]
    self.taskContent = ["None"]

    print(tasks)


    
    counter = 1

    for task in tasks:
        self.taskContent.append(task)
        self.taskList.append(f"{task[1]}")


        counter += 1


    """
    duplicatedTasks = []
    duplicatedIndex = []

    for i in range(len(tasks)):
        for c in range(len(tasks)):
            if tasks[i][1] == tasks[c][1] and i != c:
                duplicatedIndex.append(i)

    dupGroup = []

    for dupI in duplicatedIndex:
        duplicatedTasks.append((tasks[dupI][0], tasks[dupI][1], dupI))

    counter = 0

    
    for i in range(len(duplicatedTasks)):
        for c in range(len(duplicatedTasks)):
            if duplicatedTasks[i][1] == duplicatedTasks[c][1] and i != c:
                dupGroup.append((duplicatedTasks[i][2], duplicatedTasks[c][2]))


    for i in range(len(dupGroup)):
        dupGroup[i] = sorted(dupGroup[i])
        dupGroup[i] = tuple(dupGroup[i])

    print(dupGroup)
    print(type(dupGroup))

    dupGroup = list(set(dupGroup))  

    print(dupGroup)

    print(duplicatedTasks)
    """

    self.taskSel = customtkinter.CTkOptionMenu(master=self.taskFrame, values=self.taskList, font=customtkinter.CTkFont(size=15))
    self.taskSel.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=10, padx=10)

    self.confirm = customtkinter.CTkButton(master=self.taskFrame, text="Confirm", font=customtkinter.CTkFont(size=15), command=lambda: confirm(self))
    self.confirm.grid(row=1, column=0, sticky="nsew", pady=10, padx=10)

    self.reset = customtkinter.CTkButton(master=self.taskFrame, text="Reset", font=customtkinter.CTkFont(size=15))
    self.reset.grid(row=1, column=1, sticky="nsew", pady=10, padx=10)

    self.controlButtons = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.controlButtons.grid(row=4, column=0, sticky="nsew", pady=10, padx=10)
    self.controlButtons.grid_columnconfigure((0), weight=1)

    self.start = customtkinter.CTkButton(master=self.controlButtons, text="Start", font=customtkinter.CTkFont(size=15), command=lambda: start(self))
    self.start.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)

    self.stop = customtkinter.CTkButton(master=self.controlButtons, text="Stop", font=customtkinter.CTkFont(size=15))
    #self.stop.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)

def confirm(self):
    print("hey")

    self.taskSel.get()

    #self.

    self.confirmTask = self.taskSel.get()

    print(self.confirmTask)

def start(self):
    print("hey")

    self.controlButtons.grid_columnconfigure((0,1), weight=1)
    self.stop.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)