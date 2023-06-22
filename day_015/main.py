"""
Coffee Machine, by Benedict Castro | benedict.zcastro@gmail.com
A digital coffee machine.
"""

# Import needed modules
import proj_art
import proj_menu
import sys


def main():
    """Coffee Machine Project
    by Benedict Castro | benedict.zcastro@gmail.com"""

    print(proj_art.logo)
    print("Welcome to Milyastroc's Coffee Machine!")

    def ask_user(available, resources, money):
        """This function asks the user to provide the coffee type of choice."""
        choice = input(f"What would you like? {available}: ")

        while choice not in available:
            if choice.lower() == "off":  # The program exits with this choice
                sys.exit()
            if choice.lower() == "report":  # Generate report if this is the choice
                generate_report(resources, money)
            choice = input(f"Please choose from the ones available {available}: ")
        return choice

    def check_availability(resources, menu):
        """This function returns which of the coffee recipes are still available given the resources left."""
        available = []
        # Extract ingredients from the coffee types and store in separate variables
        cappuccino_ing = menu["cappuccino"]["ingredients"]
        latte_ing = menu["latte"]["ingredients"]
        espresso_ing = menu["espresso"]["ingredients"]

        # Check if the resources are still sufficient for each type
        cap = 0
        lat = 0
        esp = 0
        for ing in resources.keys():
            if resources[ing] >= cappuccino_ing[ing]:
                cap += 1
                if cap == 3:
                    available.append("cappuccino")
            if resources[ing] >= latte_ing[ing]:
                lat += 1
                if lat == 3:
                    available.append("latte")
            if resources[ing] >= espresso_ing[ing]:
                esp += 1
                if esp == 3:
                    available.append("espresso")

        return available

    def generate_report(resources, money):
        """This function returns a report indicating how many of each resource is left."""
        print(f"Water:\t{resources['water']}ml")
        print(f"Milk:\t{resources['milk']}ml")
        print(f"Coffee:\t{resources['coffee']}g")
        print(f"Money:\t{money}$")

    def ask_payment(choice, menu):
        """This function asks the user for the payment and processes it. It returns the profit from a purchase."""
        profit = 0
        print("Please insert coins.")
        num_quarters = int(input("How many quarters?: "))
        num_dimes = int(input("How many dimes: "))
        num_nickles = int(input("How many nickles?: "))
        num_pennies = int(input("How many pennies?: "))

        # Process the coins payment
        total_amount = (num_quarters * 0.25) + (num_dimes * 0.10) + (num_nickles * 0.05) + (num_pennies * 0.01)
        coffee_cost = menu[choice]["cost"]

        if total_amount < coffee_cost:
            print(f"The coffee you want is {coffee_cost}$ and you inserted only {total_amount}$."
                  f"Sorry that's not enough money. Money refunded.")
        else:
            if total_amount > coffee_cost:
                print(f"Here is {total_amount-coffee_cost:.2f}$ in change.")
            profit += coffee_cost
            print(f"Here is your {choice}. Enjoy! ☕")

        return profit

    def deduct_resources(choice, resources, menu):
        """This functions manages the amount of resources. It deducts the used resources based on the purchase made
        from the total left resources. It returns a dictionary which contains the resources left."""
        for ing in resources.keys():
            resources[ing] -= menu[choice]["ingredients"][ing]
        return resources

    # Keep track of profits and resources
    coffee_profit = 0

    run_machine = True
    while run_machine:  # Main loop

        # Define coffee machine details
        coffee_resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        coffee_menu = proj_menu.MENU

        is_sufficient = True  # This pertains to the resources if there are still enough for the machine to function properly
        while is_sufficient:
            coffee_options = check_availability(coffee_resources, coffee_menu)
            if len(coffee_options) == 0:  # If there are not enough resources to produce coffee
                is_sufficient = False
                print("There are not enough resources to process your possible orders. Sorry for the inconvenience")
            else:  # Ask user for their coffee of choice
                user_choice = ask_user(coffee_options, coffee_resources, coffee_profit)

                # Ask user for payment
                earned_money = ask_payment(user_choice, coffee_menu)
                coffee_profit += earned_money

                # Deduct the resources currently used from the initial amounts of each
                if earned_money != 0:
                    coffee_resources = deduct_resources(user_choice, coffee_resources, coffee_menu)

        if not is_sufficient:
            if input("Do you want to refill the machine and buy again? Type 'Y' or 'N': ").upper() != "Y":
                run_machine = False
                print("Thanks for dripping by! ☕☕☕")


# If the code is run (instead of imported), run the game
if __name__ == "__main__":
    main()
