def Sec_in_Year():
    
    #ask user to enter year
    years = int(input("Enter the number of years: "))

    days: int = 365 # Days in one year
    hours: int = 24 # Hours in Whole Day
    minutes: int = 60 # Minutes in one hour
    seconds: int = 60 # Seconds in one minute

    result = days * hours * minutes * seconds * years
    print(f"There are {result} seconds in a year!")
    
if __name__ == '__main__':
    Sec_in_Year()