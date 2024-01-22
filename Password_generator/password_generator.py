import random
import string

print("Welcome to the Password Generator")
#print('_' * 33)

num_letters = int(input("How many letters would you like in your password: "))
num_symbols = int(input("How many symbols would you like: "))
num_digits = int(input("How many numbers would you like: "))

#print('_' * 33)
print("Generating password...")

letters = list(string.ascii_letters)
symbols = list(string.punctuation)
digits = list(string.digits)

chosen_letters = random.sample(letters, num_letters)
chosen_symbols = random.sample(symbols, num_symbols)
chosen_digits = random.sample(digits, num_digits)

password_list = chosen_letters + chosen_symbols + chosen_digits
random.shuffle(password_list)
password = ''.join(password_list)

#print('_' * 33)
print("Generated Password:")
print(password)
