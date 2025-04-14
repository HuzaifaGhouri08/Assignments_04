# Project 2 : Guess The Number (computer),
# Created By Huzaifa Ghouri (419013)

import random

def guess_the_number():
    # Computer guesses a number you think of between 1 and 50.

    print("Think of a number between 1 and 50.")
    print("I will try to guess it.")
    print("Answer with 'H' if my guess is too high, 'L' if it's too low, and 'C' if it's correct.")

    low = 1
    high = 50
    attempts = 0

    while True:
        guess = (low + high) // 2
        attempts += 1
        print(f"Is your number {guess}?")
        feedback = input("Enter H, L, or C: ").lower()

        if feedback == 'c':
            print(f"I guessed it! Your number was {guess}, and it only took me {attempts} attempts!")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Invalid input. Please enter 'H', 'L', or 'C'.")

if __name__ == "__main__":
    guess_the_number()