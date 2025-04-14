def in_range(num, low, high):

    if num >= low and num <= high:
        return True
    else:
        return False

def main_program():
    number = int(input("Enter any number: "))
    lower_limit = int(input("Enter the lower limit: "))
    upper_limit = int(input("Enter the upper limit: "))
    result = in_range(number, lower_limit, upper_limit)

    print(result)
    
if __name__ == '__main__':
    main_program()