from themes.theme import *
from integration.googleCal import *
import customtkinter
from tabs.home import home

from tkinter import messagebox, filedialog
import webbrowser

def googleCalSetup(self):
    self.content2 = customtkinter.CTkFrame(master=self)
    self.content2.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content2.grid_columnconfigure((0), weight=1)

    self.header = customtkinter.CTkLabel(master=self.content2, text="Google Calendar Setup", font=customtkinter.CTkFont(size=20, weight="bold"))
    self.header.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.question = customtkinter.CTkFrame(master=self.content2, corner_radius=6, fg_color=topLevel())
    self.question.grid(row=1, column=0, sticky="nsew", pady=5, padx=10)
    self.question.grid_columnconfigure((0), weight=1)

    self.questionLabel = customtkinter.CTkLabel(master=self.question, text="Click the docs button below to setup your Google Calendar", font=customtkinter.CTkFont(size=15))
    self.questionLabel.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.docsButton = customtkinter.CTkButton(master=self.question, text="Docs", command=lambda: webbrowser.open("https://dino-dev.gitbook.io/studysync/settings/google-calendar-setup"))
    self.docsButton.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    self.questionLabel2 = customtkinter.CTkLabel(master=self.question, text="Once done import your cred file", font=customtkinter.CTkFont(size=15))
    self.questionLabel2.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

    self.importCredButton = customtkinter.CTkButton(master=self.question, text="Import Cred File", command=lambda: importCredFile(self))
    self.importCredButton.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

    self.content2.grid_columnconfigure((0), weight=1)
    self.content2.grid_rowconfigure((4), weight=1)

    self.content = customtkinter.CTkFrame(master=self)
    #self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure((0), weight=1)
    self.content.grid_rowconfigure((4), weight=1)

    self.header = customtkinter.CTkLabel(master=self.content, text="Google Calendar Setup", font=customtkinter.CTkFont(size=20, weight="bold"))
    self.header.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.question = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.question.grid(row=1, column=0, sticky="nsew", pady=5, padx=10)
    self.question.grid_columnconfigure((0), weight=1)

    self.questionLabel = customtkinter.CTkLabel(master=self.question, text="Do you want all tasks to be under the same calendar or different?", font=customtkinter.CTkFont(size=15))
    self.questionLabel.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.answer = customtkinter.CTkFrame(master=self.question, corner_radius=6, fg_color=topLevel())
    self.answer.grid(row=2, column=0, sticky="nsew")
    self.answer.grid_columnconfigure((0,1), weight=1)

    self.calAnswer = customtkinter.StringVar(value="none")
    with open("setup.json", "r") as f:
        setup = json.load(f)

    theme = setup["theme"]

    radio = getRadioInfo(theme=theme)
    
    self.same = customtkinter.CTkRadioButton(master=self.answer, text="Same Calendar", value="same", variable=self.calAnswer,
                                            corner_radius=radio["corner_radius"], border_width_unchecked=radio["border_width_unchecked"], border_width_checked=radio["border_width_checked"],
                                            fg_color=radio["fg_color"], hover_color=radio["hover_color"], border_color=radio["border_color"],
                                            text_color=radio["text_color"], text_color_disabled=radio["text_color_disabled"])
    self.same.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.different = customtkinter.CTkRadioButton(master=self.answer, text="Different Calendar", value="different", variable=self.calAnswer,
                                                corner_radius=radio["corner_radius"], border_width_unchecked=radio["border_width_unchecked"], border_width_checked=radio["border_width_checked"],
                                                fg_color=radio["fg_color"], hover_color=radio["hover_color"], border_color=radio["border_color"],
                                                text_color=radio["text_color"], text_color_disabled=radio["text_color_disabled"])
    self.different.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    self.continueOn = customtkinter.CTkButton(master=self.question, text="Continue", command=lambda: continueButton(self, self.calAnswer.get()))
    self.continueOn.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

