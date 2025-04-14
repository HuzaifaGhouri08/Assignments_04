def main_program():
    item_collection = []
    user_input = input("Type something in: ")

    while user_input:
     
        item_collection.append(user_input)
        user_input = input("Type something else in (or just press Enter to finish): ")

    print("Here's everything you typed:", item_collection)

if __name__ == '__main__':
    main_program()