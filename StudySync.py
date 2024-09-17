from integration.todoist import syncTodoist
from tabs.assignments import assignments
from tabs.importance import importance
from tabs.setting import settings
from tabs.classes import classes
from tabs.home import home
from tabs.studyTimer import studyTimer
from icon import loadIcon
from tabs.due import due
from version import checkIfBeta

from tkinter import messagebox
from setup import setup
from PIL import Image
import customtkinter
import json
import os


class StudySync(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        with open("setup.json", "r") as f:
            self.setupDir = json.load(f)

        self.geometry("700x450")
        self.title("StudySync")

        self.after(201, lambda :self.iconbitmap(r"logo\StudySync-ico.ico"))

        icon_path = os.path.join(os.path.dirname(__file__), "icons")
        self.settingImage = loadIcon("settings")

        customtkinter.set_appearance_mode(self.setupDir["mode"])  # Modes: system (default), light, dark

        try:
            customtkinter.set_default_color_theme(f"themes/{self.setupDir['theme'].lower()}.json")  # Themes: blue (default), dark-blue, green

        except:
            customtkinter.set_default_color_theme("themes/teal.json")

        syncTodoist(self)


        self.numClasses = self.setupDir["numClasses"]

        self.grid_columnconfigure((1,2), weight=1)
        self.grid_columnconfigure((3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.side = customtkinter.CTkFrame(master=self, corner_radius=0)  # Create the side frame
        self.side.grid(row=0, rowspan=3, column=0, sticky="nswe")  # Position the side frame

        self.name = customtkinter.CTkLabel(master=self.side, text="StudySync", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.name.grid(row=0, column=0, padx=15, pady=20)
        self.name.bind("<Button-1>", lambda event: self.sync())

        self.infoFrame = customtkinter.CTkFrame(master=self.side, height=250, fg_color=["gray86","gray17"])
        self.infoFrame.grid_columnconfigure(0, weight=1)
        self.infoFrame.grid(row=1, rowspan=2, column=0, sticky="nswe", pady=10)

        b = 0

        if self.setupDir["tabs"]["home"] == True:
            self.home = customtkinter.CTkButton(master=self.infoFrame, text="Home", command=lambda:home(self))
            self.home.grid(row=b, column=0, padx=15, pady=5)

            b += 1

        if self.setupDir["tabs"]["class"] == True:
            self.classes = customtkinter.CTkButton(master=self.infoFrame, text="Classes", command=lambda: self.classesMain())
            self.classes.grid(row=b, column=0, padx=15, pady=5)

            b += 1

        if self.setupDir["tabs"]["task"] == True:
            self.assignments = customtkinter.CTkButton(master=self.infoFrame, text="Assignments", command=lambda:assignments(self))
            self.assignments.grid(row=b, column=0, padx=15, pady=5)

            b += 1
        
        if self.setupDir["tabs"]["due"] == True:
            self.due = customtkinter.CTkButton(master=self.infoFrame, text="Due soon", command=lambda:due(self))
            self.due.grid(row=b, column=0, padx=15, pady=5)

            b += 1

        if self.setupDir["tabs"]["important"] == True:
            self.importance = customtkinter.CTkButton(master=self.infoFrame, text="Importance", command=lambda: importance(self))
            self.importance.grid(row=b, column=0, padx=15, pady=5)

            b += 1

        if self.setupDir["tabs"]["sleep-timer"] == True:
            self.sleep = customtkinter.CTkButton(master=self.infoFrame, text="Study Timer", command=lambda: studyTimer(self))
            self.sleep.grid(row=b, column=0, padx=15, pady=5)

            b += 1

        self.settingsButton = customtkinter.CTkButton(master=self.side, text="Settings", command=lambda: self.settingsMain(), image=self.settingImage)
        #self.settingsButton.grid(row=3, column=0, padx=15, pady=100)
        self.settingsButton.place(relx=.09, rely=.9)

        self.bind("<Control_L><h>", lambda event: home(self))
        self.bind("<Control_L><f>", lambda event: classes(self))
        self.bind("<Control_L><q>", lambda event: assignments(self))
        self.bind("<Control_L><d>", lambda event: due(self))
        self.bind("<Control_L><s>", lambda event: settings(self))
        self.bind("<Control_L><i>", lambda event: importance(self))
        self.bind("<Control_L><t>", lambda event: studyTimer(self))

        self.bind("<Control_R><h>", lambda event: home(self))
        self.bind("<Control_R><f>", lambda event: classes(self))
        self.bind("<Control_R><q>", lambda event: assignments(self))
        self.bind("<Control_R><d>", lambda event: due(self))
        self.bind("<Control_R><s>", lambda event: settings(self))
        self.bind("<Control_R><i>", lambda event: importance(self))
        self.bind("<Control_R><t>", lambda event: studyTimer(self))

        home(self)

    def button_function(self):
        print("button pressed")

    def settingsMain(self):
        settings(self)

    def classesMain(self):
        classes(self)

    def sync(self):
        syncTodoist(self)
        home(self)


if __name__ == "__main__":
    with open("setup.json", "r") as f:
        setupDir = json.load(f)

    try:
        if setupDir["setupComplete"] == False or setupDir["setupComplete"] == None:
            app = setup()
            app.mainloop()

        elif setupDir["betaUser"] == True:
            if checkIfBeta() == True:
                app = StudySync()
                app.mainloop()

            else:
                messagebox.showerror(title="Error", message="Beta version of StudySync has ended")

        elif setupDir["setupComplete"] == True:
            app = StudySync()
            app.mainloop()

        else:
            app = StudySync()
            app.mainloop()

    except KeyError as error:
        print(error)
        messagebox.showerror(title="Error", message="Invalid setup.json file")
        app = setup()
        app.mainloop()