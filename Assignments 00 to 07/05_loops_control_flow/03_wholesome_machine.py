AFFIRMATION : str = "I'm Developer"

def Affr():
    print("Please type the following affirmation: " + AFFIRMATION)

    user_feedback = input()
    while user_feedback != AFFIRMATION:
        print("That was not the affirmation.")

        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()

    print("That's right! :)")

if __name__ == '__main__':
    Affr()