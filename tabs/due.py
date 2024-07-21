import customtkinter
import datetime


def due(self):
    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)

    date = datetime.datetime.today()
    daysToMonday = date.weekday()
    print(monday)

    monday = date - datetime.timedelta(days=daysToMonday)
    tuesday = date - datetime.timedelta(days=daysToMonday - 1)
    wednesday = date - datetime.timedelta(days=daysToMonday - 2)
    thursday = date - datetime.timedelta(days=daysToMonday - 3)
    friday = date - datetime.timedelta(days=daysToMonday - 4)
    saturday = date - datetime.timedelta(days=daysToMonday - 5)
    sunday = date - datetime.timedelta(days=daysToMonday - 6)