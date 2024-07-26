import customtkinter
from task import *

from themes.theme import topLevel

def showAssignment(self, id):
    self.content = customtkinter.CTkFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure((0, 1), weight=1)
    self.content.grid_rowconfigure((1), weight=1)

    taskInfo = getMainTaskSingle(id)

    print(taskInfo)

    self.header = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.header.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)

    self.subTaskFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.subTaskFrame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)

    self.assignment = customtkinter.CTkLabel(master=self.header, text=f"{taskInfo[0][1]}", font=customtkinter.CTkFont(size=20, weight="bold"), width=400, anchor="w", justify="left",)
    self.assignment.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.due = customtkinter.CTkLabel(master=self.header, text=f"Due: {taskInfo[0][3]}/{taskInfo[0][2]}/{taskInfo[0][4]}", font=customtkinter.CTkFont(size=15), width=400, anchor="w", justify="left",)
    self.due.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=4)


