import argparse
import rps8
import guess_number
import sys

parser = argparse.ArgumentParser(
    description="Makes the game more personal by adressing the user using their name."
)

parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the player."
    )

args =  parser.parse_args()
print(args.name)

rock_paper_scissors = rps8.rps(args.name)

def arcade(name):
    # global args
    # args = parser.parse_args()
    print(f"\n{name}, welcome to the arcade!")
    def pick_game():
        # global args
        print(f"\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number")
        print('\nOr press "x" to exit the Arcade')
        game = input("\n")

        try:
            game = int(game)
        except:
            if game.lower() == "x":
                sys.exit(f"Goodbye {name}!")
            else:
                print("Please enter 1, 2, or x.")
                return pick_game()

        if game == 1:
            rock_paper_scissors()
            print(f"Welcome back to the arcade {name}!")
            return pick_game()
        elif game == 2:
            guess_number.play_game(name)
            print(f"Welcome back to the arcade {name}!")
            return pick_game()
        
    pick_game()
