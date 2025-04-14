import random

NUM_SIDES = 6

def roll_dice():
    
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Inside roll_dice(): Die 1 = {die1}, Die 2 = {die2}, Total = {total}")

def main():

    die1 = 10
    print(f"Inside main(): die1 starts as = {die1}")

    # Call the roll_dice() function 3 times.
    roll_dice()
    roll_dice()
    roll_dice()

    # Show that the value of die1 in main() remains unchanged.
    print(f"Inside main(): die1 is now = {die1}")

if __name__ == "__main__":
    main()