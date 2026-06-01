from random import choice
from sys import exit

i = ["ROCK", "PAPER", "SCISSORS"]
random_choice = choice(i)

temp = input('Do you want to play?:\nPress "Enter" key if you want\n')
def play():
    user_input = input("Type Rock/Paper/Scissors:")
    print(f"computer picked {random_choice}")
    user_input = user_input.upper()
    if (random_choice == "ROCK") and (user_input == "ROCK"):
        print("It's a tie")
    elif (random_choice == "PAPER") and (user_input == "PAPER"):
        print("It's a tie")
    elif (random_choice == "SCISSORS") and (user_input == "SCISSORS"):
        print("It's a tie")
    elif (random_choice == "ROCK") and (user_input == "PAPER"):
        print("You won!")
    elif (random_choice == "ROCK") and (user_input == "SCISSORS"):
        print("You lost!")
    elif (random_choice == "PAPER") and (user_input == "ROCK"):
        print("You lost!")
    elif (random_choice == "PAPER") and (user_input == "SCISSORS"):
        print("You won!")
    elif (random_choice == "SCISSORS") and (user_input == "ROCK"):
        print("You lost!")
    elif (random_choice == "SCISSORS") and (user_input == "PAPER"):
        print("You won!")
    else:
        print("enter wrong string!!\n")


if temp == "":
    play()
else:
    exit("Quit the program!!")
