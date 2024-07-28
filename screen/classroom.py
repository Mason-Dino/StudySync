from tkinter import messagebox
import customtkinter
import subprocess

from themes.theme import topLevel
from task import *
from screen.classAddEdit import classAddEdit

def classroom(self, id, className):
    classInfo = getClassInfo(id)
    task = getClassTasks(id)

    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.content.grid_columnconfigure(0, weight=1)
    self.content.grid_rowconfigure((1), weight=1)

    self.header = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.header.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)

    self.mainContent = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.mainContent.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)

    self.buttonFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.buttonFrame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)
    self.buttonFrame.grid_columnconfigure((0,1), weight=1)

    self.className = customtkinter.CTkLabel(master=self.header, text=className, font=customtkinter.CTkFont(size=20, weight="bold"),
                                            anchor="w", justify="left")
    self.className.grid(row=0, column=0, sticky="nsew", padx=10, pady=7)

    self.classTeacher = customtkinter.CTkLabel(master=self.header, text=f"Teacher: {classInfo["teacher"]}", cursor="hand2",
                                                font=customtkinter.CTkFont(size=15), anchor="w", justify="left")
    self.classTeacher.grid(row=1, column=0, sticky="nsew", padx=10, pady=7)
    self.classTeacher.bind("<Button-1>", lambda event: teacherEmail(self, classInfo["email"]))

    self.editClass = customtkinter.CTkButton(master=self.buttonFrame, text="Edit", command=lambda: classAddEdit(self, "edit", className))
    self.editClass.grid(row=0, column=0, sticky="nsew", padx=10, pady=7)

    self.infoClass = customtkinter.CTkButton(master=self.buttonFrame, text="Info", command=lambda: print("info"))
    self.infoClass.grid(row=0, column=1, sticky="nsew", padx=10, pady=7)

def teacherEmail(self, email):
    cmd='echo '+ email +'|clip'
    subprocess.Popen(cmd, shell=True)

    messagebox.showinfo(title="Success", message="Email copied to clipboard!")
