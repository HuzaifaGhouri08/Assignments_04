def add_contact(phonebook):
  name = input("Enter Contact Name:")
  number = input("Enter Contact Number:")

  if name in phonebook:
    print(f"{name} Alrady Exists in the phonebook.")
  else:
    phonebook[name] = number
    print(f"{name} Added to the phonebook.")

def search_contact(phonebook):
  name = input("Enter Contact Name:")
  number = input("Enter Contact Number:")

  if name in phonebook:
    print(f"{name}: {phonebook[name]}")

  else:
    print(f"{name} Not Found in the phonebook.")



def delete_contact(phonebook):
  name = input("Enter Contact Name:")
  if name in phonebook:
    del phonebook[name]
    print(f"{name} Deleted from the phonebook.")
  else:
    print(f"{name} Not Found in the phonebook")


def display_contact(phonebook):
  if phonebook:
    print("\nPhonebook Contacts List:")
    for name,number in phonebook.items():
      print(f"{name}: {number}")
  else:
    print("Phonebook is Empty.")


if __name__ == "__main__":
  phonebook = {}



  while True:
    print("\nPhoneBook Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")


    choice = input("Enter your choice (1/2/3/4/5):")
    if choice == "1":
      add_contact(phonebook)
    elif choice == "2":
      search_contact(phonebook)
    elif choice == "3":
      delete_contact(phonebook)
    elif choice == "4":
      display_contact(phonebook)
    elif choice == "5":
      print("Exiting Phonebook. Goodbye!")
      break

    else:
      print("Invalid Choice. Please select a valid option.")
