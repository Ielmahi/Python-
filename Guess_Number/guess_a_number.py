import random
import pic_Guess_N

random_number = random.randint(1, 51)
print(pic_Guess_N.pic)
print("Let me think of a number between 1 to 50")
difficulty = input("Choose level of difficulty 'easy' or 'hard': ")

def guess_again(attempts):
    if attempts <= 0:
        print(f"Sorry, you've run out of attempts. The correct answer was {random_number}")
    else:
        print(f"You have {attempts} attempts")
        try:
            guess = int(input("Make a guess: "))
            if guess == random_number:
                print(f"Your guess is correct! The answer is {random_number}")
            elif guess > random_number:
                print("Your guess is too high.")
                if attempts > 1:  # Print "Guess again" only when attempts are greater than 1
                    print("Guess again.")
                guess_again(attempts - 1)
            elif guess < random_number:
                print("Your guess is too low.")
                if attempts > 1:  # Print "Guess again" only when attempts are greater than 1
                    print("Guess again.")
                guess_again(attempts - 1)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            guess_again(attempts)

if difficulty == 'easy':
    guess_again(10)
elif difficulty == 'hard':
    guess_again(5)
else:
    print("Invalid difficulty level. Please choose 'easy' or 'hard'.")
    # Add code here to handle invalid input, like exiting the program or asking the user to input the difficulty again.
