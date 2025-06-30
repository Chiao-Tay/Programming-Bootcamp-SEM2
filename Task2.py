"""
Number Guessing Game (1–100)

This simple Python game selects a random number between 1 and 100,
and the player tries to guess it. After each guess, the program tells
the player if the correct number is higher or lower than their guess.
It continues until the player gets it right.

Intuition:
The game uses a loop to keep prompting the user for input. Each guess
is checked against the target number, and a helpful message is printed
until the correct number is guessed. This teaches loops, conditionals,
and user input handling in Python.
"""

import random  # Import the random module to generate random numbers

def generate_number():
    """
    Generates a random integer between 1 and 100 (inclusive).
    """
    return random.randint(1, 100)

def get_guess():
    """
    Prompts the user for a guess and checks if it's a valid integer between 1 and 100. 
    Keeps asking until valid input is given.
    """
    while True:
        user_input = input("Enter your guess (1 to 100): ")
        if user_input.isdigit(): # check if user input is digit
            guess = int(user_input) # convert the input from string to integer
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number within the range 1–100.")
        else:
            print("Invalid input. Please enter a whole number.")

def check_guess(guess, target):
    """
    Compare user guess with the target and print a hint after the comparison.
    """
    if guess < target:
        print("Try a higher number.")
    elif guess > target:
        print("Try a lower number.")
    else:
        print("Congratulations! You got it!")

def play_guessing_game():
    """
    Runs the number guessing game until the user guesses correctly.
    """
    display_welcome_message()
    target = generate_number()
    attempts = 0  # keep track of how many guesses the user makes to guess the number

    while True:
        guess = get_guess()
        attempts += 1
        check_guess(guess, target)

        if guess == target:
            print(f"Well done! You guessed it in {attempts} attempt(s).")
            break  # exit the loop if guessed correctly

def display_welcome_message():
    """Display the welcome message and game instructions."""
    print("Welcome to the Number Guessing Game!")
    print("Try to guess a number between 1 and 100.")

if __name__ == "__main__":
    play_guessing_game()
