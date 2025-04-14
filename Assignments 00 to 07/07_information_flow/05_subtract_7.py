def subtract_seven(num):
    return num - 7

def main():
    num = int(input("Enter a number: "))
    subtract = subtract_seven(num)
    print("Result: ", subtract)

if __name__ == '__main__':
    main()