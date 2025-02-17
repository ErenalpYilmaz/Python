from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
make_coffee = CoffeeMaker()
money = MoneyMachine()
while True:
    user_choice = input(f"What would you like {menu.get_items()}:").lower()
    if user_choice == "report":
        make_coffee.report()
        money.report()
    elif user_choice == "off":
        print("Machine shuts down")
        break
    else:
        try:
            choice = menu.find_drink(user_choice)
            if make_coffee.is_resource_sufficient(choice):
                money.make_payment(choice.cost)
                make_coffee.make_coffee(choice)
        except Exception as ex:
            print(ex)
