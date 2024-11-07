# Joel Hadley
# Period 3
# 02 08 2024

# Random Number Guessing Game!
game = True

while game == True:
    import random
    # Chooses Random Number
    number = random.randint(1,100)
    # Sets number of Guesses
    guesses = 5
    user_guess = -1
    while(user_guess != number and guesses > 0):
        user_guess = (int(input("Guess the Number Between 1-100: ")))
        guesses = guesses -1
        # Shows if number is too high or low
        if (user_guess > number):
            print("Too High")
        elif (user_guess < number):
            print("Too Low")
        # Shows if number is right
        else: 
            print("Congrats! You are correct! ")
            guesses = 0
    if(user_guess != number):
        print("You Lose. The number was " + str(int(number)))
    # Play Again Line
    if (guesses == 0):
        answer = (input("Play again? (y/n): "))
        if (answer == "n"):
            game = False
        if (answer == "y"):
            game = False
            game = True