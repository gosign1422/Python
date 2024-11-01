import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the UnPwnable Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

password = ""

#EASY MODEL
for char in range(0,nr_letters):
    password += random.choice(letters)
for char in range(0,nr_numbers):
    password += random.choice(numbers)
for char in range(0,nr_symbols):
    password += random.choice(symbols)
print(f"Easy:{password}")



# #TOUGH MODEL

# METHOD-1
# password1=""
# pass_list=list(password)
# random.shuffle(pass_list)
# for char in pass_list:
#     password1 += char
# print(f"Tough:{password1}")

# METHOD-2
password_list = []
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))
for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))
for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

passw = ""
for char in password_list:
    passw += char
print(f"Tough:{passw}")


