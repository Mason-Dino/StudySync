import customtkinter
import datetime


def due(self):
    self.content = customtkinter.CTkScrollableFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
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

    for day in weekdays:
        dayText = f"{day.strftime('%m')}/{day.strftime('%d')}"

        self.dayFrame = customtkinter.CTkFrame(master=self.content)
        self.dayFrame.grid(row=weekdays.index(day), column=0, sticky="nsew", padx=10)

        self.labelDay = customtkinter.CTkLabel(master=self.dayFrame, text=dayText, height=100, fg_color=["gray88", "gray19"])
        self.labelDay.grid(row=weekdays.index(day), column=0, sticky="nsew", padx=10, pady=10)