def continueButton(self, answer):
    self.different.configure(state="disabled")
    self.same.configure(state="disabled")

    if answer == "same":
        self.setupFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
        self.setupFrame.grid(row=4, column=0, sticky="nsew", padx=10, pady=5)

        self.calInfoFrame = customtkinter.CTkFrame(master=self.setupFrame, corner_radius=6, fg_color=topLevel())
        self.calInfoFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.calInfoFrame.grid_columnconfigure((0), weight=1)
        self.calInfoFrame.grid_rowconfigure((0,1), weight=1)

        self.className = customtkinter.CTkLabel(master=self.calInfoFrame, text="Calendar:", font=customtkinter.CTkFont(size=15))
        self.className.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.calID = customtkinter.CTkEntry(master=self.calInfoFrame, placeholder_text="Calendar ID")
        self.calID.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)


    elif answer == "different":
        self.setupFrame = customtkinter.CTkScrollableFrame(master=self.content, corner_radius=6, fg_color=topLevel())
        self.setupFrame.grid(row=4, column=0, sticky="nsew", padx=10, pady=5)
        self.setupFrame.grid_columnconfigure((0,1), weight=1)

        self.classNames = customtkinter.CTkFrame(master=self.setupFrame, corner_radius=6, fg_color=topLevel())
        self.classNames.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.classNames.grid_columnconfigure((0), weight=1)

        self.calInput = customtkinter.CTkFrame(master=self.setupFrame, corner_radius=6, fg_color=topLevel())
        self.calInput.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.calInput.grid_columnconfigure((0), weight=1)

        with open("setup.json", "r") as f:
            setup = json.load(f)

        numClasses = setup["numClasses"]

        self.calClass = {}

        # Need to add in a none class calendar option for users

        self.calClass[0] = {}

        self.className = customtkinter.CTkLabel(master=self.classNames, text="None:", font=customtkinter.CTkFont(size=15))
        self.className.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.calClass[0]["id"] = "0000000000"

        self.calClass[0]["input"] = customtkinter.CTkEntry(master=self.calInput, placeholder_text="Calendar ID")
        self.calClass[0]["input"].grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        for i in range(numClasses):
            self.className = customtkinter.CTkLabel(master=self.classNames, text=f"{setup[f'class{i+1}']['name']}:", font=customtkinter.CTkFont(size=15))
            self.className.grid(row=i+1, column=0, sticky="nsew", padx=10, pady=10)

            self.calClass[i+1] = {}

            self.calClass[i+1]["id"] = setup[f"class{i+1}"]["id"]

            self.calClass[i+1]["input"] = customtkinter.CTkEntry(master=self.calInput, placeholder_text="Calendar ID")
            self.calClass[i+1]["input"].grid(row=i+1, column=0, sticky="nsew", padx=10, pady=10)

    self.continueOn.destroy()

    self.controlButtons = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.controlButtons.grid(row=5, column=0, sticky="nsew", padx=10, pady=5)
    self.controlButtons.grid_columnconfigure((0,1), weight=1)

    self.setupButton = customtkinter.CTkButton(master=self.controlButtons, text="Setup", command=lambda: setupButton(self, answer))
    self.setupButton.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.docButton = customtkinter.CTkButton(master=self.controlButtons, text="Documentation", command=lambda: webbrowser.open("https://dino-dev.gitbook.io/studysync/settings/google-calendar-setup"))
    self.docButton.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

def googleCalEdit(self):
    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure((0), weight=1)

    self.header = customtkinter.CTkLabel(master=self.content, text="Google Calendar Edit", font=customtkinter.CTkFont(size=20, weight="bold"))
    self.header.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.resetFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.resetFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
    self.resetFrame.grid_columnconfigure((0,1), weight=1)

    self.resetButton = customtkinter.CTkButton(master=self.resetFrame, text="Reset Setup", command=lambda: resetButton(self))
    self.resetButton.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.importNewFile = customtkinter.CTkButton(master=self.resetFrame, text="Import New File", command=lambda: print("importNewFile"))
    self.importNewFile.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    self.docButton = customtkinter.CTkButton(master=self.resetFrame, text="Documentation", command=lambda: webbrowser.open("https://dino-dev.gitbook.io/studysync/settings/google-calendar-setup"))
    self.docButton.grid(row=1, column=0,  columnspan=2, sticky="nsew", padx=10, pady=10)

    self.option = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.option.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
    self.option.grid_columnconfigure((0,1), weight=1)

    self.calAnswer = customtkinter.StringVar(value="none")
    with open("setup.json", "r") as f:
        setup = json.load(f)

    theme = setup["theme"]

    radio = getRadioInfo(theme=theme)
    
    self.same = customtkinter.CTkRadioButton(master=self.option, text="Same Calendar", value="same", variable=self.calAnswer,
                                            corner_radius=radio["corner_radius"], border_width_unchecked=radio["border_width_unchecked"], border_width_checked=radio["border_width_checked"],
                                            fg_color=radio["fg_color"], hover_color=radio["hover_color"], border_color=radio["border_color"],
                                            text_color=radio["text_color"], text_color_disabled=radio["text_color_disabled"])
    self.same.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.different = customtkinter.CTkRadioButton(master=self.option, text="Different Calendars", value="different", variable=self.calAnswer,
                                                corner_radius=radio["corner_radius"], border_width_unchecked=radio["border_width_unchecked"], border_width_checked=radio["border_width_checked"],
                                                fg_color=radio["fg_color"], hover_color=radio["hover_color"], border_color=radio["border_color"],
                                                text_color=radio["text_color"], text_color_disabled=radio["text_color_disabled"])
    self.different.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    self.continueButton = customtkinter.CTkButton(master=self.option, text="Continue", command=lambda: continueEdit(self, answer=self.calAnswer.get()))
    self.continueButton.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

