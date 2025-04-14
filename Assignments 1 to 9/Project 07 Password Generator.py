# Project 7 : Random Password Generator,
# Created By Huzaifa Ghouri (419013)

import random
import string

def password_generator(length):
  combination = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(combination) for i in range(length))
  return password

print(password_generator(12)) # Generate 12-Characters Password