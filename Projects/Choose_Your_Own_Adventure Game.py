from sys import exit

user_input = input(
    "You wakeup and find a small gift box on your table\nDo you:\n1.Open it\n2.Ignore it\n"
)


def Final_door():
    print("You find a another door.")
    user_input3 = input(
        'A voice asks:\n"What is the one thing you can never live without?"\n'
    )
    if "sumi" or "sumathi" in user_input3.lower():
        print(
            f"--------------------------------------\n{"\u2764\ufe0f"}   Correct!\n---------------------\nYou found the greatest treasure.\nThe treasure was never gold, diamonds, or magic.\nIt was YOU.\nThanks for being part of my world {"\U0001F30E"}{"\u2764\ufe0f"}"
        )


def Blue_color():
    user_input2 = input(
        '----------------------------------\nYou enter a room filled with stars ⭐🌟 and lights ✨✨\n--------------------------\nA note says:\n----------------\n"The real treasure is waiting ahead."\nContinue? (yes/no)\n'
    )
    if "yes" in user_input2.lower():
        Final_door()
    else:
        user_input2 = input(
            'Do you realy not interest to open the final door ?\nEnter "yes" for quit the game\nEnter "No for continueing the game\n'
        )
        if "no" in user_input2.lower():
            print("You find another door...")
            Final_door()
        else:
            exit("Quit the game")


def Red_color():
    user_input_1 = input(
        f"You enter a room full of chocolates {"\U0001F36B"} and flowers{"\U0001F337"}\n----------\n----------\nA note says:\n----------\n----------\nGood choice, but there is something even more valuable in another room\nContinue? (yes/no)\n"
    )
    if "yes" in user_input_1.lower():
        print("You find another door...")
        Blue_color()
    else:
        user_input_1 = input(
            'Do you realy not interest to open the another door ?\nEnter "yes" for quit the game\nEnter "No for continueing the game\n'
        )
        if "no" in user_input_1.lower():
            print("You find another door...")
            Blue_color()
        else:
            exit("Quit the game")


def open():
    user_input1 = input(
        "----------------------------\nOne golden key is present inside the box\n-----------------------\nyou find the two doors\nDo you choose:\n1.Red color\n2. Blue color\n"
    )
    if "red" in user_input1.lower():
        Red_color()
    elif "blue" in user_input1.lower():
        Blue_color()
    else:
        user_input1 = input(
            '------------------\nenter the wrong string\n--------------------\nEnter "Y" to continue the game\n------------------\nEnter "N" for quit the game\n------------------'
        )
        if "y" in user_input.lower():
            open()
        else:
            exit()


def Ignore():
    user_input4 = input(
        "--------------------------You walk away, but your curiosity grows\n----------------\nDo you:\n1. Go back and open it\n2. Leave it forever\n"
    )
    if "open" or "go back" in user_input.lower():
        open()
    elif "leave" in user_input4():
        print("You never discovered what was inside.\n-----------------\nGame Over.")
    else:
        print("enter the wrong string\nquit the game")
        exit()


if "open" in user_input.lower():
    open()
elif "ignore" in user_input.lower():
    Ignore()
