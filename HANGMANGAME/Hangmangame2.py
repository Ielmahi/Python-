import random
import HANGMANPICS

print("Welcome to the hangman game")
lives = 6
words = ['apple', 'banana', 'cherry', 'date', 'potato']
gen_word = random.choice(words)
blanks = "_" * len(gen_word)  # Use string multiplication to create blanks

guessed_letters = []  # Track the guessed letters

while "_" in blanks:  # Loop until all blanks are filled
    print("Current progress:", blanks)
    user_letter = input("Enter a letter: ")

    if len(user_letter) != 1:
        print("Please enter a single letter.")
        continue

    if user_letter in guessed_letters:
        print("You have already guessed that letter.")
        continue

    guessed_letters.append(user_letter)

    if user_letter in gen_word:
        # Reveal the correct letter in the blanks
        blanks = "".join(
            letter if letter == user_letter else blank
            for letter, blank in zip(gen_word, blanks)
        )
    else:
        lives -= 1
        print("Wrong guess.")
        print(HANGMANPICS.PICS[lives])

    if lives == 0:
        break

print("Congratulations! You guessed the word:", gen_word)