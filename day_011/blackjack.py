# Set up the constants:
HEARTS = chr(9829)  # Character 9829 is '♥'.
DIAMONDS = chr(9830)  # Character 9830 is '♦'.
SPADES = chr(9824)  # Character 9824 is '♠'.
CLUBS = chr(9827)  # Character 9827 is '♣'.
BACKSIDE = "backside"


def get_bet(max_bet):
    """Ask the player how much they want to bet for the current round."""
    invalid_bet = True
    while invalid_bet:  # Keep asking the player until they provide a valid bet amount
        print(f"How much would you like to bet? (1-{max_bet}, or QUIT")
        bet = input("> ").upper().strip()
        if bet == "QUIT":
            print("Thanks for playing! Have a nice day!")
            break
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


def display_hands(player_hand, dealer_hand, show_dealer_hand):
    """This function shows the hands of both the player and dealer. In addition, It hides the dealer's
    first card if the variable show_dealer_hand is set to False."""