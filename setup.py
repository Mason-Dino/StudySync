from task import database
from id import makeID
from icon import getIcons
import customtkinter
import json
from tkinter import messagebox
from tkinter import filedialog

from themes.theme import *


class setup(customtkinter.CTk):
    def __init__(self):
        self.version = "v1.0.2"
        self.beta = False
        """
        This is the constructor for the Setup class. It initializes the setup window and its elements.
        """
        # Call the constructor of the parent class
        super().__init__()

        # Set the appearance mode and default color theme
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("themes/teal.json")

        self.after(201, lambda :self.iconbitmap(r"logo\StudySync-ico.ico"))

        # Initialize the attributes
        self.setupDir = {}  # Dictionary to store the setup directory
        self.classes = False  # Flag to indicate if the user has classes
        self.pageNum = 1  # Current page number
        self.currentClass = 0  # Current class index
        self.numClasses = 1  # Number of classes

        # Set the size of the window and title
        self.geometry("600x360")
        self.title("Setup")

        # Configure the grid to make the frames stick together
        self.grid_columnconfigure((0,1,2), weight=1, uniform="1")  # Column weights and uniform configuration
        self.grid_columnconfigure((1,2), weight=2)  # Column weights
        self.grid_rowconfigure((0,1), weight=1)  # Row weights

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Create the side frame and add the logo
        self.side = customtkinter.CTkFrame(master=self, corner_radius=0)  # Create the side frame
        self.side.grid(row=0, rowspan=3, column=0, sticky="nswe")  # Position the side frame
        self.side.grid_columnconfigure(0, weight=1)  # Column weight
        self.side.grid_rowconfigure((0,1), weight=1)  # Row weight

        self.logo = customtkinter.CTkLabel(master=self.side, anchor="n", text="Setup", font=customtkinter.CTkFont(size=20, weight="bold"))  # Create the logo label
        self.logo.grid(row=0, column=0, padx=5, pady=5)  # Position the logo label

        self.load = customtkinter.CTkButton(master=self.side, text="Load Setup", command=self.loadSetup)  # Create the load button
        self.load.grid(row=1, column=0, padx=10, pady=5)  # Position the load button

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Create the first question frame
        self.questionFrame1 = customtkinter.CTkFrame(master=self)  # Create the first question frame
        self.questionFrame1.grid(row=0, column=1, columnspan=3, rowspan=2, padx=5, pady=5, sticky="nswe")  # Position the first question frame
        self.questionFrame1.grid_columnconfigure(0, weight=1)  # Column weight
        self.questionFrame1.grid_rowconfigure((0,1), weight=1)  # Row weight

        self.question = customtkinter.CTkLabel(master=self.questionFrame1, text="What mode do you want?")  # Create the mode question label
        self.question.grid(row=0, column=0, padx=5, pady=5)  # Position the mode question label

        self.mode = customtkinter.CTkOptionMenu(master=self.questionFrame1, values=["Light", "Dark", "System"], variable=customtkinter.StringVar(value=customtkinter.get_appearance_mode()))  # Create the mode option menu
        self.mode.grid(row=1, column=0, padx=5, pady=5)  # Position the mode option menu

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Create the second question frame
        self.questionFrame2 = customtkinter.CTkFrame(master=self)  # Create the second question frame
        self.questionFrame2.grid_columnconfigure(0, weight=1)  # Column weight
        self.questionFrame2.grid_rowconfigure((0,1), weight=1)  # Row weight

        self.question = customtkinter.CTkLabel(master=self.questionFrame2, text="What theme do you want?")  # Create the theme question label
        self.question.grid(row=0, column=0, padx=5, pady=5)  # Position the theme question label

        self.theme = customtkinter.CTkOptionMenu(master=self.questionFrame2, values=["Teal", "Orange", "Purple", "Red", "Yellow", "Green", "Blue", "Grey"])  # Create the theme option menu
        self.theme.grid(row=1, column=0, padx=5, pady=5)  # Position the theme option menu

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Create the third question frame
        self.questionFrame3 = customtkinter.CTkFrame(master=self)  # Create the third question frame
        self.questionFrame3.grid_columnconfigure(0, weight=1)  # Column weight
        self.questionFrame3.grid_rowconfigure((0,1), weight=1)  # Row weight

        self.question = customtkinter.CTkLabel(master=self.questionFrame3, text="How many classes do you have?")  # Create the class question label
        self.question.grid(row=0, column=0, padx=5, pady=5)  # Position the class question label

        self.numClass = customtkinter.CTkOptionMenu(master=self.questionFrame3, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])  # Create the class option menu
        self.numClass.grid(row=1, column=0, padx=5, pady=5)  # Position the class option menu

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Create the class frame
        self.classFrame = customtkinter.CTkFrame(master=self)  # Create the class frame
        self.classFrame.grid_columnconfigure((0), weight=1)  # Column weight
        #self.classFrame.grid_rowconfigure((0,1,2), weight=1)  # Row weights

        self.title = customtkinter.CTkLabel(master=self.classFrame, text=f"Class Add",
                                        font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title.grid(row=0, column=0, pady=10)

        self.classNameFrame = customtkinter.CTkFrame(master=self.classFrame, fg_color=topLevel())
        self.classNameFrame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        self.classNameFrame.grid_columnconfigure((0), weight=1)

        self.className = customtkinter.CTkEntry(master=self.classNameFrame, placeholder_text="Class Name", width=200)
        self.className.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.cosmetics = customtkinter.CTkFrame(master=self.classFrame, fg_color=topLevel())
        self.cosmetics.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        self.cosmetics.grid_columnconfigure((0,1), weight=1)

        self.classSubject = customtkinter.CTkOptionMenu(master=self.cosmetics, values=["Math", "Science", "English",  "History", "Social Studies", "World Language", "Fine Arts/Music", "Arts", "Physical Education", "Other"],
                                                    variable=customtkinter.StringVar(value="Subject"))
        self.classSubject.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.classIcon = customtkinter.CTkOptionMenu(master=self.cosmetics, values=getIcons(), variable=customtkinter.StringVar(value="Icon"))
        self.classIcon.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.classColor = customtkinter.CTkOptionMenu(master=self.cosmetics, values=["Teal", "Orange", "Purple", "Red", "Yellow", "Green", "Blue", "Other"],
                                                    variable=customtkinter.StringVar(value="Color"), command=lambda colorOption: self.changeColorSetup(colorOption))
        self.classColor.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        self.newColor = customtkinter.CTkEntry(master=self.cosmetics, placeholder_text="Color (hex code)")

        self.teacherFrame = customtkinter.CTkFrame(master=self.classFrame, fg_color=topLevel())
        self.teacherFrame.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        self.teacherFrame.grid_columnconfigure((0,1), weight=1)

        self.classTeacher = customtkinter.CTkEntry(master=self.teacherFrame, placeholder_text="Who is the teacher/instructor?")
        self.classTeacher.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.classTeacherEmail = customtkinter.CTkEntry(master=self.teacherFrame, placeholder_text="What is their email?")
        self.classTeacherEmail.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Create the page buttons
        self.pageButton = customtkinter.CTkSegmentedButton(master=self, values=["Last", "Next"], command=self.page)  # Create the page buttons
        self.pageButton.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="nswe")  # Position the page buttons

        # Create the congratulations frame
        self.congratsFrame = customtkinter.CTkFrame(master=self)  # Create the congratulations frame
        self.congratsFrame.grid_columnconfigure(0, weight=1)  # Column weight
        self.congratsFrame.grid_rowconfigure(0, weight=1)  # Row weight

        self.congrats = customtkinter.CTkLabel(master=self.congratsFrame, text="Congratulations!\nYou have finished the setup!\nRestart StudySync to start using it!")  # Create the congratulations label
        self.congrats.grid(row=0, column=0, padx=5, pady=5, sticky="nswe")  # Position the congratulations label

        # Store the frames for the page function
        self.pageInfo = [self.questionFrame1, self.questionFrame2, self.questionFrame3, self.classFrame, self.congratsFrame]

        self.protocol("WM_DELETE_WINDOW", self.close)

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
                # Store the selected mode in the setup directory
                self.setupDir["mode"] = self.mode.get()
                # Move to the next page
                self.movepage("Next")

            # If the page number is 3, set the theme in the setup directory and move to the next page
            if self.pageNum == 3:
                # Store the selected theme in the setup directory
                self.setupDir["theme"] = self.theme.get()
                # Move to the next page
                self.movepage("Next")

            # If the page number is 4, set the number of classes in the setup directory,
            # update the number of classes, and move to the next page
            if self.pageNum == 4:
                # Store the entered number of classes in the setup directory
                self.setupDir["numClasses"] = int(self.numClass.get())
                # Update the number of classes
                self.numClasses = int(self.numClass.get())
                # Move to the next page
                self.movepage("Next")

            # If the page number is greater than or equal to 5, increment the current class count,
            # add the current class to the setup directory, and move to the next page
            if self.pageNum >= 5:
                # Increment the current class count
                self.currentClass += 1

                if self.classIcon.get() == "Icon":
                    icon = "Other"

                else:
                    icon = self.classIcon.get()

                if self.classSubject.get() == "Subject":
                    subject = "Other"

                else:
                    subject = self.classSubject.get()

                if self.classColor == "Color":
                    color = "Blue"

                else:
                    color = self.classColor.get()

                if color.lower() == "other":
                    newColor = self.newColor.get()

                    if isValidColorCode(newColor) == True:
                        color = newColor
                        error = False

                    else:
                        color = "Blue"
                        messagebox.showerror(title="Error", message="Invalid color code")
                        error = True

                else:
                    error = False

                if error == False:
                # Create a dictionary to store the details of the current class
                    class_details = {
                        "id": makeID(),  # Generate a unique ID for the class
                        "name": self.className.get(),  # Store the class name
                        "subject": subject,  # Store the class subject
                        "icon": icon,  # Store the class icon
                        "color": color.lower(),  # Store the class color
                        "teacher": self.classTeacher.get(),  # Store the class teacher/instructor
                        "email": self.classTeacherEmail.get(),  # Store the class email
                    }

                    database()

                    # Add the current class to the setup directory
                    self.setupDir[f"class{self.currentClass}"] = class_details

                    # Clear the class name entry widget
                    self.className.delete(0, "end")
                    # Reconfigure the class name entry widget to display the placeholder text
                    self.className.configure(placeholder_text="What is the class name?")

                    # Reset the class subject option menu to display the default value
                    self.classSubject.configure(variable=customtkinter.StringVar(value="Subject"))

                    self.classColor.configure(variable=customtkinter.StringVar(value="Color"))

                    # Clear the class teacher/instructor entry widget
                    self.classTeacher.delete(0, "end")
                    # Reconfigure the class teacher/instructor entry widget to display the placeholder text
                    self.classTeacher.configure(placeholder_text="Who is the teacher/instructor?")

                    # Clear the class email entry widget
                    self.classTeacherEmail.delete(0, "end")
                    # Reconfigure the class email entry widget to display the placeholder text
                    self.classTeacherEmail.configure(placeholder_text="What is the email?")

                    # Reset the class icon option menu to display the default value
                    self.classIcon.configure(variable=customtkinter.StringVar(value="Icon"))

                    # If the current class count is equal to the number of classes, print the setup directory as JSON,
                    # display the final page, and reset the class entry widgets
                    if self.currentClass == self.numClasses:
                        self.setupDir["setupComplete"] = True  # Set the setup complete flag in the setup directory

                        self.setupDir["progress"] = 0
                        self.setupDir["level"] = 0
                        self.setupDir["version"] = self.version
                        self.setupDir["betaUser"] = False

                        self.setupDir["tabs"] = {
                            "home": True,
                            "class": True,
                            "task": True,
                            "due": True,
                            "important": True,
                            "study-timer": True
                        }

                        # Convert the setup directory to JSON format and store it in a variable
                        json_obj = json.dumps(self.setupDir, indent=4)

                        # Open the setup.json file in write mode and write the JSON data to the file
                        with open("setup.json", "w") as f:
                            f.write(json_obj)

                        # Print the setup directory as JSON
                        print(json_obj)

                        # Display the final page
                        self.pageInfo[4].grid(row=0, column=1, columnspan=3, rowspan=2, padx=5, pady=5, sticky="nswe")


        # If the value is "Last", move to the previous page
        elif value == "Last":
            # Decrement the page number
            self.pageNum -= 1

            # Move to the previous page
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

    def close(self):
        self.destroy()
        exit()

    def changeColorSetup(self, colorOption):
        if colorOption == "Other":
            self.classColor.grid_forget()
            self.classColor.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

            self.newColor.grid_forget()
            self.newColor.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

    def loadSetup(self):
        file_path = filedialog.askopenfilename(filetypes=(("JSON Files", "*.json"), ("All Files", "*.*")))

        with open(file_path, "r") as f:
            setupDir = json.load(f)

        try:
            if setupDir["setupComplete"] == False or setupDir["setupComplete"] == None:
                messagebox.showwarning(title="Error", message="Not a valid setup file")

            else:
                numClass = setupDir["numClasses"]
                mode = setupDir["mode"]
                theme = setupDir["theme"]
                progress = setupDir["progress"]
                level = setupDir["level"]
                version = setupDir["version"]
                beta = setupDir["betaUser"]

                for i in range(numClass):
                    id = setupDir[f"class{i+1}"]["id"]
                    name = setupDir[f"class{i+1}"]["name"]
                    teacher = setupDir[f"class{i+1}"]["teacher"]
                    subject = setupDir[f"class{i+1}"]["subject"]
                    color = setupDir[f"class{i+1}"]["color"]
                    icon =  setupDir[f"class{i+1}"]["icon"]

                setupDir["version"] = self.version

                with open("setup.json", "w") as f:
                    json.dump(setupDir, f, indent=4)
                messagebox.showinfo(title="Success", message="Setup file loaded!")

                database()

                self.pageInfo[4].grid(row=0, column=1, columnspan=3, rowspan=2, padx=5, pady=5, sticky="nswe")

        except KeyError:
            messagebox.showerror(title="Error", message="\tNot a valid setup file file\n\tPlease select a valid setup file\n\tOld setup file is still in use.")

if __name__ == "__main__":
    App = setup()
    App.mainloop()