target = input("Welcome to quiz program!\nDo you want to play?\n")
count = 0
temp_var = 0
score = 0
if target == "yes":
    print("okay lets play :)")
    user_input = input("1.What does RAM stand for?\n")
    if user_input.upper() == "random access memory".upper():
        print("Correct!")
        score += 1
        count = count + 25
    else:
        print("Incorrect!")
    user_input = input('2.Which part of the computer is known as the "brain"?\n')
    if user_input.upper() == "CPU".upper():
        print("Correct!")
        score += 1
        count = count + 25
    else:
        print("Incorrect!")
    user_input = input('3.What does "WWW" stand for when browsing the internet?\n')
    if user_input.upper() == "World Wide Web".upper():
        print("Correct!")
        score += 1
        count = count + 25
    else:
        print("Incorrect!")
    user_input = input(
        "4.Which device is used to physically type text into a computer?\n"
    )
    if user_input.upper() == "Keyboard".upper():
        print("Correct!")
        score += 1
        count = count + 25
    else:
        print("Incorrect!")
    user_input = input("5.What is something you simply cannot live without??\n")
    if user_input.upper() == "sumi".upper() or user_input.upper() == "sumathi".upper():
        print(f"Correct Honey...{"\u2665"}{"\u2665"}{"\u2665"}!")
        score += 1
        count = count + 25
    else:
        print("Incorrect,I realy hate you...!")
else:
    quit()
print(f"you got {score } questions is correct\n")
print(f"you got {(score /5) * 100} %")
