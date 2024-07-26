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
    self.header.grid_columnconfigure((0), weight=1)

    self.mainHeader = customtkinter.CTkFrame(master=self.header, fg_color="transparent")
    self.mainHeader.grid(row=0, column=0, sticky="nsew")

    self.subHeader = customtkinter.CTkFrame(master=self.header, fg_color="transparent")
    self.subHeader.grid(row=1, column=0, sticky="nsew")

    self.subTaskFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.subTaskFrame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)

    self.buttonFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.buttonFrame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)
    self.buttonFrame.grid_columnconfigure((0, 1, 2), weight=1)

    self.assignment = customtkinter.CTkLabel(master=self.mainHeader, text=f"{taskInfo[0][1]}", font=customtkinter.CTkFont(size=20, weight="bold"), anchor="w", justify="left",)
    self.assignment.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.due = customtkinter.CTkLabel(master=self.subHeader, text=f"Due: {taskInfo[0][3]}/{taskInfo[0][2]}/{taskInfo[0][4]}", font=customtkinter.CTkFont(size=15), anchor="w", justify="left",)
    self.due.grid(row=0, column=0, sticky="nsew", padx=10, pady=4)

    self.classContent = customtkinter.CTkLabel(master=self.subHeader, text=f"Class: {taskInfo[0][7]}", font=customtkinter.CTkFont(size=15), anchor="w", justify="left",)
    self.classContent.grid(row=0, column=1, sticky="nsew", padx=10, pady=4)

    self.edit = customtkinter.CTkButton(master=self.buttonFrame, text="Edit")
    self.edit.grid(row=0, column=0, sticky="nsew", padx=10, pady=6)

    self.delete = customtkinter.CTkButton(master=self.buttonFrame, text="Delete")
    self.delete.grid(row=0, column=1, sticky="nsew", padx=10, pady=6)

    self.complete = customtkinter.CTkButton(master=self.buttonFrame, text="Complete")
    self.complete.grid(row=0, column=2, sticky="nsew", padx=10, pady=6)
