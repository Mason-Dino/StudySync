import customtkinter
import datetime

from task import *


def due(self):
    self.content = customtkinter.CTkScrollableFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure(0, weight=1)
    #self.content.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

    date = datetime.datetime.today()
    daysToMonday = date.weekday()

    monday = date - datetime.timedelta(days=daysToMonday)
    tuesday = date - datetime.timedelta(days=daysToMonday - 1)
    wednesday = date - datetime.timedelta(days=daysToMonday - 2)
    thursday = date - datetime.timedelta(days=daysToMonday - 3)
    friday = date - datetime.timedelta(days=daysToMonday - 4)
    saturday = date - datetime.timedelta(days=daysToMonday - 5)
    sunday = date - datetime.timedelta(days=daysToMonday - 6)

    weekdays = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
    strWeekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

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
            self.taskName = customtkinter.CTkLabel(master=self.taskFrame, text=str(overdue[i][1]), font=customtkinter.CTkFont(size=15), fg_color="red", corner_radius=6)
            self.taskName.grid(row=i, column=0, sticky="nsew", padx=10, pady=2)

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

        if len(dayTask) < 3 and len(dayTask) > 0:
            for i in range(len(dayTask)):
                self.taskName = customtkinter.CTkLabel(master=self.taskFrame, text=dayTask[i][1], font=customtkinter.CTkFont(size=15), fg_color="red", corner_radius=6)
                self.taskName.grid(row=i, column=0, sticky="nsew", padx=10, pady=2)

        elif len(dayTask) == 0:
            self.taskFrame.grid_columnconfigure(0, weight=1)
            self.taskFrame.grid_rowconfigure(0, weight=1)

            self.noTask = customtkinter.CTkLabel(master=self.taskFrame, text="No tasks found", font=customtkinter.CTkFont(size=15))
            self.noTask.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        elif len(dayTask) > 3:
            dayTask = dayTask[0:3] 
            for i in range(len(dayTask)):
                self.taskName = customtkinter.CTkLabel(master=self.taskFrame, text=dayTask[i][1], font=customtkinter.CTkFont(size=15), fg_color="red", corner_radius=6)
                self.taskName.grid(row=i, column=0, sticky="nsew", padx=10, pady=3)

        #self.test = customtkinter.CTkLabel(master=self.taskFrame, text="No tasks found", font=customtkinter.CTkFont(size=15))
        #self.test.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)