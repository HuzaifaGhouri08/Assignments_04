# Project 5 : HangMan Game,
# Created By Huzaifa Ghouri (419013)

import random

def hangman():
    # Hangman game.

    words = ["python", "hangman", "programming", "giaic", "computer", "keyboard", "mouse", "developer", "algorithm"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 8

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while attempts > 0:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print("\nWord:", display_word)
        print("Attempts left:", attempts)

        if "_" not in display_word:
            print("Congratulations! You guessed the word:", secret_word)
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print("Incorrect guess.")

    if attempts == 0:
        print("\nGame over! The secret word was:", secret_word)

if __name__ == "__main__":
    hangman()