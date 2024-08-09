from version import getMainVersion, getUserVersion
from screen.classColor import showClassColors
from task import deleteDatabase, makeTestTask
from screen.classAddEdit import classAddEdit
from themes.theme import topLevel
from tkinter import messagebox
from tkinter import filedialog
from icon import getIcons
import customtkinter
import webbrowser
import shutil
import json
import os


def settings(self):
    classes = []
    overallPadyOutside = 9
    overallPadyInside = 9
    RowI = 0

    self.content = customtkinter.CTkScrollableFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.content.grid_columnconfigure(0, weight=1)

    with open("setup.json", "r") as f:
        self.setupDir = json.load(f)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    self.appearanceFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.appearanceFrame.grid(row=RowI, column=0, sticky="nsew", padx=10, pady=overallPadyOutside)
    self.appearanceFrame.grid_columnconfigure((1), weight=1)

    RowI += 1

    self.appearance = customtkinter.CTkOptionMenu(master=self.appearanceFrame, values=["System", "Light", "Dark"], command=changeAppearanceMode, width=200)
    self.appearance.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.currentAppearance = customtkinter.CTkLabel(master=self.appearanceFrame, text="Appearance Mode: " + str(self.setupDir["mode"]).capitalize())
    self.currentAppearance.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    self.themeFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.themeFrame.grid(row=RowI, column=0, sticky="nsew", padx=10, pady=overallPadyInside)
    self.themeFrame.grid_columnconfigure((1), weight=1)

    RowI += 1

    self.theme = customtkinter.CTkOptionMenu(master=self.themeFrame, values=["Teal", "Orange", "Purple", "Red", "Yellow", "Green", "Blue", "Grey"], command=changeTheme, width=200, variable=customtkinter.StringVar(value=self.setupDir["theme"]))
    self.theme.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.currentTheme = customtkinter.CTkLabel(master=self.themeFrame, text="Current Theme: " + self.setupDir["theme"])
    self.currentTheme.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    self.turnOffFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.turnOffFrame.grid(row=RowI, column=0, sticky="nsew", padx=10, pady=overallPadyInside)
    self.turnOffFrame.grid_columnconfigure((0,1), weight=1)

    RowI += 1

    self.sideLeft = customtkinter.CTkFrame(master=self.turnOffFrame, fg_color="transparent")
    self.sideLeft.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.homeSwitch = customtkinter.CTkSwitch(master=self.sideLeft, text="Home")
    self.homeSwitch.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.classSwitch = customtkinter.CTkSwitch(master=self.sideLeft, text="Classes")
    self.classSwitch.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    self.taskSwitch = customtkinter.CTkSwitch(master=self.sideLeft, text="Assignments")
    self.taskSwitch.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

    self.dueSwitch = customtkinter.CTkSwitch(master=self.sideLeft, text="Due")
    self.dueSwitch.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

    self.importSwitch = customtkinter.CTkSwitch(master=self.sideLeft, text="Important")
    self.importSwitch.grid(row=4, column=0, sticky="nsew", padx=10, pady=10)

    self.sideRight = customtkinter.CTkFrame(master=self.turnOffFrame, fg_color="transparent")
    self.sideRight.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    self.sideRight.grid_columnconfigure((0), weight=1)

    self.des = customtkinter.CTkLabel(master=self.sideRight, text="Turn on and off\nOn: See Button\nOff: No Button", font=customtkinter.CTkFont(size=15))
    self.des.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.turnOff = customtkinter.CTkButton(master=self.sideRight, text="Turn all Off", command=lambda: turnOff(self))
    self.turnOff.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    self.turnOn = customtkinter.CTkButton(master=self.sideRight, text="Turn all On", command=lambda: turnOn(self))
    self.turnOn.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

    self.update = customtkinter.CTkButton(master=self.sideRight, text="Update", command=lambda: updateTabs(self))
    self.update.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)


    pageSwitch = [self.homeSwitch, self.classSwitch, self.taskSwitch, self.dueSwitch, self.importSwitch]
    name = ["home", "class", "task", "due", "important"]

    with open("setup.json", "r") as f:
        setupDir = json.load(f)

    for i in range(5):
        if setupDir["tabs"][name[i]] == True:
            pageSwitch[i].select()

        else:
            pageSwitch[i].deselect()


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    self.classEditFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.classEditFrame.grid(row=RowI, column=0, sticky="nsew", padx=10, pady=overallPadyInside)
    self.classEditFrame.grid_columnconfigure((0,1), weight=1)

    RowI += 1

    with open("setup.json", "r") as f:
        self.setupDir = json.load(f)

    for i in range(self.setupDir["numClasses"]):
        classes.append(self.setupDir[f"class{i+1}"]["name"])

    self.classEdit = customtkinter.CTkOptionMenu(master=self.classEditFrame, values=classes, width=200)
    self.classEdit.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.edit = customtkinter.CTkButton(master=self.classEditFrame, text="Edit Class", command=lambda: editClassSave(self, self.classEdit.get()))
    self.edit.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    self.delete = customtkinter.CTkButton(master=self.classEditFrame, text="Delete Class", command=lambda: deleteClass(self, self.classEdit.get()))
    self.delete.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    self.addClassFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.addClassFrame.grid(row=RowI, column=0, sticky="nsew", padx=10, pady=overallPadyInside)
    self.addClassFrame.grid_columnconfigure((0), weight=1)

    RowI += 1

    self.addClass = customtkinter.CTkButton(master=self.addClassFrame, text="Add Class", command=lambda: addClass(self))
    self.addClass.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    self.classColorFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.classColorFrame.grid(row=RowI, column=0, sticky="nsew", padx=10, pady=overallPadyInside)
    self.classColorFrame.grid_columnconfigure((0), weight=1)

    RowI += 1

    self.classColor = customtkinter.CTkButton(master=self.classColorFrame, text="Class Color", command=lambda: showClassColors(self))
    self.classColor.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)



    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    self.level = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.level.grid(row=RowI, column=0, sticky="nsew", padx=10, pady=overallPadyOutside)
    self.level.grid_columnconfigure((0,1), weight=1)

    RowI += 1

    self.currentProgress = customtkinter.CTkLabel(master=self.level, text="Current Progress: " + str(round(round(self.setupDir["progress"], 3) * 100, 2)) + "%")
    self.currentProgress.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    
    self.currentLevel = customtkinter.CTkLabel(master=self.level, text="Current Level: " + str(self.setupDir["level"]))
    self.currentLevel.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    self.currentClasses = customtkinter.CTkLabel(master=self.level, text="Current Classes: " + str(self.setupDir["numClasses"]))
    self.currentClasses.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    self.availableClasses = customtkinter.CTkLabel(master=self.level, text="Available Classes: " + str(10 -self.setupDir["numClasses"]))
    self.availableClasses.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    self.saveFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.saveFrame.grid(row=RowI, column=0, sticky="nsew", padx=10, pady=overallPadyInside)
    self.saveFrame.grid_columnconfigure((0, 1, 2), weight=1)

    RowI += 1

    self.saveSetup = customtkinter.CTkButton(master=self.saveFrame, text="Save Setup File", command=saveFile)
    self.saveSetup.grid(row=0, column=0, sticky="nsew", padx=10, pady=overallPadyOutside)

    self.loadSetup = customtkinter.CTkButton(master=self.saveFrame, text="Load Setup File", command=loadFile)
    self.loadSetup.grid(row=0, column=1, sticky="nsew", padx=10, pady=overallPadyOutside)

    self.reset = customtkinter.CTkButton(master=self.saveFrame, text="Reset StudySync", command=lambda: resetStudySync(self))
    self.reset.grid(row=0, column=2, sticky="nsew", padx=10, pady=overallPadyOutside)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    self.taskUpdateFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.taskUpdateFrame.grid(row=RowI, column=0, sticky="nsew", padx=10, pady=overallPadyInside)
    self.taskUpdateFrame.grid_columnconfigure((0, 1), weight=1)

    RowI += 1

    self.deleteAll = customtkinter.CTkButton(master=self.taskUpdateFrame, text="Delete All Tasks", command=lambda: deleteAllTasks(self))
    self.deleteAll.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.loadTasks = customtkinter.CTkButton(master=self.taskUpdateFrame, text="Load Tasks", command=lambda: loadTask(self))
    self.loadTasks.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    self.versionFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.versionFrame.grid(row=RowI, column=0, sticky="nsew", padx=10, pady=overallPadyInside)
    self.versionFrame.grid_columnconfigure((0, 1), weight=1)

    RowI += 1

    self.checkVersion = customtkinter.CTkButton(master=self.versionFrame, text="Check for Updates", command=lambda: checkVersion(self))
    self.checkVersion.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.version = customtkinter.CTkLabel(master=self.versionFrame, text="  Current Version: " + self.setupDir["version"] + "  ")
    self.version.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    self.docFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.docFrame.grid(row=RowI, column=0, sticky="nsew", padx=10, pady=overallPadyInside)
    self.docFrame.grid_columnconfigure((0), weight=1)

    RowI += 1

    self.openDoc = customtkinter.CTkButton(master=self.docFrame, text="Open Documentation", command=lambda: openDoc())
    self.openDoc.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    

