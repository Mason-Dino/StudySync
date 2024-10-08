from turtle import width
from unittest import result
from integration.todoist import *
from tkinter import messagebox
from tabs.home import home
from themes.theme import *
import customtkinter
import webbrowser

def todoistSetup(self):
    self.content = customtkinter.CTkFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure((0), weight=1)

    self.header = customtkinter.CTkLabel(master=self.content, text="Todoist Setup", font=customtkinter.CTkFont(size=20, weight="bold"))
    self.header.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.question = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.question.grid(row=1, column=0, sticky="nsew", pady=5, padx=10)
    self.question.grid_columnconfigure((0), weight=1)

    self.questionLabel = customtkinter.CTkLabel(master=self.question, text="Click the docs button below to setup Todoist", font=customtkinter.CTkFont(size=15))
    self.questionLabel.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.docsButton = customtkinter.CTkButton(master=self.question, text="Docs", command=lambda: webbrowser.open("https://dino-dev.gitbook.io/studysync/settings/todoist-setup"))
    self.docsButton.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    self.questionLabel2 = customtkinter.CTkLabel(master=self.question, text="Once done paste in your token", font=customtkinter.CTkFont(size=15))
    self.questionLabel2.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

    self.tokenEntry = customtkinter.CTkEntry(master=self.question, placeholder_text="Token")
    self.tokenEntry.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

    self.doneToken = customtkinter.CTkButton(master=self.question, text="Done", command=lambda: doneToken(self))
    self.doneToken.grid(row=4, column=0, sticky="nsew", padx=10, pady=10)

def todoistEdit(self):
    self.content = customtkinter.CTkFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure((0), weight=1)

    self.header = customtkinter.CTkLabel(master=self.content, text="Todoist Edit", font=customtkinter.CTkFont(size=20, weight="bold"))
    self.header.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.buttonControl = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.buttonControl.grid(row=1, column=0, sticky="nsew", pady=5, padx=10)
    self.buttonControl.grid_columnconfigure((0,1), weight=1)

    self.resetButton = customtkinter.CTkButton(master=self.buttonControl, text="Reset Setup", command=lambda: reset(self))
    self.resetButton.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.docButton = customtkinter.CTkButton(master=self.buttonControl, text="Documentation", command=lambda: webbrowser.open("https://dino-dev.gitbook.io/studysync/settings/todoist-setup"))
    self.docButton.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    self.question = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.question.grid(row=2, column=0, sticky="nsew", pady=5, padx=10)
    self.question.grid_columnconfigure((0,1), weight=1)

    self.calAnswer = customtkinter.StringVar(value="none")
    with open("setup.json", "r") as f:
        setup = json.load(f)

    theme = setup["theme"]

    radio = getRadioInfo(theme=theme)
    
    self.same = customtkinter.CTkRadioButton(master=self.question, text="Same", value="same", variable=self.calAnswer,
                                            corner_radius=radio["corner_radius"], border_width_unchecked=radio["border_width_unchecked"], border_width_checked=radio["border_width_checked"],
                                            fg_color=radio["fg_color"], hover_color=radio["hover_color"], border_color=radio["border_color"],
                                            text_color=radio["text_color"], text_color_disabled=radio["text_color_disabled"])
    self.same.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.different = customtkinter.CTkRadioButton(master=self.question, text="Different", value="different", variable=self.calAnswer,
                                                corner_radius=radio["corner_radius"], border_width_unchecked=radio["border_width_unchecked"], border_width_checked=radio["border_width_checked"],
                                                fg_color=radio["fg_color"], hover_color=radio["hover_color"], border_color=radio["border_color"],
                                                text_color=radio["text_color"], text_color_disabled=radio["text_color_disabled"])
    self.different.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    self.continueButton = customtkinter.CTkButton(master=self.question, text="Continue", command=lambda: continueEdit(self, self.calAnswer.get()))
    self.continueButton.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

