# Project 4 : Rock, paper & Scissors Game,
# Created By Huzaifa Ghouri (419013)

import random

def rock_paper_scissors():
    # Rock, Paper and Scissors Game

    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors), or 'q' to quit: ").lower()

        if user_choice == 'q': # if you want to Exit the game
            print("Thanks for playing!")
            break

        if user_choice not in choices: # If user has given wrong input.
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices) # Generate random choice

        print(f"You chose: {user_choice}") # your Choice
        print(f"Computer chose: {computer_choice}") # Computer Choice

        if user_choice == computer_choice: #game logic
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")

if __name__ == "__main__":
    rock_paper_scissors()