def changeAppearanceMode(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)

    with open("setup.json", "r") as f:
        setupDir = json.load(f)

    setupDir["mode"] = new_appearance_mode
    with open("setup.json", "w") as f:
        json.dump(setupDir, f, indent=4)


def changeTheme(new_theme: str):
    with open("setup.json", "r") as f:
        setupDir = json.load(f)

    setupDir["theme"] = new_theme
    with open("setup.json", "w") as f:
        json.dump(setupDir, f, indent=4)

    messagebox.showinfo("Success", "Theme Changed!\nRestart StudySync for changes to take effect.")


def deleteClass(self, className: str):
    question = pause()

    if question == True:
        with open("setup.json", "r") as f:
            setupDir = json.load(f)

        if setupDir["numClasses"] == 1:
            messagebox.showerror("Error", "Cannot delete last class!")

        else:
            for i in range(setupDir["numClasses"]):
                if setupDir[f"class{i+1}"]["name"] == className:
                    deleteNum = i + 1
                    del setupDir[f"class{i+1}"]

            for i in range(deleteNum, setupDir["numClasses"]):
                tempClass = setupDir[f"class{i+1}"]
                setupDir[f"class{i}"] = tempClass
                del setupDir[f"class{i+1}"]

            setupDir["numClasses"] -= 1
            with open("setup.json", "w") as f:
                json.dump(setupDir, f, indent=4)

            messagebox.showinfo("Success", "Class Deleted!")

