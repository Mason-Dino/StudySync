import customtkinter

from themes.theme import *

def importance(self):
    padyLevel = 5
    padxLevel = 3

    self.content = customtkinter.CTkScrollableFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure((0), weight=1)

    self.level1 = customtkinter.CTkFrame(master=self.content, fg_color=topLevel(), corner_radius=6)
    self.level1.grid(row=0, column=0, sticky="nsew", pady=padyLevel, padx=padxLevel)

    self.level2 = customtkinter.CTkFrame(master=self.content, fg_color=topLevel(), corner_radius=6)
    self.level2.grid(row=1, column=0, sticky="nsew", pady=padyLevel, padx=padxLevel)

    self.level3 = customtkinter.CTkFrame(master=self.content, fg_color=topLevel(), corner_radius=6)
    self.level3.grid(row=2, column=0, sticky="nsew", pady=padyLevel, padx=padxLevel)

    self.level4 = customtkinter.CTkFrame(master=self.content, fg_color=topLevel(), corner_radius=6)
    self.level4.grid(row=3, column=0, sticky="nsew", pady=padyLevel, padx=padxLevel)

    self.level5 = customtkinter.CTkFrame(master=self.content, fg_color=topLevel(), corner_radius=6)
    self.level5.grid(row=4, column=0, sticky="nsew", pady=padyLevel, padx=padxLevel)
