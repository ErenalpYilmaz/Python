from logo import logo
print(logo)

# TODO-1: Ask the user for input
def take_people(dictionary):
    name = input("What is your name?:")
    price = int(input("What is your bid?:$"))
    dictionary[name] = price
    return dictionary
def max_value(dictionary):    
    max_price = 0
    winner = {}
    for key in dictionary:
        if dictionary[key] > max_price:
            max_price = dictionary[key]

    for key in dictionary:
        if dictionary[key] == max_price:
            winner[key] = max_price
    return winner


isDone = False
people_dictionary = {}
while not isDone:
    take_people(people_dictionary)
    done = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    print("\n"*100)
    if done == "no":
        isDone = True

winner_people = max_value(people_dictionary)
for winner in winner_people:
    print(f"The winner is {winner} with a bid of ${winner_people[winner]}")




