from tkinter import messagebox
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
    if calAnswer == "same":
        with open("setup.json", "r") as f:
            setup = json.load(f)

        pass

    elif calAnswer == "different":
        with open("setup.json", "r") as f:
            setup = json.load(f)

        pass