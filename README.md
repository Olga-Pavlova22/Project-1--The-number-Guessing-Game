"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.
import random

guess_attempts = 0

# Create the start_game function.
def start_game():
 # Write your code inside this function.

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
    print ("Welcome To The Number Guessing Game")
    print ("Menu: ")
    print ("1: Play game")
    print ("2: Quit")
    choice = input("Please choose the menu option: ")
    if choice == "1":
#   2. Store a random number as the answer/solution.
        random_number = random.randint(1, 10)
#   3. Continuously prompt the player for a guess.
        while number_guess != random_number:
            number_guess = int(input("Please guess the number from 1-10: "))
            guess_attempt += 1
            print(number_guess)
 #     a. If the guess is greater than the solution, display to the player "It's lower".
            if number_guess > 10;
                print("This number is too high, please pick lower number: ")
 #     b. If the guess is less than the solution, display to the player "It's higher".
            else number_guess < 1;
                print("This number is too low, please pick higher number: ")
 #   4. Once the guess is correct, stop looping, inform the user they "Got it"
 #      and show how many attempts it took them to get the correct number.
        else:
            print(f"Well done! Your guess matches the random number! It took you {guess_attempts} to get the correct number.")
#   5. Let the player know the game is ending, or something that indicates the game is over.
    else choice == "2":
        print("Game is quitting.")
        break
# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
start_game()