def setupButton(self, answer):
    with open("setup.json", "r") as f:
        setup = json.load(f)

    setup["calendar"] = {}
    numClasses = setup["numClasses"]
    errorList = []

    if answer == "same":
        setup["calendar"]["type"] = "same"
        for i in range(numClasses):
            classID = setup[f"class{i+1}"]["id"]
            setup[f"calendar"][classID] = self.calID.get()

            error = testEvent(self.calID.get())
            errorList.append(error)

        setup["calendar"]["0000000000"] = self.calID.get()

        error = testEvent(self.calID.get())
        errorList.append(error)

        if True in errorList:
            messagebox.showerror("Error", "Invalid Calendar ID")

        else:
            setup["googleCal"] = True

            with open("setup.json", "w") as f:
                json.dump(setup, f, indent=4)

            messagebox.showinfo("Success", "Google Calendar Setup!")

    elif answer == "different":
        setup["calendar"]["type"] = "different"
        numClasses = setup["numClasses"]

        for i in range(numClasses):
            classID = setup[f"class{i+1}"]["id"]
            setup[f"calendar"][classID] = self.calClass[i+1]["input"].get()

            error = testEvent(self.calClass[i+1]["input"].get())
            errorList.append(error)

        setup["calendar"]["0000000000"] = self.calClass[0]["input"].get()

        error = testEvent(self.calClass[0]["input"].get())
        errorList.append(error)

        if True in errorList:
            messagebox.showerror("Error", "Invalid Calendar ID")

        else:
            setup["googleCal"] = True

            with open("setup.json", "w") as f:
                json.dump(setup, f, indent=4)

            messagebox.showinfo("Success", "Google Calendar Setup!")

    if True in errorList:
        pass

    else:
        home(self)

def resetButton(self):
    warning = messagebox.askyesno("Warning", "Are you sure you want to reset the Google Calendar?\nNo Events will be deleted.")

    if warning == True:
        with open("setup.json", "r") as f:
            setup = json.load(f)

        setup["calendar"] = {}
        setup["googleCal"] = False

        with open("setup.json", "w") as f:
            json.dump(setup, f, indent=4)

        os.remove("creds.json")
        os.remove("token.json")

        messagebox.showinfo("Success", "Google Calendar Reset!\nGo back into settings to re-setup. ")

        home(self)

    else:
        pass

def importCredFile(self):
    file = filedialog.askopenfile(mode='r', filetypes=[('JSON Files', '*.json')])

    if file is not None:
        print(file.name)
        print(type(file))
        with open(file.name, "r") as f:
            cred = json.load(f)

        try:
            cred["installed"]["client_id"]
            cred["installed"]["client_secret"]
            cred["installed"]["project_id"]
            cred["installed"]["auth_uri"]
            cred["installed"]["token_uri"]
            cred["installed"]["auth_provider_x509_cert_url"]
            cred["installed"]["redirect_uris"]
            error = False

        except:
            error = True
            messagebox.showerror("Error", "Invalid Cred File")

        if error == False:
            print(cred)

            with open("creds.json",  "w") as f:
                json.dump(cred, f, indent=4)

            loadGooglCal()

            self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)

