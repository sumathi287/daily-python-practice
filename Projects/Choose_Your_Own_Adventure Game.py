user_input = input(
    "One fine mornig you wake up form the bed\n--------------\nyou saw the one gift box on the table\n----------\n1.open it\n2.Ignore it\n"
)
if "open" in user_input.lower() or "1" in user_input:
    print("You found the one golden key in that box\n")
    user_input_open = input(
        "You find a two doors\n------------\nDo you choose:\n1.Red door\n2.Blue door\n"
    )
    if (
        "red door" in user_input_open.lower()
        or "red" in user_input_open.lower()
        or "1" in user_input_open
    ):
        print(
            "You enter the room with full of choculates🍫🍫🍫 and flowers💐🌺🌸🌼🌷\n"
        )
        user_input_red = input(
            "A note says:\n------------\n-----------\nGood choice, but there is something even more valuable.\nContinue?\n1.Yes\n2.No\n"
        )
        if "yes" in user_input_red.lower() or "1" in user_input_red:
            print("You enter a room filled with stars🌟🌟🌟🌟🌟 and lights✨✨✨✨✨.")
            user_input_red1 = input(
                "A note says:\nThe real treasure is waiting ahead.\nContinue? \n1.Yes\n2.No\n"
            )
            if "yes" in user_input_red1.lower() or "1" in user_input_red1:
                print("You find the another door\nYou open the final door.\n")
                user_input_red2 = input(
                    'A voice asks:\n"What is the one thing you can never live without?"\n'
                )
                if "sumi" in user_input_red2 or "sumathi" in user_input_red2:
                    print(
                        "❤️ Correct!\nYou found the greatest treasure.\n-------------\n----------\nThe treasure was never gold, diamonds, or magic.It was YOU.\nThanks for being part of my world. ❤️"
                    )
                else:
                    print(
                        "Congrats!!\nI expect something more precious answer\nBut still\nThe treasure was never gold, diamonds, or magic.It was YOU.\nThanks for being part of my world. ❤️"
                    )
            else:
                print("End the game!!")
        elif "no" in user_input_red.lower() or "2" in user_input_red:
            print("End the game!!")
        else:
            print("Enter the wrong string\nQuit the Game")

    elif (
        "blue door" in user_input_open.lower()
        or "blue" in user_input_open.lower()
        or "2" in user_input_open
    ):
        print("You enter a room filled with stars🌟🌟🌟🌟 and lights.✨✨✨✨\n")
        user_input_blue = input(
            'A note says:\n"The real treasure is waiting ahead."\nContinue?\n1.Yes\n2.No\n'
        )
        if "yes" in user_input_blue.lower() or "1" in user_input_blue:
            print("You find another door...")
            user_input_blue1 = input(
                'A voice asks:\n"What is the one thing you can never live without?"\n'
            )
            if (
                "sumi" in user_input_blue1.lower()
                or "sumathi" in user_input_blue1.lower()
            ):
                print(
                    "❤️ Correct!\nYou found the greatest treasure.\n----------\n-------------\nThe treasure was never gold, diamonds, or magic.\nIt was YOU.\nThanks for being part of my world. ❤️\n"
                )
            else:
                print(
                    "Congrats!!\nI expect something more precious answer\nBut still\nThe treasure was never gold, diamonds, or magic.It was YOU.\nThanks for being part of my world. ❤️"
                )
        else:
            print("End the game!!")
    else:
        print("Enter the wrong string\nEnd the game")
elif "ignore" in user_input.lower() or "2" in user_input.lower():
    print("You walk away, but your curiosity grows.\n")
    user_input_ignore = input("Do you:\n1.Go back and open it\n2.Leave it forever\n")
    if "go back" in user_input_ignore.lower() or "1." in user_input_ignore:
        print("You found the one golden key in that box\n")
        user_input_open = input(
            "You find a two doors\n------------\nDo you choose:\n1.Red door\n2.Blue door\n"
        )
        if (
            "red door" in user_input_open.lower()
            or "red" in user_input_open.lower()
            or "1" in user_input_open
        ):
            print(
                "You enter the room with full of choculates🍫🍫🍫🍫 and flowers🌷🌼🌸🌺💐🌹\n"
            )
            user_input_red = input(
                "A note says:\n------------\n-----------\nGood choice, but there is something even more valuable.\nContinue?\n1.Yes\n2.No\n"
            )
            if "yes" in user_input_red.lower() or "1" in user_input_red:
                print(
                    "You enter a room filled with stars🌟🌟🌟🌟 and lights✨✨✨✨✨✨."
                )
                user_input_red1 = input(
                    "A note says:\nThe real treasure is waiting ahead.\nContinue? \n1.Yes\n2.No\n"
                )
                if "yes" in user_input_red1.lower() or "1" in user_input_red1:
                    print("You find the another door\nYou open the final door.\n")
                    user_input_red2 = input(
                        'A voice asks:\n"What is the one thing you can never live without?"\n'
                    )
                    if "sumi" in user_input_red2 or "sumathi" in user_input_red2:
                        print(
                            "❤️ Correct!\nYou found the greatest treasure.\n-------------\n----------\nThe treasure was never gold, diamonds, or magic.It was YOU.\nThanks for being part of my world. ❤️"
                        )
                    else:
                        print(
                            "Congrats!!\nI expect something more precious answer\nBut still\nThe treasure was never gold, diamonds, or magic.It was YOU.\nThanks for being part of my world. ❤️"
                        )
                elif "no" in user_input_red1.lower() or "2" in user_input_red1:
                    print("End the game!!")
                else:
                    print("Enter the wrong string!!\nEnd the game!!")
            elif "no" in user_input_red.lower() or "2" in user_input_red:
                print("End the game!!")
            else:
                print("Enter the wrong string\nQuit the Game")

        elif (
            "blue door" in user_input_open.lower()
            or "blue" in user_input_open.lower()
            or "2" in user_input_open
        ):
            print("You enter a room filled with stars🌟🌟🌟🌟 and lights.✨✨✨✨\n")
            user_input_blue = input(
                'A note says:\n"The real treasure is waiting ahead."\nContinue?\n1.Yes\n2.No\n'
            )
            if "yes" in user_input_blue.lower() or "1" in user_input_blue:
                print("You find another door...")
                user_input_blue1 = input(
                    'A voice asks:\n"What is the one thing you can never live without?"\n'
                )
                if (
                    "sumi" in user_input_blue1.lower()
                    or "sumathi" in user_input_blue1.lower()
                ):
                    print(
                        "❤️ Correct!\nYou found the greatest treasure.\n----------\n-------------\nThe treasure was never gold, diamonds, or magic.\nIt was YOU.\nThanks for being part of my world. ❤️\n"
                    )
                else:
                    print(
                        "Congrats!!\nI expect something more precious answer\nBut still\nThe treasure was never gold, diamonds, or magic.It was YOU.\nThanks for being part of my world. ❤️"
                    )
            elif "no" in user_input_blue.lower() or "2" in user_input_blue:
                print("End the game!!")
            else:
                print("Enter the wrong string\nEnd the game!!")
    elif (
        "2" in user_input_ignore
        or "leave it forever" in user_input_ignore.lower()
        or "leave" in user_input_ignore.lower()
    ):
        print("End the game!!")
else:
    print("Enter the wrong string\nQuit the Game")