def doneToken(self):
    todoistToken = self.tokenEntry.get()

    if todoistToken == "":
        messagebox.showerror("Error", "Please enter a token")

    else:
        with open("setup.json", "r") as f:
            setupDir = json.load(f)

        setupDir["todoist"] = {}

        setupDir["todoist"]["token"] = todoistToken
        with open("setup.json",  "w") as f:
                json.dump(setupDir, f, indent=4)

        self.content = customtkinter.CTkFrame(master=self, corner_radius=6)
        self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
        self.content.grid_columnconfigure((0), weight=1)

        self.header = customtkinter.CTkLabel(master=self.content, text="Todoist Setup", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.header.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.question = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
        self.question.grid(row=1, column=0, sticky="nsew", pady=5, padx=10)
        self.question.grid_columnconfigure((0,1), weight=1)

        self.questionLabel = customtkinter.CTkLabel(master=self.question, text="Do you want all the tasks to be in one location or separate?", font=customtkinter.CTkFont(size=15))
        self.questionLabel.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        self.calAnswer = customtkinter.StringVar(value="none")
        with open("setup.json", "r") as f:
            setup = json.load(f)

        theme = setup["theme"]

        radio = getRadioInfo(theme=theme)
        
        self.same = customtkinter.CTkRadioButton(master=self.question, text="Same", value="same", variable=self.calAnswer,
                                                corner_radius=radio["corner_radius"], border_width_unchecked=radio["border_width_unchecked"], border_width_checked=radio["border_width_checked"],
                                                fg_color=radio["fg_color"], hover_color=radio["hover_color"], border_color=radio["border_color"],
                                                text_color=radio["text_color"], text_color_disabled=radio["text_color_disabled"])
        self.same.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.different = customtkinter.CTkRadioButton(master=self.question, text="Different", value="different", variable=self.calAnswer,
                                                    corner_radius=radio["corner_radius"], border_width_unchecked=radio["border_width_unchecked"], border_width_checked=radio["border_width_checked"],
                                                    fg_color=radio["fg_color"], hover_color=radio["hover_color"], border_color=radio["border_color"],
                                                    text_color=radio["text_color"], text_color_disabled=radio["text_color_disabled"])
        self.different.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        self.continueButton = customtkinter.CTkButton(master=self.question, text="Continue", command=lambda: continueButton(self, self.calAnswer.get()))
        self.continueButton.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

def continueButton(self, calAnswer):
    self.todoistDIR = {}
    print(calAnswer)

    if calAnswer == "same":
        with open("setup.json", "r") as f:
            setup = json.load(f)

        self.continueButton.destroy()
        self.different.configure(state="disabled")
        self.same.configure(state="disabled")
        self.content.grid_rowconfigure((4), weight=1)
        self.questionLabel.destroy()

        self.setupFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
        self.setupFrame.grid(row=4, column=0, sticky="nsew", padx=10, pady=5)

        self.centerFrame = customtkinter.CTkFrame(master=self.setupFrame, corner_radius=6, fg_color=topLevel(), width=200, height=100)
        self.centerFrame.place(relx=0.5, rely=0.5, anchor="center")

        self.label = customtkinter.CTkLabel(master=self.centerFrame, text="Project of Section ID", font=customtkinter.CTkFont(size=15))
        self.label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.entry = customtkinter.CTkEntry(master=self.centerFrame, placeholder_text="Project of Section ID")
        self.entry.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.controlButtons = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
        self.controlButtons.grid(row=5, column=0, sticky="nsew", padx=10, pady=5)
        self.controlButtons.grid_columnconfigure((0,1), weight=1)

        self.continueSame = customtkinter.CTkButton(master=self.controlButtons, text="Continue", command=lambda: setupFunction(self, "same"))
        self.continueSame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.cancel = customtkinter.CTkButton(master=self.controlButtons, text="Cancel", command=lambda: home(self))
        self.cancel.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        setup["todoist"]["type"] = "same"

        with open("setup.json", "w") as f:
            json.dump(setup, f, indent=4)

    elif calAnswer == "different":
        with open("setup.json", "r") as f:
            setup = json.load(f)

        className = []
        classID = []
        numClasses = setup["numClasses"]

        className.append("None")
        classID.append("0000000000")

        for i in range(numClasses):
            className.append(setup[f"class{i+1}"]["name"])
            classID.append(setup[f"class{i+1}"]["id"])

        self.continueButton.destroy()
        self.different.configure(state="disabled")
        self.same.configure(state="disabled")
        self.content.grid_rowconfigure((4), weight=1)
        self.questionLabel.destroy()

        self.setupFrame = customtkinter.CTkScrollableFrame(master=self.content, corner_radius=6, fg_color=topLevel())
        self.setupFrame.grid(row=4, column=0, sticky="nsew", padx=10, pady=5)
        self.setupFrame.grid_columnconfigure((0,1), weight=1)

        self.classNames = customtkinter.CTkFrame(master=self.setupFrame, corner_radius=6, fg_color=topLevel())
        self.classNames.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.classNames.grid_columnconfigure((0), weight=1)

        self.todoistInput = customtkinter.CTkFrame(master=self.setupFrame, corner_radius=6, fg_color=topLevel())
        self.todoistInput.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        for i in range(numClasses + 1):
            self.todoistDIR[classID[i]] = {}
            self.todoistDIR[classID[i]]["class id"] = classID[i]

            self.todoistDIR[classID[i]]["name"] = customtkinter.CTkLabel(master=self.classNames, text=className[i], font=customtkinter.CTkFont(size=15))
            self.todoistDIR[classID[i]]["name"].grid(row=i, column=0, sticky="nsew", padx=10, pady=10)

            self.todoistDIR[classID[i]]["id"] = customtkinter.CTkEntry(master=self.todoistInput, placeholder_text="Todoist ID")
            self.todoistDIR[classID[i]]["id"].grid(row=i, column=0, sticky="nsew", padx=10, pady=10)


        pass

        self.controlButtons = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
        self.controlButtons.grid(row=5, column=0, sticky="nsew", padx=10, pady=5)
        self.controlButtons.grid_columnconfigure((0,1), weight=1)

        self.continueButton = customtkinter.CTkButton(master=self.controlButtons, text="Setup", command=lambda: setupFunction(self, "different"))
        self.continueButton.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.cancelButton = customtkinter.CTkButton(master=self.controlButtons, text="Cancel", command=lambda: home(self))
        self.cancelButton.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        setup["todoist"]["type"] = "different"

        with open("setup.json", "w") as f:
            json.dump(setup, f, indent=4)

def setupFunction(self, type):
    #print(self.todoistDIR)

    with open("setup.json", "r") as f:
        setup = json.load(f)

    numClass = setup["numClasses"]

    classID = []

    classID.append("0000000000")

    for i in range(numClass):
        classID.append(setup[f"class{i+1}"]["id"])

    if type == "same":
        id = self.entry.get()
        numClasses = setup["numClasses"]

        error = False

        if id == "" or ProjectorSection(int(id)) == "None":
            error = True

        if error == False:
            result = ProjectorSection(int(id))

            for calID in classID:
                setup["todoist"][calID] = {}

                try:
                    setup["todoist"][calID]["id"] = int(id)
                    setup["todoist"][calID]["type"] = result

                except:
                    error = True
                    break

        if error == True:
            messagebox.showerror("Error", "Invalid Todoist ID\nDouble Check the ID and Try Again")

        elif error == False:
            setup["todoistSetup"] = True

            setupSyncFile()

            with open("setup.json", "w") as f:
                json.dump(setup, f, indent=4)

            messagebox.showinfo("Success", "Setup Complete")

    elif type == "different":
        error = False

        for i in range(numClass + 1):
            if self.todoistDIR[classID[i]]["id"].get() == "":
                error = True

        print(error)

        if error == False:
            for i in range(numClass + 1):
                setup["todoist"][classID[i]] = {}

                type = ProjectorSection(self.todoistDIR[classID[i]]["id"].get())

                if type != "None":
                    try:
                        setup["todoist"][classID[i]]["id"] = int(self.todoistDIR[classID[i]]["id"].get())
                        setup["todoist"][classID[i]]["type"] = type

                    except:
                        error = True
                        break

                elif type == "None":
                    error = True

                    break

            if error == False:
                setup["todoistSetup"] = True

                with open("setup.json", "w") as f:
                    json.dump(setup, f, indent=4)

                setupSyncFile()

                messagebox.showinfo("Success", "Setup Complete")
                home(self)

        if error == True:
            messagebox.showerror("Error", "An Error Occurred Please Try Again\nDouble Check that all ID's are correct")

def reset(self):
    result = messagebox.showerror(title="Error", message="Are you sure you want to reset?", type="yesno")

    if result == "yes":
        with open("setup.json", "r") as f:
            setup = json.load(f)

        setup["todoistSetup"] = False
        setup["todoist"] = {}

        with open("setup.json", "w") as f:
            json.dump(setup, f, indent=4)

        home(self)

    else:
        pass

def continueEdit(self, answer):
    with open("setup.json", "r") as f:
        setup = json.load(f)

    if answer == "same":
        with open("setup.json", "r") as f:
            setup = json.load(f)

        self.continueButton.destroy()
        self.different.configure(state="disabled")
        self.same.configure(state="disabled")
        self.content.grid_rowconfigure((4), weight=1)

        self.setupFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
        self.setupFrame.grid(row=4, column=0, sticky="nsew", padx=10, pady=5)

        self.centerFrame = customtkinter.CTkFrame(master=self.setupFrame, corner_radius=6, fg_color=topLevel(), width=200, height=100)
        self.centerFrame.place(relx=0.5, rely=0.5, anchor="center")

        self.label = customtkinter.CTkLabel(master=self.centerFrame, text="Project of Section ID", font=customtkinter.CTkFont(size=15))
        self.label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.entry = customtkinter.CTkEntry(master=self.centerFrame, placeholder_text="Project of Section ID")
        self.entry.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.controlButtons = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
        self.controlButtons.grid(row=5, column=0, sticky="nsew", padx=10, pady=5)
        self.controlButtons.grid_columnconfigure((0,1), weight=1)

        self.continueSame = customtkinter.CTkButton(master=self.controlButtons, text="Continue", command=lambda: setupFunction(self, "same"))
        self.continueSame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.cancel = customtkinter.CTkButton(master=self.controlButtons, text="Cancel", command=lambda: home(self))
        self.cancel.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        if setup["todoist"]["type"] == "same":
            self.entry.insert(0, setup["todoist"]["0000000000"]["id"])

        else:
            setup["todoist"]["type"] = "same"

            with open("setup.json", "w") as f:
                json.dump(setup, f, indent=4)

    elif answer == "different":
        className = []
        classID = []
        numClasses = setup["numClasses"]

        className.append("None")
        classID.append("0000000000")

        for i in range(numClasses):
            className.append(setup[f"class{i+1}"]["name"])
            classID.append(setup[f"class{i+1}"]["id"])

        self.continueButton.destroy()
        self.different.configure(state="disabled")
        self.same.configure(state="disabled")
        self.content.grid_rowconfigure((4), weight=1)

        self.setupFrame = customtkinter.CTkScrollableFrame(master=self.content, corner_radius=6, fg_color=topLevel())
        self.setupFrame.grid(row=4, column=0, sticky="nsew", padx=10, pady=5)
        self.setupFrame.grid_columnconfigure((0,1), weight=1)

        self.classNames = customtkinter.CTkFrame(master=self.setupFrame, corner_radius=6, fg_color=topLevel())
        self.classNames.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.classNames.grid_columnconfigure((0), weight=1)

        self.todoistInput = customtkinter.CTkFrame(master=self.setupFrame, corner_radius=6, fg_color=topLevel())
        self.todoistInput.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.todoistDIR = {}

        for i in range(numClasses + 1):
            self.todoistDIR[classID[i]] = {}
            self.todoistDIR[classID[i]]["class id"] = classID[i]

            self.todoistDIR[classID[i]]["name"] = customtkinter.CTkLabel(master=self.classNames, text=className[i], font=customtkinter.CTkFont(size=15))
            self.todoistDIR[classID[i]]["name"].grid(row=i, column=0, sticky="nsew", padx=10, pady=10)

            self.todoistDIR[classID[i]]["id"] = customtkinter.CTkEntry(master=self.todoistInput, placeholder_text="Todoist ID")
            self.todoistDIR[classID[i]]["id"].grid(row=i, column=0, sticky="nsew", padx=10, pady=10)

        self.controlButtons = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
        self.controlButtons.grid(row=5, column=0, sticky="nsew", padx=10, pady=5)
        self.controlButtons.grid_columnconfigure((0,1), weight=1)

        self.continueButton = customtkinter.CTkButton(master=self.controlButtons, text="Setup", command=lambda: setupFunction(self, "different"))
        self.continueButton.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.cancelButton = customtkinter.CTkButton(master=self.controlButtons, text="Cancel", command=lambda: home(self))
        self.cancelButton.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)


        if setup["todoist"]["type"] == "different":
            print("hey")
            for i in range(len(classID)):
                try:
                    self.todoistDIR[classID[i]]["id"].insert(0, setup["todoist"][classID[i]]["id"])

                except:
                    pass

        else:
            setup["todoist"]["type"] = "different"

            with open("setup.json", "w") as f:
                json.dump(setup, f, indent=4)

