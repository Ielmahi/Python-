import os

def clear_screen():
    # Check the operating system and execute the appropriate clear screen command
    os.system('cls' if os.name == 'nt' else 'clear')

# Define functions for basic arithmetic operations
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# Define a simple calculator function
def calculator():
    # Get the first number from the user
    f_number = int(input("Enter the first number: "))
    
    # Initialize a flag for repetition
    again = False

    # Main calculator loop
    while not again:
        # Get the operation and the next number from the user
        operation = input("Pick an operation:\n+\n-\n*\n/\n")
        n_number = int(input("Enter the next number: "))

        # Perform the calculation based on the selected operation
        if operation == '+':
            result = add(f_number, n_number)
        elif operation == '-':
            result = sub(f_number, n_number)
        elif operation == '*':
            result = mul(f_number, n_number)
        elif operation == '/':
            result = div(f_number, n_number)

        # Display the result
        print(result)

        # Ask the user if they want to continue, start a new calculation, or exit
        do_it_again = input(f"Enter 'y' to continue with {result}, 'n' to start a new calculation, or 'x' to exit: ")

        # Update variables based on user input
        if do_it_again == 'y':
            f_number = result
            clear_screen()
        elif do_it_again == 'n':
            again = True
            clear_screen()
            calculator()
        elif do_it_again == 'x':
            again = True
            print("Bye!")

# Start the calculator
calculator()
