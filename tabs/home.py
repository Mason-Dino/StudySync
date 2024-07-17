import customtkinter
import datetime
import json

def home(self):
    self.taskFrame = {}

    self.content = customtkinter.CTkFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.content.grid_columnconfigure((0,1,2), weight=1)
    self.content.grid_rowconfigure((5), weight=1)

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

    self.task = customtkinter.CTkScrollableFrame(master=self.content, corner_radius=6, fg_color="transparent")
    self.task.grid(row=5, column=0, columnspan=3, sticky="nsew", padx=3)
    self.task.grid_columnconfigure(0, weight=1)

    for i in range(10):
        self.taskFrame[i] = customtkinter.CTkFrame(master=self.task, fg_color=["gray88", "gray19"])
        self.taskFrame[i].grid(row=i, column=0, sticky="nsew", padx=3, pady=2)
        #self.taskFrame[i].bind("<Button-1>", lambda: makeTask(self, i))

        self.info = customtkinter.CTkLabel(master=self.taskFrame[i], text="Homework", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.info.grid(row=0, column=0, padx=3)

        self.due = customtkinter.CTkLabel(master=self.taskFrame[i], text="Due: 7/16/2024")
        self.due.grid(row=1, column=0, padx=0)

        self.done = customtkinter.CTkButton(master=self.taskFrame[i], text="Done", width=50, command=lambda: finishTask(self, i))
        #self.done.grid(row=0, rowspan=2, column=1, padx=3, sticky="e")
        self.done.place(relx=.99, rely=0.25, anchor="ne")

    #self.bind("<Button-1>", makeTask)

def makeTask(self, i):
    print("make task")
    print(i)

def finishTask(self, i):
    print("finish task")
    print(i)