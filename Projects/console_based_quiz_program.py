# it would be nice to have description of project

target = input("Welcome to quiz program!\nDo you want to play?\n")
count = 0
temp_var = 0
score = 0

if "yes" in target.lower():
    print("okay lets play :)")

    user_input = input("1.What does RAM stand for?\n")
    if user_input.upper() == "random access memory".upper():
        print("Correct!")
        score += 1
        count = count + 25 # what is the use of this 'count' variable
    else:
        print("Incorrect!")
        
    user_input = input('2.Which part of the computer is known as the "brain"?\n')
    if user_input.upper() == "CPU".upper(): #Nice!
        print("Correct!")
        score += 1
        count = count + 25
    else:
        print("Incorrect!")
        
    user_input = input('3.What does "WWW" stand for when browsing the internet?\n')
    if user_input.upper() == "World Wide Web".upper(): # Nice
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
    if user_input.upper() == "sumi".upper() or user_input.upper() == "sumathi".upper(): # very very nice
        print(f"Correct Honey...{"\u2665"}{"\u2665"}{"\u2665"}!") # especially this one - you had explored ascii characters to do this special ssymbol insertion!
        score += 1
        count = count + 25
    else:
        print("Incorrect,I realy hate you...!") # cutest part of the code!
        
else:
    quit() # could provide exit code!
print(f"you got {score } questions is correct\n")
print(f"you got {(score /5) * 100} %")