def continueEdit(self, answer):
    self.continueButton.destroy()
    self.different.configure(state="disabled")
    self.same.configure(state="disabled")
    self.content.grid_rowconfigure((4), weight=1)
    self.resetFrame.destroy()

    with open("setup.json", "r") as f:
        setup = json.load(f)

    pType = setup["calendar"]["type"]

    if answer == "different":
        self.setupFrame = customtkinter.CTkScrollableFrame(master=self.content, corner_radius=6, fg_color=topLevel())
        self.setupFrame.grid(row=4, column=0, sticky="nsew", padx=10, pady=5)
        self.setupFrame.grid_columnconfigure((0,1), weight=1)

        self.classNames = customtkinter.CTkFrame(master=self.setupFrame, corner_radius=6, fg_color=topLevel())
        self.classNames.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.classNames.grid_columnconfigure((0), weight=1)

        self.calInput = customtkinter.CTkFrame(master=self.setupFrame, corner_radius=6, fg_color=topLevel())
        self.calInput.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.calInput.grid_columnconfigure((0), weight=1)

        with open("setup.json", "r") as f:
            setup = json.load(f)

        numClasses = setup["numClasses"]

        self.calClass = {}

        # Need to add in a none class calendar option for users

        self.calClass[0] = {}

        self.className = customtkinter.CTkLabel(master=self.classNames, text="None:", font=customtkinter.CTkFont(size=15))
        self.className.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.calClass[0]["id"] = "0000000000"

        self.calClass[0]["input"] = customtkinter.CTkEntry(master=self.calInput, placeholder_text="Calendar ID")
        self.calClass[0]["input"].grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        if pType == "different":
            try:
                self.calClass[0]["input"].insert(0, setup["calendar"]["0000000000"])

            except:
                pass

        for i in range(numClasses):
            self.className = customtkinter.CTkLabel(master=self.classNames, text=f"{setup[f'class{i+1}']['name']}:", font=customtkinter.CTkFont(size=15))
            self.className.grid(row=i+1, column=0, sticky="nsew", padx=10, pady=10)

            self.calClass[i+1] = {}

            self.calClass[i+1]["id"] = setup[f"class{i+1}"]["id"]

            self.calClass[i+1]["input"] = customtkinter.CTkEntry(master=self.calInput, placeholder_text="Calendar ID")
            self.calClass[i+1]["input"].grid(row=i+1, column=0, sticky="nsew", padx=10, pady=10)

            if pType == "different":
                try:
                    self.calClass[i+1]["input"].insert(0, setup["calendar"][self.calClass[i+1]["id"]])

                except:
                    pass

    if answer == "same":
        self.setupFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
        self.setupFrame.grid(row=4, column=0, sticky="nsew", padx=10, pady=5)

        self.calInfoFrame = customtkinter.CTkFrame(master=self.setupFrame, corner_radius=6, fg_color=topLevel())
        self.calInfoFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.calInfoFrame.grid_columnconfigure((0), weight=1)
        self.calInfoFrame.grid_rowconfigure((0,1), weight=1)

        self.className = customtkinter.CTkLabel(master=self.calInfoFrame, text="Calendar:", font=customtkinter.CTkFont(size=15))
        self.className.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.calID = customtkinter.CTkEntry(master=self.calInfoFrame, placeholder_text="Calendar ID")
        self.calID.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        if pType == "same":
            try:
                self.calID.insert(0, setup["calendar"]["0000000000"])

            except:
                pass

    self.controlFame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.controlFame.grid(row=5, column=0, sticky="nsew", padx=10, pady=5)
    self.controlFame.grid_columnconfigure((0,1), weight=1)

    self.update = customtkinter.CTkButton(master=self.controlFame, text="Update", command=lambda: updateEdit(self, answer))
    self.update.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.cancel = customtkinter.CTkButton(master=self.controlFame, text="Cancel", command=lambda: home(self))
    self.cancel.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

def updateEdit(self, answer):
    with open("setup.json", "r") as f:
        setup = json.load(f)

    setup["calendar"] = {}
    numClasses = setup["numClasses"]
    errorList = []

    if answer == "same":
        setup["calendar"]["type"] = "same"
        for i in range(numClasses):
            classID = setup[f"class{i+1}"]["id"]
            setup[f"calendar"][classID] = self.calID.get()

            error = testEvent(self.calID.get())
            errorList.append(error)

        setup["calendar"]["0000000000"] = self.calID.get()

        error = testEvent(self.calID.get())
        errorList.append(error)

        if True in errorList:
            messagebox.showerror("Error", "Invalid Calendar ID")

        else:
            setup["googleCal"] = True

            with open("setup.json", "w") as f:
                json.dump(setup, f, indent=4)

            messagebox.showinfo("Success", "Google Calendar Updated!")

            home(self)

    elif answer == "different":
        setup["calendar"]["type"] = "different"
        numClasses = setup["numClasses"]

        for i in range(numClasses):
            classID = setup[f"class{i+1}"]["id"]
            setup[f"calendar"][classID] = self.calClass[i+1]["input"].get()

            error = testEvent(self.calClass[i+1]["input"].get())
            errorList.append(error)

        setup["calendar"]["0000000000"] = self.calClass[0]["input"].get()

        error = testEvent(self.calClass[0]["input"].get())
        errorList.append(error)

        if True in errorList:
            messagebox.showerror("Error", "Invalid Calendar ID")

        else:
            setup["googleCal"] = True

            with open("setup.json", "w") as f:
                json.dump(setup, f, indent=4)

            messagebox.showinfo("Success", "Google Calendar Updated!")

            home(self)