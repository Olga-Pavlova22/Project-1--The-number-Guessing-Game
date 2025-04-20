import random

guess_attempts = 0

def start_game():
    print ("Welcome To The Number Guessing Game")
    print ("Menu: ")
    print ("1: Play game")
    print ("2: Quit")
    choice = input("Please choose the menu option: ")
    if choice == "1":
        random_number = random.randint(1, 10)

        while number_guess != random_number:
            number_guess = int(input("Please guess the number from 1-10: "))
            guess_attempt += 1
            print(number_guess)
            if number_guess > 10:
                print("This number is too high, please pick lower number: ")
            else number_guess < 1:
                print("This number is too low, please pick higher number: ")
        else:
            print(f"Well done! Your guess matches the random number! It took you {guess_attempts} to get the correct number.")
    else choice == "2":
        print("Game is quitting.")
        
        break
start_game()
