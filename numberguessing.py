import sys
import random

numbers = range(1, 100+1)
print(f"\nWelcome to numberguessing.\nYou have 10 tries to guess the number.")
print("---------------------")

def numberguessing():
    secretnumber = random.choice(numbers)
    playagain = True

    usernumber = input("\nEnter a number from 1 to 100\n")
    try:
        usernumber = int(usernumber)
    except:
        print("invalid number")
        return numberguessing()
    
    def play_again():
        playagain = input("\nWould you like to play again?\nY to continue\nor\nQ to Quit\n\n")
        if playagain.lower() == "y":
            numberguessing()
        elif playagain.lower() ==  "q":
            print("Thanks for playing! 😁 \nGoodbye! 👋")
            sys.exit()
        else:
            print("Sorry, what did you want to do?")
            return play_again()
            

    while playagain == True:
        for tries in range(0,9):
            if usernumber != secretnumber:
                print("Wrong number! 😕")
                if (usernumber > secretnumber):
                    print("Your number was too big. 🐘 \nTry again!\n")
                elif (usernumber < secretnumber):
                    print("Your number was too small. 🐜 \nTry again!")
                usernumber = int(input("\nEnter a number from 1 to 100\n"))
            else:
                print(f"You got it! The number was {secretnumber}\nGood job! 🥳🎉")
                return play_again()
        else:
            print("Wrong number! 😕")
            if usernumber < secretnumber:
                print("Your number was too small. 🐜")
            elif usernumber > secretnumber:
                print("Your number was to big. 🐘")
            print("\nYou ran out of tries.\n")
            print(f"The secret number was {secretnumber}.\nBetter luck next time!")

        play_again()
    else:
        return None
    

numberguessing()