# List representing the alphabet
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

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