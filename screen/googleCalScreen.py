from themes.theme import *
from googleCal import *
import customtkinter

def googleCalSetup(self):
    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure((0), weight=1)

    self.header = customtkinter.CTkLabel(master=self.content, text="Google Calendar Setup", font=customtkinter.CTkFont(size=20, weight="bold"))
    self.header.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.question = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.question.grid(row=1, column=0, sticky="nsew", pady=10, padx=10)
    self.question.grid_columnconfigure((0), weight=1)


    self.questionLabel = customtkinter.CTkLabel(master=self.question, text="Do you want all tasks to be under the same calendar or different?", font=customtkinter.CTkFont(size=15))
    self.questionLabel.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)


    self.answer = customtkinter.CTkFrame(master=self.question, corner_radius=6, fg_color=topLevel())
    self.answer.grid(row=2, column=0, sticky="nsew")
    self.answer.grid_columnconfigure((0,1), weight=1)

    self.calAnswer = customtkinter.StringVar(value="none")

    self.same = customtkinter.CTkRadioButton(master=self.answer, text="Same Calendar", value="same", variable=self.calAnswer)
    self.same.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.different = customtkinter.CTkRadioButton(master=self.answer, text="Different Calendar", value="different", variable=self.calAnswer)
    self.different.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    self.continueOn = customtkinter.CTkButton(master=self.question, text="Continue", command=lambda: continueButton(self, self.calAnswer.get()))
    self.continueOn.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

def continueButton(self, answer):
    if answer == "same":
        self.setupFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6)
        self.setupFrame.grid(row=4, column=1, sticky="nsew", padx=10, pady=10)

    elif answer == "different":
        self.setupFrame = customtkinter.CTkScrollableFrame(master=self.content, corner_radius=6)
        self.setupFrame.grid(row=4, column=1, sticky="nsew", padx=10, pady=10)