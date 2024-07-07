from id import makeID
import customtkinter
import json

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("themes/teal.json")

class setup(customtkinter.CTk):
    def __init__(self):
        """
        This is the constructor for the Setup class. It initializes the setup window and its elements.
        """
        super().__init__()

        # Initialize the attributes
        self.setupDir = {}
        self.classes = False
        self.pageNum = 1
        self.currentClass = 0
        self.numClasses = 1

        # Set the size of the window
        self.geometry("600x360")

        # Configure the grid to make the frames stick together
        self.grid_columnconfigure((0,1,2), weight=1, uniform="1")
        self.grid_columnconfigure((1,2), weight=2)
        self.grid_rowconfigure((0,1), weight=1)

        # Create the side frame and add the logo
        self.side = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.side.grid(row=0, rowspan=3, column=0, sticky="nswe")
        self.side.grid_columnconfigure(0, weight=1)
        self.side.grid_rowconfigure((0,1), weight=1)

        self.logo = customtkinter.CTkLabel(master=self.side, anchor="n", text="Setup", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo.grid(row=0, column=0, padx=5, pady=5)

        # Create the first question frame
        self.questionFrame1 = customtkinter.CTkFrame(master=self)
        self.questionFrame1.grid(row=0, column=1, columnspan=3, rowspan=2, padx=5, pady=5, sticky="nswe")
        self.questionFrame1.grid_columnconfigure(0, weight=1)
        self.questionFrame1.grid_rowconfigure((0,1), weight=1)

        self.question = customtkinter.CTkLabel(master=self.questionFrame1, text="What mode do you want?")
        self.question.grid(row=0, column=0, padx=5, pady=5)

        self.mode = customtkinter.CTkOptionMenu(master=self.questionFrame1, values=["Light", "Dark", "System"], variable=customtkinter.StringVar(value=customtkinter.get_appearance_mode()))
        self.mode.grid(row=1, column=0, padx=5, pady=5)

        # Create the second question frame
        self.questionFrame2 = customtkinter.CTkFrame(master=self)
        self.questionFrame2.grid_columnconfigure(0, weight=1)
        self.questionFrame2.grid_rowconfigure((0,1), weight=1)

        self.question = customtkinter.CTkLabel(master=self.questionFrame2, text="What theme do you want?")
        self.question.grid(row=0, column=0, padx=5, pady=5)

        self.theme = customtkinter.CTkOptionMenu(master=self.questionFrame2, values=["Teal", "Orange", "Purple", "Red", "Yellow", "Green", "Blue", "Grey"])
        self.theme.grid(row=1, column=0, padx=5, pady=5)

        # Create the third question frame
        self.questionFrame3 = customtkinter.CTkFrame(master=self)
        self.questionFrame3.grid_columnconfigure(0, weight=1)
        self.questionFrame3.grid_rowconfigure((0,1), weight=1)

        self.question = customtkinter.CTkLabel(master=self.questionFrame3, text="How many classes do you have?")
        self.question.grid(row=0, column=0, padx=5, pady=5)

        self.numClass = customtkinter.CTkOptionMenu(master=self.questionFrame3, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
        self.numClass.grid(row=1, column=0, padx=5, pady=5)

        # Create the class frame
        self.classFrame = customtkinter.CTkFrame(master=self)
        self.classFrame.grid_columnconfigure(0, weight=1)
        self.classFrame.grid_rowconfigure((0,1,2), weight=1)

        self.className = customtkinter.CTkEntry(master=self.classFrame, placeholder_text="What is the class name?", width=200)
        self.className.grid(row=0, column=0, padx=5, pady=5)

        self.classSubject = customtkinter.CTkOptionMenu(master=self.classFrame, width=200, variable=customtkinter.StringVar(value="Subject"),
                                                        values=["Math", "Science", "English",  "History", "Social Studies", "World Language", "Fine Arts/Music", "Arts", "Physical Education", "Other"])
        self.classSubject.grid(row=1, column=0, padx=5, pady=5)

        self.classTeacher = customtkinter.CTkEntry(master=self.classFrame, placeholder_text="Who is the teacher/instructor?", width=200)
        self.classTeacher.grid(row=2, column=0, padx=5, pady=5)


        # Create the page buttons
        self.pageButton = customtkinter.CTkSegmentedButton(master=self, values=["Last", "Next"], command=self.page)
        self.pageButton.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="nswe")

        # Create the congratulations frame
        self.congratsFrame = customtkinter.CTkFrame(master=self)
        self.congratsFrame.grid_columnconfigure(0, weight=1)
        self.congratsFrame.grid_rowconfigure(0, weight=1)

        self.congrats = customtkinter.CTkLabel(master=self.congratsFrame, text="Congratulations!\nYou have finished the setup!\nClick Next to start using StudySync!")
        self.congrats.grid(row=0, column=0, padx=5, pady=5, sticky="nswe")

        # Store the frames for the page function
        self.pageInfo = [self.questionFrame1, self.questionFrame2, self.questionFrame3, self.classFrame, self.congratsFrame]

        # Bind the return key to the page function
        self.bind("<Return>", lambda e: self.page("Next"))

    def page(self, value):
        """
        This function is used to move to the next or last page based on the value passed in.

        If the value is "Next", the current page is removed from the grid and the next page is moved
        to the current position.

        If the value is "Last", the current page is removed from the grid and the last page is moved
        to the current position.
        """

        # Set the value of the pageButton to None to reset its state
        self.pageButton.set(None)

        # If the value is "Last" and the current page is the first page, do nothing
        if value == "Last" and self.pageNum == 1:
            pass

        # If the value is "Next", move to the next page
        elif value == "Next":

            # If the current page is greater than 4, set the page number to 5
            if self.pageNum > 4:
                self.pageNum = 5

            # Otherwise, increment the page number
            else:
                self.pageNum += 1

            # If the page number is 2, set the mode in the setup directory and move to the next page
            if self.pageNum == 2:
                self.setupDir["mode"] = self.mode.get()
                self.movepage("Next")

            # If the page number is 3, set the theme in the setup directory and move to the next page
            if self.pageNum == 3:
                self.setupDir["theme"] = self.theme.get()
                self.movepage("Next")

            # If the page number is 4, set the number of classes in the setup directory, update the number of classes,
            # and move to the next page
            if self.pageNum == 4:
                self.setupDir["numClasses"] = int(self.numClass.get())
                self.numClasses = int(self.numClass.get())
                self.movepage("Next")

            # If the page number is greater than or equal to 5, increment the current class count,
            # add the current class to the setup directory, and move to the next page
            if self.pageNum >= 5:
                self.currentClass += 1

                self.setupDir[f"class{self.currentClass}"] =  {
                    "id": makeID(),
                    "className": self.className.get(),
                    "classSubject": self.classSubject.get(),
                    "classTeacher": self.classTeacher.get()
                }
                
                self.className.delete(0, "end")
                self.className.configure(placeholder_text="What is the class name?")
                self.classSubject.configure(variable=customtkinter.StringVar(value="Subject"))
                self.classTeacher.delete(0, "end")
                self.classTeacher.configure(placeholder_text="Who is the teacher/instructor?")

                # If the current class count is equal to the number of classes, print the setup directory as JSON,
                # display the final page, and reset the class entry widgets
                if self.currentClass == self.numClasses:
                    self.setupDir["setupComplete"] = True

                    json_obj = json.dumps(self.setupDir, indent=4)

                    print(json_obj)

                    self.pageInfo[4].grid(row=0, column=1, columnspan=3, rowspan=2, padx=5, pady=5, sticky="nswe")


        # If the value is "Last", move to the previous page
        elif value == "Last":
            self.pageNum -= 1

            self.movepage("Last")

    # This function is used to move the current page to the next or last page
    # based on the value passed in.

    # If the value is "Next", the current page is removed from the grid and
    # the next page is moved to the current position.

    # If the value is "Last", the current page is removed from the grid and
    # the last page is moved to the current position.

    def movepage(self, value):
        # Check if the value is "Next"
        if value == "Next":
            # Remove the current page from the grid
            self.pageInfo[self.pageNum - 2].grid_forget()
            
            # Move the next page to the current position
            self.pageInfo[self.pageNum -1].grid(row=0, column=1, columnspan=3, rowspan=2, padx=5, pady=5, sticky="nswe")

        # Check if the value is "Last"
        elif value == "Last":
            # Remove the current page from the grid
            self.pageInfo[self.pageNum].grid_forget()
            
            # Move the last page to the current position
            self.pageInfo[self.pageNum - 1].grid(row=0, column=1, columnspan=3, rowspan=2, padx=5, pady=5, sticky="nswe")

if __name__ == "__main__":
    App = setup()
    App.mainloop()