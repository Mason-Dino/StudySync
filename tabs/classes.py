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
                classButton[c] = customtkinter.CTkButton(master=self.classFrame, text=self.setupDir[f"class{c}"]["name"])
                classButton[c].grid(row=row, column=0, pady=15)
                print(classButton[c]._text)

            elif c % 2 == 0: 
                classButton[c] = customtkinter.CTkButton(master=self.classFrame, text=self.setupDir[f"class{c}"]["name"])
                classButton[c].grid(row=row, column=1, pady=15)
                row += 1

            else:
                classButton[c] = customtkinter.CTkButton(master=self.classFrame, text=self.setupDir[f"class{c}"]["name"])
                classButton[c].grid(row=row, column=0, pady=15)

        #print(classButton)

    for i in range(numClasses):
        print(i)

        if i == 0:
            classButton[i+1].configure(command=lambda: classScreen(1))

        elif i == 1:
            classButton[i+1].configure(command=lambda: classScreen(2))

        elif i == 2:
            classButton[i+1].configure(command=lambda: classScreen(3))

        elif i == 3:
            classButton[i+1].configure(command=lambda: classScreen(4))

        elif i == 4:
            classButton[i+1].configure(command=lambda: classScreen(5))

        elif i == 5:
            classButton[i+1].configure(command=lambda: classScreen(6))

        elif i == 6:
            classButton[i+1].configure(command=lambda: classScreen(7))

        elif i == 7:
            classButton[i+1].configure(command=lambda: classScreen(8))

        elif i == 8:
            classButton[i+1].configure(command=lambda: classScreen(9))

        elif i == 9:
            classButton[i+1].configure(command=lambda: classScreen(10))
            

def classScreen(button):
    print(button)