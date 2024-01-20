import encryption_fun
import decryption_fun
"""
# List representing the alphabet
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Function for encryption
def encryption(text, shift_N):
    cipher_text = ""
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = (position + shift_N) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += i

    print(f"Here is the text after encryption: {cipher_text}")

# Function for decryption
def decryption(text, shift_N):
    normal_text = ""
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = (position - shift_N) % 26
            normal_text += alphabet[new_position]
        else:
            normal_text += i

    print(f"Here is the text after decryption: {normal_text}")
"""
# Flag to control the main loop
wanna_end = False

# Main loop
while not wanna_end:
    # User input for encryption or decryption
    select_type = input("Type 'encrypt' for encryption, type 'decrypt' for decryption: ")
    
    # User input for the message
    input_string = input("Type your message: ")
    
    # User input for the shift number
    shift_N = int(input("Type your shift number: "))
    
    # Perform encryption or decryption based on user input
    if select_type == 'encrypt':
        encryption_fun.encryption(input_string, shift_N)
    elif select_type == 'decrypt':
        decryption_fun.decryption(input_string, shift_N)
    
    # Ask if the user wants to play again
    play_again = input("Type 'yes' to continue, type 'no' to exit.\n")
    
    # Check if the user wants to end the program
    if play_again == 'no':
        wanna_end = True
        print("Have a nice day! Bye")
