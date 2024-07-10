import customtkinter
import json

def isodd(value: int):
    return ((value % 2) == 1)


def classes(self):
    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.content.grid_columnconfigure((1,2), weight=1)
    self.content.grid_rowconfigure((0,1,2,3,4), weight=1)

    with open("setup.json", "r") as f:
        self.setupDir = json.load(f)

    numClasses = int(self.setupDir["numClasses"])
    odd = isodd(numClasses)

    if odd == True:
        c = 0
        row = 0

        while (c < (numClasses - 1)):
            #print(c)
            c += 1

            if c % 2 == 0:
                self.button = customtkinter.CTkButton(master=self.content, text=f"Class {c}")
                self.button.grid(row=row, column=1, padx=10, pady=10)
                row += 1

            else:
                self.button = customtkinter.CTkButton(master=self.content, text=f"Class {c}")
                self.button.grid(row=row, column=0, padx=10, pady=10)
            
            print(f"{c} {row}")

    #self.test = customtkinter.CTkLabel(master=self.content, text="Classes")
    #self.test.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)