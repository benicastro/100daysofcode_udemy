"""Blackjack Capstone Project, by Benedict Castro benedict.castro11@gmail.com
A digital card game.
Tags: large, game, logic"""

# Import needed modules
import proj_art
import random
import sys


def main():
    print(proj_art.logo)
    print('''Blackjack, a digital card game.
            By Benedict Castro | benedict.zcastro@gmail.com''')

    def get_card():
        """This function gets random cards for the players."""
        deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]  # This deck represents the cards available
        random.shuffle(deck)
        card = deck.pop()
        return card

    def get_hand_value(hand):
        """This function outputs the total value of the cards dealt"""
        total_value = 0
        number_of_aces = 0
        for card in hand:
            if card == 11:
                number_of_aces += 1
            else:
                total_value += card
        if (number_of_aces >= 1) and (total_value + 11 <= 21):  # This determines the value for the ace
            total_value += number_of_aces + 10
        else:
            total_value += number_of_aces

        return total_value

    # Ask user if he/she wants to play the game
    play_game = input('Do you want to play a game of Blackjack? Type "Y" or "N": ')
    if play_game != "Y":
        sys.exit()
    else:
        run_game = True

    while run_game:  # Main game loop

        # Get cards for players
        player_hand = []
        computer_hand = []
        for i in range(2):
            player_hand.append(get_card())
            computer_hand.append(get_card())

        # Display the player's hand and the computer's first card
        print(f"Your cards: {player_hand}")
        print(f"Computer's cards: [{computer_hand[0]}, _ ]")

        # Keep looping until they draw the right amount of cards to possibly win
        add_card = True
        while add_card:
            # Ask player if they want to draw another card
            draw_card = input('Type "Y" to get another card, otherwise type "N" to pass: ')
            if draw_card != "Y":
                add_card = False
            else:
                player_hand.append(get_card())
                print(f"Your cards: {player_hand}")
            if get_hand_value(player_hand) > 21:
                print("You have been busted! Sorry, you lose.")
                break
            if get_hand_value(computer_hand) < 17:
                computer_hand.append(get_card())
                if get_hand_value(computer_hand) > 21:
                    print("The computer has busted. You won!")
                    print(f"Computer's cards: {computer_hand}")
                    break

        # Check winner
        player_hand_value = get_hand_value(player_hand)
        computer_hand_value = get_hand_value(computer_hand)
        if (player_hand_value > 21) or (computer_hand_value > 21):
            pass
        else:
            print(f"Your cards: {player_hand}")
            print(f"Computer's cards: {computer_hand}")
            if player_hand_value == computer_hand_value:
                print("It's a draw")
            elif player_hand_value > computer_hand_value:
                print("You won!")
            else:
                print("You lose!")

        play_again = input('Do you want to play again? Type "Y" or "N": ')
        if play_again.upper() != "Y":
            run_game = False

    print("Thanks for playing! Have a nice day!")


# If the game is run (instead of imported), run the game
if __name__ == "__main__":
    main()
