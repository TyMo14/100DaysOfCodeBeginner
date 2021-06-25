import random

print("\nWelcome to the Password Generator\n")

password_length = int(input("How many letters would you like in your password?\n"))
symbol_count = int(input("How many symbols would you like in your password?\n"))
number_count = int(input("How many numbers would you like in your password?\n"))

password_list = []
password = ""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

for number in range(password_length):

    if number < password_length - symbol_count - number_count:
        val = letters[random.randint(0,len(letters)-1)]
    elif number < password_length - symbol_count:
        val = numbers[random.randint(0,len(numbers)-1)]
    elif number < password_length:
        val = symbols[random.randint(0,len(symbols)-1)]

    password_list.append(val)


shuffled_password_list = random.sample(password_list,len(password_list))
# print(shuffled_password_list)

for n in range(password_length):
    password = password + shuffled_password_list[n]

print(f"\nHere is your new password: {password}")