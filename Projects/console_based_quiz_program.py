target = input(
    'Welcome to quiz program!\nEnter "yes" if you want to play quiz \nEnter "no" or any charecter to quit the quiz"\n'
)
count = 0
temp_var = 0
count_1 = 0
if target == "yes":
    user_input = input("1.What does RAM stand for?\n")
    if user_input.upper() == "random access memory".upper():
        print("the answer is correct")
        count_1 = +1
        count = count + 25
    else:
        print("The answer is incorrect\n")
    user_input = input('2.Which part of the computer is known as the "brain"?\n')
    if user_input.upper() == "CPU".upper():
        print("The answer is correct")
        count_1 = +count_1
        count = count + 25
    else:
        print("The answer is incorrect\n")
    user_input = input('3.What does "WWW" stand for when browsing the internet?\n')
    if user_input.upper() == "World Wide Web".upper():
        print("The answer is correct")
        count_1 = +count_1
        count = count + 25
    else:
        print("The answer is incorrect\n")
    user_input = input(
        "4.Which device is used to physically type text into a computer?\n"
    )
    if user_input.upper() == "Keyboard".upper():
        print("The answer is correct")
        count_1 = +count_1
        count = count + 25
    else:
        print("The answer is incorrect\n")
else:
    print("Exit from the quiz program\n")
print(f"the total correct answers is {count_1}\n")
print(f"the total percentage of correct answer is {count}%\n")
print("End the quiz!!")