def editClassSave(self, newClassName: str):
    classAddEdit(self, "edit", newClassName)

def saveFile():
    file_path = filedialog.asksaveasfilename(filetypes=(("JSON Files", "*.json"), ("All Files", "*.*")), typevariable=customtkinter.StringVar(value="setup"))  # Use askopenfilenames() for multiple files
    #file_path = filedialog.asksaveasfilename()

    if file_path:
        current = os.getcwd()
        shutil.copyfile(f"{current}/setup.json", f"{file_path}.json")

def loadFile():
    file_path = filedialog.askopenfilename(filetypes=(("JSON Files", "*.json"), ("All Files", "*.*")))

    with open(file_path, "r") as f:
        setupDir = json.load(f)

    try:
        if setupDir["setupComplete"] == False or setupDir["setupComplete"] == None:
            messagebox.showwarning(title="Error", message="Not a valid setup file")

        else:
            numClass = setupDir["numClasses"]
            mode = setupDir["mode"]
            theme = setupDir["theme"]
            progress = setupDir["progress"]
            level = setupDir["level"]
            version = setupDir["version"]
            beta = setupDir["betaUser"]

            for i in range(numClass):
                id = setupDir[f"class{i+1}"]["id"]
                name = setupDir[f"class{i+1}"]["name"]
                teacher = setupDir[f"class{i+1}"]["teacher"]
                subject = setupDir[f"class{i+1}"]["subject"]
                color = setupDir[f"class{i+1}"]["color"]
                icon =  setupDir[f"class{i+1}"]["icon"]

            with open("setup.json", "w") as f:
                json.dump(setupDir, f, indent=4)
            messagebox.showinfo(title="Success", message="Setup file loaded!")

    except KeyError:
        messagebox.showerror(title="Error", message="\tNot a valid setup file file\n\tPlease select a valid setup file\n\tOld setup file is still in use.")

