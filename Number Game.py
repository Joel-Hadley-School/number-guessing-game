# Joel Hadley
# 02 08 2024
# (Originally Made for my 3rd Period Computer Science)

# Random Number Guessing Game!
game = True

while game == True:
    import random
    # Chooses Random Number in range
    number = random.randint(1,100) 
    # Change number range here ^^^. 
        # - Only works with integers, not floats (whole numbers, not decimal numbers)
        # - ALSO 1 MUST BE MINIMUM
        # - Be sure to change the input() text on line 19 to "Guess the Number Between 1-[number]" instead of 1-100.
    guesses = 5 # Set number of Guesses
    user_guess = -1 # Subtracts 1 from total guesses every time you guess
    while(user_guess != number and guesses > 0): # This loop repeats until either the guess is correct, or the player runs out of guesses.
        user_guess = (int(input("Guess the Number Between 1-100: "))) # Input number here
        guesses = guesses -1
        # Shows if number is too high or low
        if (user_guess > number):
            print("Too High")
        elif (user_guess < number):
            print("Too Low")
        # Shows if number is right
        else: 
            print("Congrats! You are correct! ")
            guesses = 0 # Resets guesses so the game can be replayed
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
