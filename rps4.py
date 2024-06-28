import sys
import random
from enum import Enum

game_count = 0

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    print("----")
    playerchoice = input("Enter... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")

    while playerchoice not in ["1", "2", "3"]:
        print("You must enter a 1, 2, or 3")
        playerchoice = input("Enter... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")

    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.','').lower() + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.','').lower() + ".\n")

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "🎉 You win!"
        elif player == 2 and computer == 1:
            return "🎉 You win!"
        elif player == 3 and computer == 2:
            return "🎉 You win!"
        elif player == computer:
            return "😲 Tie game!"
        else:
            return "🐍 Python wins!"
        
    game_result = decide_winner(player, computer)

    print(game_result)

    global game_count
    game_count += 1

    print("\nGame count: " + str(game_count) + " games.")

    print("\nPlay again?")

    while True:
        playagain = input("\nY for Yes \nor \nQ to Quit\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉 🎉 🎉 🎉")
        print("Thank you for playing\n")
        playagain = False

play_rps()