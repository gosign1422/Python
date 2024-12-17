import random
from typing import final

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# EASY
pass_easy=""
for lett in range(1,nr_letters+1): #OR for lett in range(0,nr_letters):
    pass_easy += random.choice(letters)

for sym in range(1,nr_symbols+1):
    pass_easy += random.choice(symbols)

for num in range(1,nr_numbers+1):
    pass_easy += random.choice(numbers)

print(f"Easy Password: {pass_easy}")

# TOUGH
tough_list=list(pass_easy)    #Converting the string into a List
random.shuffle(tough_list)    #Shuffles all the items in a List
pass_tough=""
for passw in tough_list:
    pass_tough += passw
print(f"Tough Password: {pass_tough}")
