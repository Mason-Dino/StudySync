import customtkinter

from themes.theme import *
from task import *

def importance(self):
    padyLevel = 5
    padxLevel = 3

    self.taskFrame = {}
    self.taskFrame["frame"] = {}

    self.content = customtkinter.CTkScrollableFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure((0), weight=1)

    self.taskFrame["frame"]["level 1"] = customtkinter.CTkFrame(master=self.content, fg_color=topLevel(), corner_radius=6)
    self.taskFrame["frame"]["level 1"].grid(row=0, column=0, sticky="nsew", pady=padyLevel, padx=padxLevel)
    self.taskFrame["frame"]["level 1"].grid_columnconfigure((0), weight=1)

    self.level1Label = customtkinter.CTkLabel(master=self.taskFrame["frame"]["level 1"], text="Level 1", font=customtkinter.CTkFont(size=15))
    self.level1Label.grid(row=0, column=0, sticky="nsew", pady=padyLevel, padx=padxLevel)

    self.level1Break = customtkinter.CTkFrame(master=self.taskFrame["frame"]["level 1"], fg_color=["gray92", "gray14"], corner_radius=6, height=4)
    self.level1Break.grid(row=1, column=0, sticky="nsew")

    displayTask(self, "level 1", 1)

    self.taskFrame["frame"]["level 2"] = customtkinter.CTkFrame(master=self.content, fg_color=topLevel(), corner_radius=6)
    self.taskFrame["frame"]["level 2"].grid(row=1, column=0, sticky="nsew", pady=padyLevel, padx=padxLevel)
    self.taskFrame["frame"]["level 2"].grid_columnconfigure((0), weight=1)

    self.level2Label = customtkinter.CTkLabel(master=self.taskFrame["frame"]["level 2"], text="Level 2", font=customtkinter.CTkFont(size=15))
    self.level2Label.grid(row=0, column=0, sticky="nsew", pady=padyLevel, padx=padxLevel)

    self.level2Break = customtkinter.CTkFrame(master=self.taskFrame["frame"]["level 2"], fg_color=["gray92", "gray14"], corner_radius=6, height=4)
    self.level2Break.grid(row=1, column=0, sticky="nsew")

    displayTask(self, "level 2", 2)

    self.taskFrame["frame"]["level 3"] = customtkinter.CTkFrame(master=self.content, fg_color=topLevel(), corner_radius=6)
    self.taskFrame["frame"]["level 3"].grid(row=2, column=0, sticky="nsew", pady=padyLevel, padx=padxLevel)
    self.taskFrame["frame"]["level 3"].grid_columnconfigure((0), weight=1)

    self.level2Label = customtkinter.CTkLabel(master=self.taskFrame["frame"]["level 3"], text="Level 3", font=customtkinter.CTkFont(size=15))
    self.level2Label.grid(row=0, column=0, sticky="nsew", pady=padyLevel, padx=padxLevel)

    self.level2Break = customtkinter.CTkFrame(master=self.taskFrame["frame"]["level 3"], fg_color=["gray92", "gray14"], corner_radius=6, height=4)
    self.level2Break.grid(row=1, column=0, sticky="nsew")

    displayTask(self, "level 3", 3)

    self.level4 = customtkinter.CTkFrame(master=self.content, fg_color=topLevel(), corner_radius=6)
    self.level4.grid(row=3, column=0, sticky="nsew", pady=padyLevel, padx=padxLevel)

    self.level5 = customtkinter.CTkFrame(master=self.content, fg_color=topLevel(), corner_radius=6)
    self.level5.grid(row=4, column=0, sticky="nsew", pady=padyLevel, padx=padxLevel)

def workTask(self, id, i):
    pass

def displayTask(self, levelSTR: str, levelINT: int):
    level1Task = getTaskbyLevel(levelINT)

    self.taskFrame[levelSTR] = {}

    for i in range(len(level1Task)):
        self.taskFrame[levelSTR][i] = {}
        self.taskFrame[levelSTR][i]["id"] = level1Task[i][0]

        self.taskFrame[levelSTR][i]["frame"] = customtkinter.CTkFrame(master=self.taskFrame["frame"][levelSTR], fg_color=top2Level())
        self.taskFrame[levelSTR][i]["frame"].grid(row=i+2, column=0, sticky="nsew", padx=5, pady=4)

        self.taskFrame[levelSTR][i]["info"] = customtkinter.CTkLabel(master=self.taskFrame[levelSTR][i]["frame"], text=level1Task[i][1], font=customtkinter.CTkFont(size=20, weight="bold"), anchor="w", justify="left", width=400)
        #self.info.place(relx=.01, rely=.1, anchor="nw")
        self.taskFrame[levelSTR][i]["info"].grid(row=0, column=0, padx=5)

        date = datetime.datetime(int(level1Task[i][4]), int(level1Task[i][3]), int(level1Task[i][2]))
        now = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
        if date < now:
            self.taskFrame[levelSTR][i]["info"].configure(text_color="red")


        self.taskFrame[levelSTR][i]["due"] = customtkinter.CTkLabel(master=self.taskFrame[levelSTR][i]["frame"], text=f"Due: {level1Task[i][3]}/{level1Task[i][2]}/{level1Task[i][4]}", anchor="w", justify="left", width=400)
        self.taskFrame[levelSTR][i]["due"].grid(row=1, column=0, padx=5)

        self.taskFrame[levelSTR][i]["done"] = customtkinter.CTkButton(master=self.taskFrame[levelSTR][i]["frame"], text="Done", width=50, command=lambda: print("done"))
        #self.done.grid(row=0, rowspan=2, column=1, padx=3, sticky="e")
        self.taskFrame[levelSTR][i]["done"].place(relx=.99, rely=0.25, anchor="ne")