def checkVersion(self):
    userVersion = getUserVersion()
    version = getMainVersion()

    if version == userVersion:
        messagebox.showinfo(title="Success", message="StudySync is up to date!")
    else:
        self.checkVersion.configure(text="Update StudySync", command=lambda: updateStudySync(self))
        messagebox.showwarning(title="Warning", message='StudySync is not up to date!\nClick the "Update StudySync" button to update.\nMakse sure you save current tasks and setup file before updating!')


def updateStudySync(self):
    webbrowser.open("https://github.com/Mason-Dino/StudySync/releases/latest")

def addClass(self):
    with open("setup.json", "r") as f:
        setupDir = json.load(f)

    if setupDir["numClasses"] == 10:
        messagebox.showerror("Error", "Cannot add more than 10 classes!")

    else:
        classAddEdit(self, "add")

def turnOff(self):
    pageSwitch = [self.homeSwitch, self.classSwitch, self.importSwitch, self.dueSwitch, self.taskSwitch]

    for page in pageSwitch:
        page.deselect()

def turnOn(self):
    #self.homeSwitch.select()
    pageSwitch = [self.homeSwitch, self.classSwitch, self.importSwitch, self.dueSwitch, self.taskSwitch]

    for page in pageSwitch:
        page.select()

def updateTabs(self):
    with open("setup.json", "r") as f:
        setupDir = json.load(f)

    pageSwitch = [self.homeSwitch, self.classSwitch, self.taskSwitch, self.dueSwitch, self.importSwitch]
    name = ["home", "class", "task", "due", "important"]
    value = []

    for page in pageSwitch:
        value.append(page.get())

    for i in range(5):
        if value[i] == 1:
            setupDir["tabs"][name[i]] = True

        else:
            setupDir["tabs"][name[i]] = False

    with open("setup.json", "w") as f:
        json.dump(setupDir, f, indent=4)

    messagebox.showinfo("Success", "Tabs updated!\nRestart StudySync to apply changes.")

def resetStudySync(self):
    question = pause()

    if question == True:
        with open("setup.json", "r") as f:
            setupDir = json.load(f)

        setupDir["setupComplete"] = False

        with open("setup.json", "w") as f:
            json.dump(setupDir, f, indent=4)

        os.remove("study.db")

        messagebox.showinfo("Success", "StudySync has been reset!\nRestart StudySync to apply changes.")

def deleteAllTasks(self):
    question = pause()
    if question == True:
        deleteDatabase()

        messagebox.showinfo("Success", "All tasks have been deleted!")

def loadTask(self):
    print("hey")

    if os.path.exists("study.db"):
        os.remove("study.db")
    
    file_path = filedialog.askopenfilename(filetypes=(("Data Base Files", "*.db"), ("All Files", "*.*")))

    current = os.getcwd()
    shutil.copyfile(f"{file_path}", f"{current}/study.db")

    makeTestTask()

def openDoc():
    webbrowser.open("https://dino-dev.gitbook.io/studysync")

def pause():
    yesno = messagebox.askyesno("StudySunc", "Are you sure you want to continue?")
    
    #no = False
    #yes = True

    return yesno