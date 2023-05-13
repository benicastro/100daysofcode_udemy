"""Silent Auction Program, by Benedict Castro benedict.castro11@gmail.com
A digital bidding tool.
Tags: short, code, logic"""

# Import needed modules
import proj_art
import os


def main():
    print(proj_art.logo)
    print('''Secret Auction, a digital bidding tool.
        By Benedict Castro benedict.zcastro@gmail.com''')

    def ask_player():
        """This function asks the player for his/her name and the corresponding bid."""
        invalid_inputs = True
        while invalid_inputs:
            name = input("Please provide your name: ")
            bid = float(input("What is your bid? $"))
            if not isinstance(bid, float):
                print("Please provide valid inputs.")
            else:
                invalid_inputs = False
                return name, bid

    run_program = True
    while True:  # Main program loop
        bidder_dictionary = {}  # Store the info of bidders
        potential_winner = ""
        highest_bid = 0
        more_bidders = True
        while more_bidders:
            name, bid = ask_player()
            bidder_dictionary[name] = bid

            # Keep track of the highest bid
            if bidder_dictionary[name] > highest_bid:
                highest_bid = bid
                potential_winner = name

            # Ask if there are still bidders
            continue_bidding = input('Are there any other bidders? Type "yes" or "no": ')
            os.system('cls' if os.name == 'nt' else 'clear')
            if continue_bidding.lower() != "yes":
                print("There are no more bidders. We advance to the selection process.")
                more_bidders = False

        print(f"The winner is {potential_winner} with a bid of ${highest_bid:.2f}!")

        # Ask user if they want to use the tool again
        use_again = input('Do you want to use the tool again? Type "yes" or "no": ')
        if use_again.lower() != "yes":
            break

    print("Thank you for using this tool. May the best bidder win!")


# If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()
