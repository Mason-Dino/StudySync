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

    self.doneToken = customtkinter.CTkButton(master=self.question, text="Done", command=lambda: print("doneToken"))
    self.doneToken.grid(row=4, column=0, sticky="nsew", padx=10, pady=10)

def todoistEdit(self):
    self.content = customtkinter.CTkFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)