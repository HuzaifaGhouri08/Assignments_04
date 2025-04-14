INCHES_IN_FOOT: int = 12 #Global

def Measure():
    user_inp_feet: float = float(input("Enter Feet to convert into inches: "))
    calculate_inch = user_inp_feet * INCHES_IN_FOOT
    rounded_inches = round(calculate_inch, 2) #Rounds the result
    print(f"There are {rounded_inches} inches! in {user_inp_feet} feet ")

if __name__ == '__main__':
    Measure()