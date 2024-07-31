import customtkinter

from themes.theme import topLevel


def assignments(self, taskName: str = None):
    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure((0), weight=1)
    self.content.grid_rowconfigure((0), weight=1)

    self.overallTaskFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.overallTaskFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    self.overallTaskFrame.grid_columnconfigure((0), weight=1)
    self.overallTaskFrame.grid_rowconfigure((0, 1,2,3,4), weight=1)

    self.taskNameFrame = customtkinter.CTkFrame(master=self.overallTaskFrame, fg_color="transparent")
    self.taskNameFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=7)
    self.taskNameFrame.grid_columnconfigure((0), weight=1)

    self.taskNameEntry = customtkinter.CTkEntry(master=self.taskNameFrame)
    self.taskNameEntry.grid(row=1, column=0,  sticky="nsew", padx=10, pady=0)

    if taskName is not None:
        self.taskNameEntry.configure(textvariable=customtkinter.StringVar(value=taskName))

    self.taskNameEntry.configure(placeholder_text="Task Name (max: 30)")

    self.classFrame = customtkinter.CTkFrame(master=self.overallTaskFrame, fg_color="transparent")
    self.classFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=7)
    self.classFrame.grid_columnconfigure((0), weight=1)

    self.classOption = customtkinter.CTkOptionMenu(master=self.classFrame, values=["Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7", "Class 8", "Class 9", "Class 10"],
                                                    variable=customtkinter.StringVar(value="Pick Class"))
    self.classOption.grid(row=0, column=0, sticky="nsew", padx=10, pady=0)

    self.dateFrame = customtkinter.CTkFrame(master=self.overallTaskFrame, fg_color="transparent")
    self.dateFrame.grid(row=2, column=0, sticky="nsew", padx=10, pady=7)
    self.dateFrame.grid_columnconfigure((0,1,2), weight=1)

    self.day = customtkinter.CTkEntry(master=self.dateFrame, placeholder_text="Day")
    self.day.grid(row=0, column=0, sticky="nsew", padx=10, pady=0)

    self.month = customtkinter.CTkEntry(master=self.dateFrame, placeholder_text="Month")
    self.month.grid(row=0, column=1, sticky="nsew", padx=10, pady=0)

    self.year = customtkinter.CTkEntry(master=self.dateFrame, placeholder_text="Year")
    self.year.grid(row=0, column=2, sticky="nsew", padx=10, pady=0)

    self.miniContent = customtkinter.CTkFrame(master=self.overallTaskFrame, fg_color="red")
    self.miniContent.grid(row=3, column=0, sticky="nsew", padx=10, pady=7)
    self.miniContent.grid_columnconfigure((0,1), weight=1)

    self.sideLeft = customtkinter.CTkFrame(master=self.miniContent, fg_color="green")
    self.sideLeft.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    self.sideLeft.grid_columnconfigure((0), weight=1)

    self.sideRight = customtkinter.CTkFrame(master=self.miniContent, fg_color="blue")
    self.sideRight.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    self.sideRight.grid_columnconfigure((0), weight=1)
    
    self.project = customtkinter.StringVar(value="project")

    self.testType = customtkinter.CTkRadioButton(master=self.sideRight, text="Test", variable=self.project, value="test")
    self.testType.grid(row=0, column=0, sticky="nsew", padx=10, pady=7)

    #self.quizType = customtkinter.CTkRadioButton(master=self.sideRight, text="Quiz", variable=self.project, value="quiz")
    #self.quizType.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    self.assignment = customtkinter.CTkRadioButton(master=self.sideRight, text="Assignment", variable=self.project, value="assignment")
    self.assignment.grid(row=2, column=0, sticky="nsew", padx=10, pady=7)

    self.groupType = customtkinter.CTkRadioButton(master=self.sideRight, text="Group", variable=self.project, value="group")
    self.groupType.grid(row=3, column=0, sticky="nsew", padx=10, pady=7)

    self.essayType = customtkinter.CTkRadioButton(master=self.sideRight, text="Essay", variable=self.project, value="essay")
    self.essayType.grid(row=4, column=0, sticky="nsew", padx=10, pady=7)

    self.submission = customtkinter.CTkEntry(master=self.sideLeft, placeholder_text="Submission Link")
    self.submission.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)

    self.description = customtkinter.CTkTextbox(master=self.sideLeft, height=100)
    self.description.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

    self.addTask = customtkinter.CTkButton(master=self.overallTaskFrame, text="Add Task", command=lambda: print("Make Task"))
    self.addTask.grid(row=4, column=0, sticky="nsew", padx=10, pady=10)

    ## Point Value?
    ## Description

    ## Type of assignment



