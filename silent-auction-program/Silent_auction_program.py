import os

def clear_screen():
    # Check the operating system and execute the appropriate clear screen command
    os.system('cls' if os.name == 'nt' else 'clear')

print("***** Welcome to the Silent Auction Program *****")

# Initialize the bidding process
more_bidders = False
all_bids = {}

# Continue collecting bids until there are no more bidders
while not more_bidders:
    # Clear the console screen before taking input for the next bidder
    clear_screen()

    # Get bidder information
    bidder_name = input("Enter your name: ")
    bid_amount = int(input("Enter your bid: "))
    all_bids[bidder_name] = bid_amount

    # Check if there are more bidders
    user_response = input("Are there any other bidders? Type 'yes' or 'no': ")

    # Set more_bidders based on user response
    if user_response.lower() == 'yes':
        more_bidders = False
    else:
        more_bidders = True

# Determine the highest bid and winner
winner_name = max(all_bids, key=all_bids.get)
winning_bid = all_bids[winner_name]

# Clear the console screen before displaying the result
clear_screen()

# Display the winner and winning bid
print(f"The winner is {winner_name} with a bid of {winning_bid}")
