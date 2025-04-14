def count_even(lst):
  
    count = 0 

    for i in range(len(lst)):
        num = lst[i]
        if num % 2 == 0:
            count += 1
    print(f"Number of even numbers: {count}")
def get_list_of_ints():

    lst = []  # store integers
    user_input = input("Enter an integer or press enter to stop: ")  # Get user input
    while user_input != "":  # just press enter to exit
        lst.append(int(user_input))
        user_input = input("Enter an integer or press enter to stop: ") # next input
    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)


if __name__ == '__main__':
    main()