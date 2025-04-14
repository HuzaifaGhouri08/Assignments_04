def main_function():
    number_collection = [1, 2, 3, 4]

    for index in range(len(number_collection)):
        current_number = number_collection[index]
        number_collection[index] = current_number * 2
 
    print(number_collection)

if __name__ == '__main__':
    main_function()