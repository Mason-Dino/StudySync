import random

lowerLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upperLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def makeID(length:int=10, lower=True, upper=True,  num=True):
    id = ""
    if lower == False and upper == False and num == False:
        lower = True
        upper = True
        num = True

    for i in range(length):
        option = random.randint(1,3)
        
        if option == 1:
            id += random.choice(lowerLetters)

        if option == 2:
            id += random.choice(upperLetters)

        if option == 3:
            id += f"{random.choice(number)}"

    return id