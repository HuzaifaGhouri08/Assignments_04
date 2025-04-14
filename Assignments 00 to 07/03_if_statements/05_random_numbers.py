import random

def random_number():
  for index in range(10):
    number:int = random.randint(1,100)
    print(number)

if __name__ == "__main__":
  random_number()