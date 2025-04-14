# Voting ages in different countries
Scotland = 16
Turkey = 18
Malaysia = 21

def main():
    user_age = int(input("How old are you? "))

    # Check if the user can vote in the Scotland.
    if user_age >= Scotland:
        print(f"You can vote in the Scotland where the voting age is {Scotland}.")
    else:
        print(f"You can't vote in the Scotland where the voting age is {Scotland}.")

    # Check if the user can vote in Turkey.
    if user_age >= Turkey:
        print(f"You can vote in Turkey where the voting age is {Turkey}.")
    else:
        print(f"You can't vote in Turkey where the voting age is {Turkey}.")

    # Check if the user can vote in Malaysia.
    if user_age >= Malaysia:
        print(f"You can vote in Malaysia where the voting age is {Malaysia}.")
    else:
        print(f"You can't vote in Malaysia where the voting age is {Malaysia}.")

if __name__ == '__main__':
    main()