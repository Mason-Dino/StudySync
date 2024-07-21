import customtkinter
import datetime


def due(self):
    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)

    date = datetime.datetime.today()
    monday = date.weekday()
    print(monday)

    print(f"Monday: {date - datetime.timedelta(days=monday)}")
    print(f"Tuesday: {date - datetime.timedelta(days=monday - 1)}")
    print(f"Wednesday: {date - datetime.timedelta(days=monday - 2)}")
    print(f"Thursday: {date - datetime.timedelta(days=monday - 3)}")
    print(f"Friday: {date - datetime.timedelta(days=monday - 4)}")
    print(f"Saturday: {date - datetime.timedelta(days=monday - 5)}")
    print(f"Sunday: {date - datetime.timedelta(days=monday - 6)}")