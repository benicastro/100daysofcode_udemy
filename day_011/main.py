"""Blackjack Capstone Project, by Benedict Castro benedict.castro11@gmail.com
A digital card game.
Tags: large, game, logic

This program is inspired by Al Sweigart's same project from his book "Big Book Small Python Projects"""

# Blackjack, also known as 21, is a card game where players try to get as close to 21 points as possible without going over.
# Rules:
#   1. Try to get as close to 21 without going over.
#   2. Kings, Queens, and Jacks are worth 10 points.
#   3. Aces are worth 1 or 11 points
#   4. Cards 2 through 10 are worth their face value.
#   5. (H)it to take another card.
#   6. (S)tand to stop taking cards.
#   7. On your first play, you can (D)ouble down to increase your bet but must hit exactly one more time before standing.
#   8. In case of a tie, the bet is returned to the player.
#   9. The dealer stops hitting at 17.

# Import needed modules
import random
import sys
import proj_art

# Set up the constants:
HEARTS = chr(9829)  # Character 9829 is '♥'.
DIAMONDS = chr(9830)  # Character 9830 is '♦'.
SPADES = chr(9824)  # Character 9824 is '♠'.
CLUBS = chr(9827)  # Character 9827 is '♣'.
BACKSIDE = "backside"


def main():
    print(proj_art.logo)
    print('''Blackjack, a digital card game.
            By Benedict Castro | benedict.zcastro@gmail.com''')

    def get_bet(max_bet):
        """Ask the player how much they want to bet for the current round."""
        invalid_bet = True
        while invalid_bet:  # Keep asking the player until they provide a valid bet amount
            print(f"How much would you like to bet? (1-{max_bet}, or QUIT)")
            bet = input("> ").upper().strip()
            if bet == "QUIT":
                print("Thanks for playing! Have a nice day!")
                sys.exit()
            if not bet.isdecimal():
                continue  # If the player didn't enter a number, ask again.

            bet = int(bet)
            if 1 <= bet <= max_bet:
                return bet  # The player entered a valid bet amount

    def get_deck():
        """This function returns a list of (rank, suit) tuples for all 52 cards of the deck"""
        deck = []
        suits = [HEARTS, DIAMONDS, SPADES, CLUBS]
        high_cards = ["J", "Q", "K", "A"]
        for suit in suits:
            for rank in range(2, 11):
                deck.append((str(rank), suit))  # Add the numbered cards
            for rank in high_cards:
                deck.append((rank, suit))  # Add the high-ranking cards (face and ace cards)
        random.shuffle(deck)
        return deck

    def get_hand_value(cards):
        """This function returns the value of the cards. Face cards are worth 10, while aces are worth 1 or 11
        depending on the circumstances."""
        value = 0
        ace_number = 0
        for card in cards:
            rank = card[0]  # Cards are set as tuples (rank, suit)
            if rank == "A":
                ace_number += 1
            elif rank in ["J", "Q", "K"]:  # Face cards are worth 10 points
                value += 10
            else:
                value += int(rank)  # Number cards are worth their number

        # Add the value for the aces:
        value += ace_number  # Add 1 point per ace
        for i in range(ace_number):
            if value + 10 <= 21:  # If another 10 can be added without busting, then add:
                value += 10

        return value

    def display_cards(cards):
        """This function displays all the cards in the cards list"""
        rows = ['', '', '', '', '']  # Create a list to store the texts to be displayed on each row

        for i, card in enumerate(cards):
            rows[0] += ' ___ '  # This is the top line of the card
            if card == BACKSIDE:  # Print the back of the card
                rows[1] += '|## | '
                rows[2] += '|###| '
                rows[3] += '|_##| '
            else:  # Print the front of the card
                rank, suit = card
                rows[1] += '|{} | '.format(rank.ljust(2))
                rows[2] += '| {} | '.format(suit)
                rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

        # Print each row
        for row in rows:
            print(row)

    def display_hands(player_hand, dealer_hand, show_dealer_hand):
        """This function shows the hands of both the player and dealer. In addition, It hides the dealer's
        first card if the variable show_dealer_hand is set to False."""
        print()
        if show_dealer_hand:
            print('DEALER:', get_hand_value(dealer_hand))
            display_cards(dealer_hand)
        else:
            print('DEALER: ???')
            display_cards([BACKSIDE] + dealer_hand[1:])  # Hide the dealer's first card

        # Show the player's cards:
        print('PLAYER:', get_hand_value(player_hand))
        display_cards(player_hand)

    def get_move(player_hand, money):
        """This function asks the player for their move. It returns 'H' for Hit, 'S' for stand, and 'D' for double down."""
        correct_move = False
        while not correct_move:  # Keep looping until the player provides a correct move
            moves = ['(H)it', '(S)tand']

            # The player can opt to double down on their first move
            if len(player_hand) == 2 and money > 0:
                moves.append('(D)ouble down')

            # Get the player's move
            move_prompt = ', '.join(moves) + '> '
            move = input(move_prompt).upper()
            if move in ['H', 'S']:
                return move  # Player has entered a valid move
            if move == 'D' and '(D)ouble down' in moves:
                return move  # Player has entered a valid move

    money = 5000
    run_game = True
    while run_game:  # Main game loop
        if money <= 0:
            # First, check if the player still has money
            print("You can't continue anymore because you're broke.")
            print("Better luck next time!")
            sys.exit()

        # Ask the player for their bet
        print(f"Money: {money}")
        bet = get_bet(money)

        # Give both the player and the dealer their initial two cards
        deck = get_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        # Handle player decisions
        print(f"Bet: {bet}")
        game_finished = False
        while not game_finished:  # Keep playing until the players stands or busts
            display_hands(player_hand, dealer_hand, False)
            print()

            # Check if the player has bust
            if get_hand_value(player_hand) > 21:
                break

            # Get player's move
            move = get_move(player_hand, money - bet)

            # Handle the player's action
            if move == "D":  # The player is doubling down, they can increase their bet
                additional_bet = get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print(f"Bet increase to {bet}.")
                print(f"Bet: {bet}")

            if move in ['H', 'D']:
                # H or D requires adding another card
                new_card = deck.pop()
                rank, suit = new_card
                print(f"You drew a {rank} of {suit}.")
                player_hand.append(new_card)

                if get_hand_value(player_hand) > 21:  # The player has busted
                    continue

            if move in ['S', 'D']:
                break

        # Handle the dealer's action
        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                print("Dealer hits...")  # The dealer hits
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    break  # The dealer has busted
                input('Press Enter to continue...')
                print('\n\n')

        # Show the final hands
        display_hands(player_hand, dealer_hand, True)

        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)

        # Check if the player won, lost, or tied
        if dealer_value > 21:
            print(f"The dealer busts! You win ${bet}!")
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print(f"You lost ${bet}!")
            money -= bet
        elif player_value > dealer_value:
            print(f"You won ${bet}!")
            money += bet
        elif player_value == dealer_value:
            print("It's a tie, your bet is returned")

        input('Press Enter to continue...')
        print('\n\n')


# If the game is run (instead of imported), run the game:
if __name__ == "__main__":
    main()

