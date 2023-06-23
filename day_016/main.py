"""
OOP Coffee Machine by Benedict Castro | benedict.zcastro@gmail.com
"""
import sys

# Import needed modules
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    """ OOP Coffee Machine"""

    # Create objects from the given classes above
    # menu_item = MenuItem()
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    machine_running = True
    while machine_running:  # Main program loop

        # Ask user for their order
        user_order = input(f"What would you like? ({menu.get_items()}): ")
        if user_order.lower() == "off":
            sys.exit()
        elif user_order.lower() == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            chosen_drink = menu.find_drink(user_order)
            # Check if there are enough resources for the chosen drink
            if coffee_maker.is_resource_sufficient(chosen_drink) and money_machine.make_payment(chosen_drink.cost):
                coffee_maker.make_coffee(chosen_drink)


# If program is run (instead of imported), run the program
if __name__ == "__main__":
    main()





