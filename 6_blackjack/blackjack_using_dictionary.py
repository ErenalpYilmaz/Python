from art import logo
import random


isFinish = False
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def game_cards():
    game["user1"].append(random.choice(cards))
    game["user1"].append(random.choice(cards))
    if sum(game["user1"]) > 21:
        game["user1"][1] = 1
    game["computer"].append(random.choice(cards))
    game["computer"].append(random.choice(cards))
    if sum(game["computer"]) > 21:
        game["computer"][1] = 1
    return game

def add_card(dictionary,key):
    next_card = random.choice(cards)
    if next_card == 11 and sum(dictionary[key])+11 > 21:
        next_card = 1
    dictionary[key].append(next_card)
    return dictionary

def start_game_status():
    print(f"Your cards: {game_user["user1"]}, current score:{sum(game_user["user1"])}")
    print(f"Computer's first card:{game_user["computer"][0]}")

def end_game_status():
    print(f"Your cards: {game_user["user1"]}, final score:{sum(game_user["user1"])}")
    print(f"Computer's final hand:{game_user["computer"]} final score: {sum(game_user["computer"])}")
def calculate_score(dictionary,key):
    return sum(dictionary[key])

def compare():
    if calculate_score(game_user, "computer") == calculate_score(game_user,"user1"):
        end_game_status()
        print("Draw :D")
    elif calculate_score(game_user, "computer") < calculate_score(game_user,"user1"):
        end_game_status()
        print("You win :D")
    elif calculate_score(game_user, "computer") > calculate_score(game_user,"user1"):
        end_game_status()
        print("Computer win :D\nYou Lose :C")

user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n' :")

if user_choice == 'n':
    isFinish = True
else:
    print(logo)

while not isFinish:
    game = {
        "user1": [],
        "computer": [],
    }
    game_user = game_cards()
    start_game_status()
    another_card = input("Type 'y' to get another card,type 'n' to pass:")

    if another_card == "y":
        add_card(game_user,"user1")
        if sum(game_user["user1"]) > 21:
            end_game_status()
            print("You went over. You lose !")
    elif another_card == "n":
        while sum(game_user["computer"]) < 17:
            add_card(game_user,"computer")
        if calculate_score(game_user,"computer") <= 21:
            compare()
        else:
            end_game_status()
            print("You Win")
    user_ = input("Do you want to play a game of Blackjack? Type 'y' or 'n' :")
    if user_ == 'n':
        isFinish = True
    else:
        print(logo)