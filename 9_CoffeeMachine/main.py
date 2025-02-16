from coffeInfo import MENU , resources


def machineInfo(money):
    """It gives you the information about our coffee machine."""
    machine_water = res["water"]
    machine_milk = res["milk"]
    machine_coffee = res["coffee"]
    return  f"Machine resources\nwater: {machine_water}\nmilk: {machine_milk}\ncoffee: {machine_coffee}g\nmoney: {money}$"



def check_resources(choice):
    """Controls the resources in the coffee machine"""
    accept = True
    for machine in resources:
        if choice != "espresso" and machine != "milk":
            if resources[machine] < MENU[choice]["ingredients"][machine]:
                accept = False
    return accept

def use_resources(user_choice):
    for source in res:
        if user_choice == "espresso" and source == "milk": 
            continue
        else:
            res[source] -= MENU[user_choice]["ingredients"][source]
        
    return res
def get_coins(price):
    """Fees are charged. It compares the fee total with the product fee."""
    result = 0
    coins = {
        "quarters":0.25,
        "dimes":0.10,
        "nickles":0.05,
        "pennies":0.01,
    }
    
    for step in coins:
        coins[step] *= int(input(f"How many{step}:"))
    for step in coins:
        result += coins[step]
        
    if price < result:
        return round(result - price,2)
    else:
        return False
    
res = resources
should_continue = True
money = 0

while should_continue:
    user_choice = input("What would you like (espresso/latte/cappuccino):").lower()

    if user_choice == "report":
        print(machineInfo(money))
    elif user_choice == "off":
        print("Machine shuts down")
        break
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        if check_resources(user_choice):
            result = get_coins(MENU[user_choice]["cost"])
            if result:
                print(f"Here is {result}$ in change.")
                money += MENU[user_choice]["cost"]
                res = use_resources(user_choice)
                print(f"Here is your {user_choice}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is not enough {user_choice}")
            
    