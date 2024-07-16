import customtkinter
import datetime
import json

def home(self):
    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.content.grid_columnconfigure((0,1,2), weight=1)

    with open("setup.json", "r") as f:
        self.setupDir = json.load(f)

    self.classNum = self.setupDir["numClasses"]

    classNameValues = ["None"]

    self.progressbar = customtkinter.CTkProgressBar(master=self.content)
    self.progressbar.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)
    self.progressbar.set(0)

    self.taskName = customtkinter.CTkEntry(master=self.content, placeholder_text="Task Name")
    self.taskName.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    for i in range(self.classNum):
        classNameValues.append(self.setupDir[f"class{i+1}"]["name"])

    self.className = customtkinter.CTkOptionMenu(master=self.content, values=classNameValues, variable=customtkinter.StringVar(value="Pick Class"))
    self.className.grid(row=2, column=2, sticky="nsew", padx=10, pady=10)

    self.day = customtkinter.CTkEntry(master=self.content, placeholder_text="Day")
    self.day.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

    self.month = customtkinter.CTkEntry(master=self.content, placeholder_text="Month")
    self.month.grid(row=3, column=1, sticky="nsew", padx=10, pady=10)

    self.year = customtkinter.CTkEntry(master=self.content, placeholder_text="Year", textvariable=customtkinter.StringVar(value=datetime.datetime.now().year))
    self.year.grid(row=3, column=2, sticky="nsew", padx=10, pady=10)


    self.button = customtkinter.CTkButton(master=self.content, text="Add Task")
    self.button.grid(row=4, column=1, sticky="nsew", padx=10, pady=10)

    self.task = customtkinter.CTkScrollableFrame(master=self.content, fg_color="transparent", height=100)
    self.task.grid(row=5, column=0, columnspan=3, sticky="nsew", pady=10)

    for i in range(20):
        self.taskEvent = customtkinter.CTkLabel(master=self.task, text=f"Task {i+1}")
        self.taskEvent.grid(row=i, column=0, sticky="nsew", padx=10)