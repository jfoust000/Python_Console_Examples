import random

y = random.randint(1, 10)

while (True):

    user_input = input("Enter a number between 1 and 10: ")
    
    if (int(user_input) < y):

        print("Too low")

    elif (int(user_input) > y):

        print("Too high")

    else:

        print("You entered: " + str(user_input) + " and the number is " + str(y))
        break