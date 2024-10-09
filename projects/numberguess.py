import random
retry = True
print("=================")
print("Guess The Number!")
print("=================")

while retry == True:
    givenNum = int(input("Choose a number between 1-10"))
    randomNum = random.randint(1, 10)
    if givenNum == randomNum:
        print("Wowzers you guesed right")
    else:
        print("Nope")
    tryAgain = input("Would you like to try again? (y/n)")
    if tryAgain == "y":
        retry = True
    elif tryAgain == "n":
        retry = False
        print("Thanks for playing!")
        exit
    else:
        print("It's y or n, dummy")
        exit