from id import makeID
import customtkinter
import json

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("themes/teal.json")

class setup(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.setupDir = {}
        self.classes = False
        self.pageNum = 1
        self.currentClass = 0
        self.numClasses = 1

        self.geometry("600x360")
        # Frames aren't staying consistent with the size (they are staying consistent with the grid as of 7/6)
        self.grid_columnconfigure((0,1,2), weight=1, uniform="1")
        self.grid_columnconfigure((1,2), weight=2)
        self.grid_rowconfigure((0,1), weight=1)

        self.side = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.side.grid(row=0, rowspan=3, column=0, sticky="nswe")
        self.side.columnconfigure(0, weight=1)
        self.side.rowconfigure((0,1), weight=1)

        self.logo = customtkinter.CTkLabel(master=self.side, anchor="n", text="Setup", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo.grid(row=0, column=0, padx=5, pady=5)

        self.questionFrame1 = customtkinter.CTkFrame(master=self)
        self.questionFrame1.grid(row=0, column=1, columnspan=3, rowspan=2, padx=5, pady=5, sticky="nswe")
        self.questionFrame1.columnconfigure(0, weight=1)
        self.questionFrame1.rowconfigure((0,1), weight=1)

        self.question = customtkinter.CTkLabel(master=self.questionFrame1, text="What mode do you want?")
        self.question.grid(row=0, column=0, padx=5, pady=5)

        self.mode = customtkinter.CTkOptionMenu(master=self.questionFrame1, values=["Light", "Dark", "System"], variable=customtkinter.StringVar(value=customtkinter.get_appearance_mode()))
        self.mode.grid(row=1, column=0, padx=5, pady=5)

        self.questionFrame2 = customtkinter.CTkFrame(master=self)
        self.questionFrame2.columnconfigure(0, weight=1)
        self.questionFrame2.rowconfigure((0,1), weight=1)

        self.question = customtkinter.CTkLabel(master=self.questionFrame2, text="What theme do you want?")
        self.question.grid(row=0, column=0, padx=5, pady=5)

        self.theme = customtkinter.CTkOptionMenu(master=self.questionFrame2, values=["Teal", "Orange", "Purple", "Red", "Yellow", "Green", "Blue", "Grey"])
        self.theme.grid(row=1, column=0, padx=5, pady=5)

        self.questionFrame3 = customtkinter.CTkFrame(master=self)
        self.questionFrame3.columnconfigure(0, weight=1)
        self.questionFrame3.rowconfigure((0,1), weight=1)

        self.question = customtkinter.CTkLabel(master=self.questionFrame3, text="How many classes do you have?")
        self.question.grid(row=0, column=0, padx=5, pady=5)

        self.numClass = customtkinter.CTkOptionMenu(master=self.questionFrame3, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
        self.numClass.grid(row=1, column=0, padx=5, pady=5)

        self.classFrame = customtkinter.CTkFrame(master=self)
        self.classFrame.columnconfigure(0, weight=1)
        self.classFrame.rowconfigure((0,1,2), weight=1)

        self.className = customtkinter.CTkEntry(master=self.classFrame, placeholder_text="What is the class name?", width=200)
        self.className.grid(row=0, column=0, padx=5, pady=5)

        self.classSubject = customtkinter.CTkOptionMenu(master=self.classFrame, width=200, variable=customtkinter.StringVar(value="Subject"),
                                                        values=["Math", "Science", "English",  "History", "Social Studies", "World Language", "Fine Arts/Music", "Arts", "Physical Education", "Other"])
        self.classSubject.grid(row=1, column=0, padx=5, pady=5)

        self.classTeacher = customtkinter.CTkEntry(master=self.classFrame, placeholder_text="Who is the teacher/instructor?", width=200)
        self.classTeacher.grid(row=2, column=0, padx=5, pady=5)


        self.pageButton = customtkinter.CTkSegmentedButton(master=self, values=["Last", "Next"], command=self.page)
        self.pageButton.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="nswe")

        self.pageInfo = [self.questionFrame1, self.questionFrame2, self.questionFrame3, self.classFrame]


    def page(self, value):
        self.pageButton.set(None)

        if value == "Last" and self.pageNum == 1:
            pass

        elif value == "Next":
            if self.pageNum > 4:
                self.pageNum = 5

            else:
                self.pageNum += 1

            if self.pageNum == 2:
                self.setupDir["mode"] = self.mode.get()
                self.movepage("Next")

            if self.pageNum == 3:
                self.setupDir["theme"] = self.theme.get()
                self.movepage("Next")

            if self.pageNum == 4:
                self.setupDir["numClasses"] = int(self.numClass.get())
                self.numClasses = int(self.numClass.get())
                self.movepage("Next")

            if self.pageNum >= 5:
                print(self.numClasses)
                print(self.currentClass)
                self.currentClass += 1

                self.setupDir[f"class{self.currentClass}"] =  {
                    "id": makeID(),
                    "className": self.className.get(),
                    "classSubject": self.classSubject.get(),
                    "classTeacher": self.classTeacher.get()
                }

                if self.currentClass == self.numClasses:
                    json_obj = json.dumps(self.setupDir, indent=4)

                    print(json_obj)

                else:
                    self.className.delete(0, "end")
                    self.className.configure(placeholder_text="What is the class name?")
                    self.classSubject.configure(variable=customtkinter.StringVar(value="Subject"))
                    self.classTeacher.delete(0, "end")
                    self.classTeacher.configure(placeholder_text="Who is the teacher/instructor?")


        elif value == "Last":
            self.pageNum -= 1
            print(self.pageNum)

            self.movepage("Last")

    def movepage(self, value):
        if value == "Next":
            self.pageInfo[self.pageNum - 2].grid_forget()
            self.pageInfo[self.pageNum -1].grid(row=0, column=1, columnspan=3, rowspan=2, padx=5, pady=5, sticky="nswe")

        elif value == "Last":
            self.pageInfo[self.pageNum].grid_forget()
            self.pageInfo[self.pageNum - 1].grid(row=0, column=1, columnspan=3, rowspan=2, padx=5, pady=5, sticky="nswe")

if __name__ == "__main__":
    App = setup()
    App.mainloop()