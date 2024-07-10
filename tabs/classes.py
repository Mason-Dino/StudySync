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

    if odd == True:
        c = 0
        row = 0

        while (c < numClasses):
            c += 1

            if c == numClasses:
                self.button = customtkinter.CTkButton(master=self.classFrame, text=f"Class {c}")
                self.button.grid(row=row, column=0, columnspan=2, pady=10)

            elif c % 2 == 0:
                self.button = customtkinter.CTkButton(master=self.classFrame, text=f"Class {c}")
                self.button.grid(row=row, column=1, pady=10)
                row += 1

            else:
                self.button = customtkinter.CTkButton(master=self.classFrame, text=f"Class {c}")
                self.button.grid(row=row, column=0, pady=10)
            
            #print(f"{c} {row}")

    #self.test = customtkinter.CTkLabel(master=self.content, text="Classes")
    #self.test.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)