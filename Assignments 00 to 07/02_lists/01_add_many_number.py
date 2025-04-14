def sum_all_numbers(number_list):

    current_total = 0
    for each_number in number_list:
        current_total += each_number
    return current_total

def main_function():
    my_numbers = [1, 2, 3, 4, 5, 0, 4, 1]
    total_of_my_numbers = sum_all_numbers(my_numbers)
    print(total_of_my_numbers)

if __name__ == '__main__':
    main_function()