def setupSyncFile():
    with open("studySync1.json", "r") as f:
        studySync = json.load(f)

    with open("studySync2.json", "r") as f:
        studySync2 = json.load(f)

    with open("setup.json", "r") as f:
        setup = json.load(f)
        
    classID = []
    className = []
    todoistID = []
    numClasses = setup["numClasses"]

    for i in range(numClasses):
        classID.append(setup[f"class{i+1}"]["id"])
        className.append(setup[f"class{i+1}"]["name"])
        todoistID.append(str(setup["todoist"][setup[f"class{i+1}"]["id"]]["id"]))

    todoistID.append(str(setup["todoist"]["0000000000"]["id"]))
    classID.append("0000000000")
    className.append("None")

    studySync["info"]["classID"] = classID
    studySync["info"]["className"] = className
    studySync["info"]["todoistID"] = todoistID

    studySync2["info"]["classID"] = classID
    studySync2["info"]["className"] = className
    studySync2["info"]["todoistID"] = todoistID

    for i in range(numClasses):
        try:
            studySync2[str(todoistID[i])]

        except:
            studySync2[str(todoistID[i])] = {}

    with open("studySync1.json", "w") as f:
        json.dump(studySync, f, indent=4)

    with open("studySync2.json", "w") as f:
        json.dump(studySync2, f, indent=4)

