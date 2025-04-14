import random

NUM_SIDES = 6  # Each die has 6 sides

def Roll_The_Dice():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)

    total = die1 + die2

    # Show the results.
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total:", total)

if __name__ == '__main__':
    Roll_The_Dice()