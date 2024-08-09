from tkinter import messagebox
import customtkinter
import subprocess

from themes.theme import topLevel
from task import *
from screen.classAddEdit import classAddEdit
from tabs.home import makeButtonWork, finishTask
from screen.classInfo import classInfoScreen

def classroom(self, id, className):
    classInfo = getClassInfo(id)
    task = getClassTasks(id)

    self.taskFrame = {}

    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.content.grid_columnconfigure(0, weight=1)
    self.content.grid_rowconfigure((1), weight=1)

    self.header = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.header.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)

    self.mainContent = customtkinter.CTkScrollableFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.mainContent.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)
    self.mainContent.grid_columnconfigure((0), weight=1)

    self.buttonFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.buttonFrame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=7)
    self.buttonFrame.grid_columnconfigure((0,1), weight=1)

    self.className = customtkinter.CTkLabel(master=self.header, text=className, font=customtkinter.CTkFont(size=20, weight="bold"),
                                            anchor="w", justify="left")
    self.className.grid(row=0, column=0, sticky="nsew", padx=10, pady=7)

    self.classTeacher = customtkinter.CTkLabel(master=self.header, text=f"Teacher: {classInfo['teacher']}", cursor="hand2",
                                                font=customtkinter.CTkFont(size=15), anchor="w", justify="left")
    self.classTeacher.grid(row=1, column=0, sticky="nsew", padx=10, pady=7)
    self.classTeacher.bind("<Button-1>", lambda event: teacherEmail(self, classInfo['email']))

    self.editClass = customtkinter.CTkButton(master=self.buttonFrame, text="Edit", command=lambda: classAddEdit(self, "edit", className))
    self.editClass.grid(row=0, column=0, sticky="nsew", padx=10, pady=7)

    self.infoClass = customtkinter.CTkButton(master=self.buttonFrame, text="Info", command=lambda: classInfoScreen(self, id))
    self.infoClass.grid(row=0, column=1, sticky="nsew", padx=10, pady=7)

    if task == []:
        self.noTask = customtkinter.CTkLabel(master=self.mainContent, text="No Tasks", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.noTask.grid(row=0, column=0, sticky="nsew", padx=10, pady=7)

    else:
        for i in range(len(task)):
            self.taskFrame[i] = {}
            self.taskFrame[i]["id"] = task[i][0]

            self.taskFrame[i]["frame"] = customtkinter.CTkFrame(master=self.mainContent, fg_color=["gray90", "gray21"])
            self.taskFrame[i]["frame"].grid(row=i, column=0, sticky="nsew", padx=3, pady=2)

            self.taskFrame[i]["info"] = customtkinter.CTkLabel(master=self.taskFrame[i]["frame"], text=task[i][1], font=customtkinter.CTkFont(size=20, weight="bold"), 
                                                                anchor="w", justify="left", width=400)
            self.taskFrame[i]["info"].grid(row=0, column=0, padx=5)

            date = datetime.datetime(int(task[i][4]), int(task[i][3]), int(task[i][2]))
            if date.day < datetime.datetime.now().day and date.month <= datetime.datetime.now().month and date.year <= datetime.datetime.now().year:
                self.taskFrame[i]["info"].configure(text_color="red")


            self.taskFrame[i]["due"] = customtkinter.CTkLabel(master=self.taskFrame[i]["frame"], text=f"Due: {task[i][3]}/{task[i][2]}/{task[i][4]}", anchor="w", justify="left", width=400)
            self.taskFrame[i]["due"].grid(row=1, column=0, padx=5)

            self.taskFrame[i]["done"] = customtkinter.CTkButton(master=self.taskFrame[i]["frame"], text="Done", width=50, command=lambda: finishTask(self, i))
            #self.done.grid(row=0, rowspan=2, column=1, padx=3, sticky="e")
            self.taskFrame[i]["done"].place(relx=.99, rely=0.25, anchor="ne")

            makeButtonWork(self, i)

def teacherEmail(self, email):
    cmd='echo '+ email +'|clip'
    subprocess.Popen(cmd, shell=True)

    messagebox.showinfo(title="Success", message="Email copied to clipboard!")
