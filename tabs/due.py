import customtkinter
import datetime
from tkinter import messagebox

from themes.theme import loadColor
from task import *


def due(self):
    self.content = customtkinter.CTkScrollableFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure(0, weight=1)
    #self.content.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

    date = datetime.datetime.today()
    daysToMonday = date.weekday()

    day1 = date
    day2 = date + datetime.timedelta(days=1)
    day3 = date + datetime.timedelta(days=2)
    day4 = date + datetime.timedelta(days=3)
    day5 = date + datetime.timedelta(days=4)
    day6 = date + datetime.timedelta(days=5)
    day7 = date + datetime.timedelta(days=6)

    weekdays = [day1, day2, day3, day4, day5, day6, day7]
    strWeekdays = [day1.strftime("%A"), day2.strftime("%A"), day3.strftime("%A"), day4.strftime("%A"), day5.strftime("%A"), day6.strftime("%A"), day7.strftime("%A")]
    error = False

    if getOverdueTasks() == []:
        overdueI = 0

    else:
        self.dayFrame = customtkinter.CTkFrame(master=self.content, fg_color=["gray88", "gray19"])
        self.dayFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=2)

        self.labelDay = customtkinter.CTkLabel(master=self.dayFrame, text=f"Overdue", height=50, width=80, font=customtkinter.CTkFont(size=15))
        self.labelDay.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.breakFrame = customtkinter.CTkFrame(master=self.dayFrame, fg_color=["gray92", "gray14"], width=2, height=50)
        self.breakFrame.grid(row=0, column=1, sticky="nsew")

        self.taskFrame = customtkinter.CTkFrame(master=self.dayFrame, fg_color="transparent", height=50)
        self.taskFrame.grid(row=0, column=2, padx=10, sticky="nsew")

        if len(getOverdueTasks()) > 3:
            overdue = getOverdueTasks()[:3]

        else:
            overdue = getOverdueTasks()

        for i in range(len(overdue)):
            try:
                if overdue[i][8] == "0000000000":
                    with open("setup.json", "r") as f:
                        setup = json.load(f)

                    color = setup["theme"]

                else:
                    classInfo = getClassInfo(overdue[i][8])
                    color = classInfo["color"]

                self.taskName = customtkinter.CTkLabel(master=self.taskFrame, text=str(overdue[i][1]), font=customtkinter.CTkFont(size=15), fg_color=loadColor(color), corner_radius=6)
                self.taskName.grid(row=i, column=0, sticky="nsew", padx=10, pady=4)

            except:
                error = True
                print("error 1")

        overdueI = 1

    for i in range(7):
        dayText = f"{weekdays[i].strftime('%m')}/{weekdays[i].strftime('%d')}"

        self.dayFrame = customtkinter.CTkFrame(master=self.content, fg_color=["gray88", "gray19"])
        self.dayFrame.grid(row=weekdays.index(weekdays[i]) + overdueI, column=0, sticky="nsew", padx=10, pady=2)

        self.labelDay = customtkinter.CTkLabel(master=self.dayFrame, text=f"{strWeekdays[i]}\n{dayText}", height=50, width=80, font=customtkinter.CTkFont(size=15))
        self.labelDay.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.breakFrame = customtkinter.CTkFrame(master=self.dayFrame, fg_color=["gray92", "gray14"], width=2, height=50)
        self.breakFrame.grid(row=0, column=1, sticky="nsew")

        self.taskFrame = customtkinter.CTkFrame(master=self.dayFrame, fg_color="transparent", height=50)
        self.taskFrame.grid(row=0, column=2, padx=10, sticky="nsew")

        dayTask = searchDayTask(weekdays[i].strftime('%d'), weekdays[i].strftime('%m'), weekdays[i].strftime('%Y'))

        if len(dayTask) > 3:
            dayTask = dayTask[:3]

        elif len(dayTask) == 0:
            self.taskFrame.grid_columnconfigure(0, weight=1)
            self.taskFrame.grid_rowconfigure(0, weight=1)

            self.noTask = customtkinter.CTkLabel(master=self.taskFrame, text="No tasks found", font=customtkinter.CTkFont(size=15))
            self.noTask.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        else:
            dayTask = dayTask

        for i in range(len(dayTask)):
            try:
                if dayTask[i][8] == "0000000000":
                    with open("setup.json", "r") as f:
                        setup = json.load(f)

                    color = setup["theme"]

                else:
                    classInfo = getClassInfo(dayTask[i][8])
                    color = classInfo["color"]

                self.taskName = customtkinter.CTkLabel(master=self.taskFrame, text=str(dayTask[i][1]), font=customtkinter.CTkFont(size=15), fg_color=loadColor(classInfo["color"]), corner_radius=6)
                self.taskName.grid(row=i, column=0, sticky="nsew", padx=10, pady=4)

            except:
                error = True
                print("error 2")

    if error == True:
        messagebox.showerror(title="Error", message="Error loading tasks")

        #self.test = customtkinter.CTkLabel(master=self.taskFrame, text="No tasks found", font=customtkinter.CTkFont(size=15))
        #self.test.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)