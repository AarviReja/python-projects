import random
import sys

games_played = 0
user_wins = 0



if games_played == 0:
    playagain = "y"
    print(playagain)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Makes the game more personal by adressing the user by their name."
    )

    parser.add_argument(
            "-n", "--name", metavar="name",
            required=True, help="The name of the player.")

    args =  parser.parse_args()



def play_game(name='PlayerOne'):
    if __name__ != "__main__":
        global playagain
    while playagain.lower() == "y":
        
        def play_again():
            playagain = input("\nY for Yes or\nQ to Quit\n\n")
            
            if playagain.lower() == "y":
                return play_game(name)
            elif playagain.lower() == "q":
                if __name__ == "__main__":
                    sys.exit(f"Thanks for playing {name}!\nBye!")
                elif __name__ != "__main":
                    print(f"Thanks for playing {name}!\nBye!")
            else:
                print(f"Sorry {name}, what did you want to do?")
                return play_again()
            print(playagain.lower())
        
        global games_played
        global user_wins
        
        if playagain.lower() == "y":
            secretnumber = random.choice("123")
            usernumber = input(f"\n---------------\n{name}, guess the number I'm thinking of... 1, 2, or 3.\n")

            if usernumber not in "1, 2, 3":
                print(f"{name}, sorry, but that wasn't one of the options.")
                return play_game(name)

            if secretnumber != usernumber:
                print(f"Sorry {name}, you lost.")
                games_played += 1
            else:
                print(f"Woohoo! {name}, you won!")
                games_played += 1
                user_wins += 1

            print(f"\nGame count: {games_played}\n")
            print(f"\n{name}'s wins: {user_wins}\n")

            if user_wins == 0:
                print(f"\nYour winning percentage: 0.00%\n")
            else:
                print(f"\nYour winning percentage: {user_wins/games_played:.2%}\n")

            print(f"Play again, {name}?")
            play_again()
            if playagain.lower() == "y":
                continue
            else:
                print(playagain)
        else:
            playagain = "q"



if __name__ == "__main__":
    play_game(args.name)