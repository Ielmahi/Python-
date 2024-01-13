import random
import string

print("Welcome to the Password Generator")
N_letters = int(input("How many letters would like in your password :"))
N_symbols = int(input("How many symbols would you like : "))
N_digits = int(input("How many numbers would you like : "))

list_of_letters = list(string.ascii_letters)
list_of_symbols = list(string.punctuation)
list_of_digits = list(string.digits)

choice_letters = random.sample(list_of_letters, N_letters)
choice_symbols = random.sample(list_of_symbols, N_symbols)
choice_digits = random.sample(list_of_digits, N_digits)

password_list = choice_letters + choice_symbols + choice_digits
random.shuffle(password_list)

password = ""
for i in password_list:  # == password = ''.join(password_list)
    password += i

print(password)