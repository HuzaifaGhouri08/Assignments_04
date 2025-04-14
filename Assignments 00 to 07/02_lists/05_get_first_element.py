def get_first_element(list):
  if list:
    print(list[0])
  else:
    print("List is empty")

def get_list():
  lst = []
  element:str=input("Enter an element to add to the list:")
  while element !="":
    lst.append(element)
    element = input("Enter an element to add to the list (or press Enter to finish):")
  return lst

def main():
  list =get_list()
  get_first_element(list)

if __name__ == "__main__":
  main()