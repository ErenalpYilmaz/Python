from art import logo , vs
from game_data import data
import random

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name},{account_description},from {account_country}"

def check_answer(guess ,a_fallower,b_fallower):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_fallower > b_fallower:
        return guess == "a"
    else:
        return guess == "b"

game_should_continue = True

score = 0

# Generate a random account from the game data
b_account = random.choice(data)

print(logo)

while game_should_continue:

    # Making account at position B become the next account at position A.
    a_account = b_account
    b_account = random.choice(data)
    
    if a_account == b_account:
        b_account = random.choice(data)
    
    
    print(f"Compare A: {format_data(a_account)}")
    print(vs)
    print(f"Compare B: {format_data(b_account)}")    
    
    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B':").lower()
    
    # Clear the screen
    print("\n" * 20)
    print(logo)
    
    # - Get follower count of each account
    a_account_follower = a_account["follower_count"]
    b_account_follower = b_account["follower_count"]
    
    # Check if user is correct.
    is_correct = check_answer(guess,a_account_follower,b_account_follower)

    # Give user feedback on their guess.
    # score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score:{score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False