def double(num):
    return  num * 2
    
def main():
    num = int(input("Enter an integer: "))
    double_num = double(num)
    print(f"Double that is {double_num}")

if __name__ == '__main__':
    main()