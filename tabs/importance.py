import customtkinter

from themes.theme import *
from task import *

def importance(self):
    padyLevel = 5
    padxLevel = 3

    self.taskFrame = {}

    self.content = customtkinter.CTkScrollableFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure((0), weight=1)

    self.level1 = customtkinter.CTkFrame(master=self.content, fg_color=topLevel(), corner_radius=6)
    self.level1.grid(row=0, column=0, sticky="nsew", pady=padyLevel, padx=padxLevel)
    self.level1.grid_columnconfigure((0), weight=1)
    self.taskFrame["level 1"] = {}

    self.level1Label = customtkinter.CTkLabel(master=self.level1, text="Level 1", font=customtkinter.CTkFont(size=15))
    self.level1Label.grid(row=0, column=0, sticky="nsew", pady=padyLevel, padx=padxLevel)

    self.level1Break = customtkinter.CTkFrame(master=self.level1, fg_color=["gray92", "gray14"], corner_radius=6, height=4)
    self.level1Break.grid(row=1, column=0, sticky="nsew")

    level1Task = getTaskbyLevel(1)

    for i in range(len(level1Task)):
        self.taskFrame["level 1"][i] = {}
        self.taskFrame["level 1"][i]["id"] = level1Task[i][0]

        self.taskFrame["level 1"][i]["frame"] = customtkinter.CTkFrame(master=self.level1, fg_color=top2Level())
        self.taskFrame["level 1"][i]["frame"].grid(row=i+2, column=0, sticky="nsew", padx=5, pady=4)

        self.taskFrame["level 1"][i]["info"] = customtkinter.CTkLabel(master=self.taskFrame["level 1"][i]["frame"], text=level1Task[i][1], font=customtkinter.CTkFont(size=20, weight="bold"), anchor="w", justify="left", width=400)
        #self.info.place(relx=.01, rely=.1, anchor="nw")
        self.taskFrame["level 1"][i]["info"].grid(row=0, column=0, padx=5)

        date = datetime.datetime(int(level1Task[i][4]), int(level1Task[i][3]), int(level1Task[i][2]))
        now = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
        if date < now:
            self.taskFrame["level 1"][i]["info"].configure(text_color="red")


        self.taskFrame["level 1"][i]["due"] = customtkinter.CTkLabel(master=self.taskFrame["level 1"][i]["frame"], text=f"Due: {level1Task[i][3]}/{level1Task[i][2]}/{level1Task[i][4]}", anchor="w", justify="left", width=400)
        self.taskFrame["level 1"][i]["due"].grid(row=1, column=0, padx=5)

        self.taskFrame["level 1"][i]["done"] = customtkinter.CTkButton(master=self.taskFrame["level 1"][i]["frame"], text="Done", width=50, command=lambda: print("done"))
        #self.done.grid(row=0, rowspan=2, column=1, padx=3, sticky="e")
        self.taskFrame["level 1"][i]["done"].place(relx=.99, rely=0.25, anchor="ne")

    self.level2 = customtkinter.CTkFrame(master=self.content, fg_color=topLevel(), corner_radius=6)
    self.level2.grid(row=1, column=0, sticky="nsew", pady=padyLevel, padx=padxLevel)

    self.level3 = customtkinter.CTkFrame(master=self.content, fg_color=topLevel(), corner_radius=6)
    self.level3.grid(row=2, column=0, sticky="nsew", pady=padyLevel, padx=padxLevel)

    self.level4 = customtkinter.CTkFrame(master=self.content, fg_color=topLevel(), corner_radius=6)
    self.level4.grid(row=3, column=0, sticky="nsew", pady=padyLevel, padx=padxLevel)

    self.level5 = customtkinter.CTkFrame(master=self.content, fg_color=topLevel(), corner_radius=6)
    self.level5.grid(row=4, column=0, sticky="nsew", pady=padyLevel, padx=padxLevel)

def workTask(self, id, i):
    pass