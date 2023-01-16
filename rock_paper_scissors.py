# Random module needs to be imported
import random

# Create a Class that will define attributes to be used as the Player Name and Score


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


player1 = Player("User", 0)
player2 = Player("Comp", 0)


# Show outputs for all possible outcomes within a While Loop
# Selections made by the computer and user will be in the While Loop
while True:
    options = ["Rock", "Paper", "Scissors"]
    comp_options = random.choice(options)
    print("Welcome to Rock, Paper and Scissors! Please make a selection to play\n")
    print("Good luck! \n")
    user_options = input("Enter your selection: ")

    if user_options == "Rock" or "Paper" or "Scissors":
        print("\nYou have selected", user_options,
              "and the computer has selected", comp_options)
    else:
        print("\nInvalid selection. Please try again")
        continue

    if comp_options == user_options:
        print("You have tied!")
        print("\n| ==== SCOREBOARD ==== |")
        print("|P1:", player1.name, "-- SCORE: ", player1.score, "|")
        print("|P2:", player2.name, "-- SCORE: ", player2.score, "|")

    elif user_options in ["scissors"]:
        if comp_options == "Paper":
            print("\nScissors cuts Paper. You win!")
            player1.score += 1
            print("\n| ==== SCOREBOARD ==== |")
            print("|P1:", player1.name, "-- SCORE: ", player1.score, "|")
            print("|P2:", player2.name, "-- SCORE: ", player2.score, "|")

        else:
            print("\nRock smashes Scissors. You lose!")
            player2.score += 1
            print("\n| ==== SCOREBOARD ==== |")
            print("|P1:", player1.name, "-- SCORE: ", player1.score, "|")
            print("|P2:", player2.name, "-- SCORE: ", player2.score, "|")

    elif user_options in ["paper"]:
        if comp_options == "Rock":
            print("\nPaper covers Rock. You win!")
            player1.score += 1
            print("\n| ==== SCOREBOARD ==== |")
            print("|P1:", player1.name, "-- SCORE: ", player1.score, "|")
            print("|P2:", player2.name, "-- SCORE: ", player2.score, "|")

        else:
            print("\nScissors cuts Paper. You lose!")
            player2.score += 1
            print("\n| ==== SCOREBOARD ==== |")
            print("|P1:", player1.name, "-- SCORE: ", player1.score, "|")
            print("|P2:", player2.name, "-- SCORE: ", player2.score, "|")

    elif user_options in ["rock"]:
        if comp_options == "Scissors":
            print("\nRock smashes Scissors. You win!")
            player1.score += 1
            print("\n| ==== SCOREBOARD ==== |")
            print("|P1:", player1.name, "-- SCORE: ", player1.score, "|")
            print("|P2:", player2.name, "-- SCORE: ", player2.score, "|")

        else:
            print("Paper covers Rock. You lose!")
            player2.score += 1
            print("\n| ==== SCOREBOARD ==== |")
            print("|P1:", player1.name, "-- SCORE: ", player1.score, "|")
            print("|P2:", player2.name, "-- SCORE: ", player2.score, "|")


# User will select option to play again or stop
    start = input("\nDo you wish to play again? (Y or N): ")

    if start.lower() in ["y", "yes"]:
        continue
    elif start.lower() in ["n", "no"]:
        print("\nThanks for playing!")
        break
    else:
        print("\nInvalid selection")
        break
