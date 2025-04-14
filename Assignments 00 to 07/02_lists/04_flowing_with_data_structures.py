def add_multiple_items_to_list(the_list, item_to_add, how_many_times):
   
    for counter in range(how_many_times):
        the_list.append(item_to_add)

def main_program():
    user_message = input("Type a message you want to copy: ")
    my_collection = []
    print("The list starts empty:", my_collection)

    add_multiple_items_to_list(my_collection, user_message, 3)
    print("The list now has the copies:", my_collection)

if __name__ == "__main__":
    main_program()