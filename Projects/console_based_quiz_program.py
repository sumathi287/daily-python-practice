import sys
#global variables
target = input("Welcome to quiz program!\nDo you want to play?\n")
count = 0
temp_var = 0
score = 0
# execute the block of if else statement based on user input
if "yes" in target.lower():
    print("okay lets play :)")

    user_input = input("1.What does RAM stand for?\n")
    user_input = user_input.strip() #remove the space at the starting and ending of the string
    if user_input.upper() == "random access memory".upper():
        print("Correct!")
        score += 1
        count = count + 25  # what is the use of this 'count' variable
    else:
        print("Incorrect!")

    user_input = input('2.Which part of the computer is known as the "brain"?\n')
    user_input = user_input.strip() #remove the space at the starting and ending of the string
    if user_input.upper() == "CPU".upper():  # Nice!
        print("Correct!")
        score += 1
        count = count + 25
    else:
        print("Incorrect!")

    user_input = input('3.What does "WWW" stand for when browsing the internet?\n')
    user_input = user_input.strip() #remove the space at the starting and ending of the string
    if user_input.upper() == "World Wide Web".upper():  # Nice
        print("Correct!")
        score += 1
        count = count + 25
    else:
        print("Incorrect!")

    user_input = input(
        "4.Which device is used to physically type text into a computer?\n"
    )
    user_input = user_input.strip() #remove the space at the starting and ending of the string
    if user_input.upper() == "Keyboard".upper():
        print("Correct!")
        score += 1
        count = count + 25
    else:
        print("Incorrect!")
else:
    sys.exit("exit the code successfully!!")  # could provide exit code!
print(f"you got {score } questions is correct\n")
print(f"you got {(score /4) * 100}% score")
