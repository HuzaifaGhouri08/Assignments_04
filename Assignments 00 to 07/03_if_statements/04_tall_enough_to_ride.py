MINIMUM_HEIGHT_INCHES : int = 60 # Minimum height in inches (5 feet * 12 inches/foot)

def main():
    height_input = input("How tall are you? Please enter your height in feet and inches (e.g., 5.2 for 5 feet and 2 inches): ")
    parts = height_input.split('.')
    if len(parts) == 2:
        feet = int(parts[0])
        inches = int(parts[1])
        total_height_inches = (feet * 12) + inches

        if total_height_inches >= MINIMUM_HEIGHT_INCHES:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")
    
    else:
        print("Invalid height format. Please use the format 'feet.inches' (e.g., 5.2).")

if __name__ == '__main__':
    main()