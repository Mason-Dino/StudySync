import customtkinter

from themes.theme import topLevel


def assignments(self, taskName: str = None):
    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure((0), weight=1)

    self.overallTaskFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.overallTaskFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    self.overallTaskFrame.grid_columnconfigure((0), weight=1)

    self.taskNameFrame = customtkinter.CTkFrame(master=self.overallTaskFrame, fg_color="transparent")
    self.taskNameFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    self.taskNameFrame.grid_columnconfigure((0), weight=1)

    self.taskNameEntry = customtkinter.CTkEntry(master=self.taskNameFrame, placeholder_text="Task Name (max: 30)")
    self.taskNameEntry.grid(row=1, column=0,  sticky="nsew", padx=10, pady=0)

    self.classFrame = customtkinter.CTkFrame(master=self.overallTaskFrame, fg_color="transparent")
    self.classFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    self.classFrame.grid_columnconfigure((0), weight=1)

    self.classOption = customtkinter.CTkOptionMenu(master=self.classFrame, values=["Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7", "Class 8", "Class 9", "Class 10"],
                                                    variable=customtkinter.StringVar(value="Pick Class"))
    self.classOption.grid(row=0, column=0, sticky="nsew", padx=10, pady=0)

    self.dateFrame = customtkinter.CTkFrame(master=self.overallTaskFrame, fg_color="transparent")
    self.dateFrame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
    self.dateFrame.grid_columnconfigure((0,1,2), weight=1)

    self.day = customtkinter.CTkEntry(master=self.dateFrame, placeholder_text="Day")
    self.day.grid(row=0, column=0, sticky="nsew", padx=10, pady=0)

    self.month = customtkinter.CTkEntry(master=self.dateFrame, placeholder_text="Month")
    self.month.grid(row=0, column=1, sticky="nsew", padx=10, pady=0)

    self.year = customtkinter.CTkEntry(master=self.dateFrame, placeholder_text="Year")
    self.year.grid(row=0, column=2, sticky="nsew", padx=10, pady=0)

