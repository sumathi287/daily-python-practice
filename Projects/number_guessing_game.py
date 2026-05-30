import random

# global variables
i = list(range(1, 100))
random_number = random.choice(i)
print(random_number)
user_input = input("choose the random number between 1 and 100\n")
# logic for give the clue for user to find the correct number
while int(user_input) != random_number:
    if int(user_input) < random_number:
        print("Your value is very low!!\n")
        user_input = input("choose the number again\n")
    else:
        print("Your value is higher than actual number!!\n")
        user_input = input("choose the number again\n")


print(f"congratulations you found the correct number{"\U0001F44F"}{"\U0001F389"}!!!")
