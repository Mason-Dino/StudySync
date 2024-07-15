import customtkinter
import json

def isodd(value: int):
    return ((value % 2) == 1)


def classes(self):
    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.content.grid_columnconfigure(0, weight=1)
    self.content.grid_rowconfigure(0, weight=1)

    self.classFrame = customtkinter.CTkFrame(master=self.content, fg_color="transparent")
    self.classFrame.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

    self.classFrame.grid_columnconfigure((0,1), weight=1)

    with open("setup.json", "r") as f:
        self.setupDir = json.load(f)

    numClasses = int(self.setupDir["numClasses"])
    odd = isodd(numClasses)


    # Error when I click a class button it only prints the number of classes and not that correct class number
    classButton = {}

    if odd == True:
        c = 0
        row = 0

        while (c < numClasses):
            c += 1

            if c == numClasses:
                classButton[f"class{c}"] = customtkinter.CTkButton(master=self.classFrame, text=self.setupDir[f"class{c}"]["name"])
                classButton[f"class{c}"].grid(row=row, column=0, columnspan=2, pady=10)

            elif c % 2 == 0:
                classButton[f"class{c}"] = customtkinter.CTkButton(master=self.classFrame, text=self.setupDir[f"class{c}"]["name"])
                classButton[f"class{c}"].grid(row=row, column=1, pady=15)
                row += 1

            else:
                classButton[f"class{c}"] = customtkinter.CTkButton(master=self.classFrame, text=self.setupDir[f"class{c}"]["name"])
                classButton[f"class{c}"].grid(row=row, column=0, pady=15)
            
            #print(f"{c} {row}")

    elif odd == False:
        c = 0
        row = 0

        while (c < numClasses):
            c += 1
            print(c)

            if c == 1:
                classButton = customtkinter.CTkButton(master=self.classFrame, text=self.setupDir[f"class{c}"]["name"], command=lambda: classScreen(c))
                classButton.grid(row=row, column=0, pady=15)

            elif c % 2 == 0: 
                classButton = customtkinter.CTkButton(master=self.classFrame, text=self.setupDir[f"class{c}"]["name"], command=lambda: classScreen(c))
                classButton.grid(row=row, column=1, pady=15)
                row += 1

            else:
                classButton = customtkinter.CTkButton(master=self.classFrame, text=self.setupDir[f"class{c}"]["name"], command=lambda: classScreen(c))
                classButton.grid(row=row, column=0, pady=15)

        #print(classButton)

    for i in range(numClasses):
        print(f"class{i+1}")
        #classButton[f"class{i+1}"].configure(command=lambda: classScreen(i+1))
            

def classScreen(button):
    print(button)