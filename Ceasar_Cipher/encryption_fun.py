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