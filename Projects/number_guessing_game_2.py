from random import choice
from sys import exit

i = ["ROCK", "PAPER", "SCISSORS"]
random_choice = choice(i)

temp = input(
    'Do you want to play?:\nEnter "y" if you want play\nEnter "n" if you dont want play\n'
)
temp = temp.upper()
temp_var = "Y"


def computer_selection():
    print(f"computer picked {random_choice.lower()}")


def play():
    user_input = input("Type Rock/Paper/Scissors:")
    user_input = user_input.upper()
    if (random_choice == "ROCK") and (user_input == "ROCK"):
        computer_selection()
        print("It's a tie")
    elif (random_choice == "PAPER") and (user_input == "PAPER"):
        computer_selection()
        print("It's a tie")
    elif (random_choice == "SCISSORS") and (user_input == "SCISSORS"):
        computer_selection()
        print("It's a tie")
    elif (random_choice == "ROCK") and (user_input == "PAPER"):
        computer_selection()
        print("You won!")
    elif (random_choice == "ROCK") and (user_input == "SCISSORS"):
        computer_selection()
        print("You lost!")
    elif (random_choice == "PAPER") and (user_input == "ROCK"):
        computer_selection()
        print("You lost!")
    elif (random_choice == "PAPER") and (user_input == "SCISSORS"):
        computer_selection()
        print("You won!")
    elif (random_choice == "SCISSORS") and (user_input == "ROCK"):
        computer_selection()
        print("You lost!")
    elif (random_choice == "SCISSORS") and (user_input == "PAPER"):
        computer_selection()
        print("You lost!")
    else:
        print("enter a wrong string!!\n")


while temp_var == "Y":
    if temp == "Y":
        play()
        temp_var = input(
            f'Enter "y" if you continue the game\nEnter "n" or any charecter if quit the game\n'
        )
        temp_var = temp_var.upper()
    else:
        exit("Quit the program!!")
