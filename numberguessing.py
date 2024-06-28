import sys
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

def numberguessing():
    secretnumber = random.choice(numbers)
    playagain = True
    print("----------")
    print("Welcome to the number guessing game!\nYou have 25 tries to guess the number!")

    usernumber = int(input("\nEnter a number from 1 to 100\n"))

    while playagain:
        for tries in range(25):
            if usernumber != secretnumber:
                print("Wrong number! 😕")
                if (usernumber > secretnumber):
                    print("Your number was too big. 🐘 \nTry again!\n")
                elif (usernumber < secretnumber):
                    print("Your number was too small. 🐜 \nTry again!")
                usernumber = int(input("\nEnter a number from 1 to 100\n"))
            else:
                    print("You got it! The number was " + str(secretnumber) + "\nGood job! 🥳🎉")
                    
            playagain = input("Would you like to play again?\nY to continue\nor\nQ to Quit\n")
            if playagain.lower() == "y":
                numberguessing()
                break
            else:
                print("Thanks for playing! 😁 \nGoodbye! 👋")
                playagain = False
                sys.exit()
        else:
            print("You ran out of tries! 😔")

        playagain = input("Would you like to play again?\nY to continue\nor\nQ to Quit\n")

        if playagain.lower() == "y":
            numberguessing()
            break
        else:
            print("Thanks for playing! 😁 \nGoodbye! 👋")
            playagain = False
            sys.exit()

numberguessing()