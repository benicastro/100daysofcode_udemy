"""
Higher Lower Game, by Benedict Z. Castro | benedict.zcastro@gmail.com
An interactive educated guessing game.
"""

# Import needed modules
import game_data
import proj_art
import random


def main():
    """Higher Lower Game
    by: Benedict Castro | benedict.zcastro@gmail.com"""

    def get_random_data():
        """This function gets a random item entry for the game from the data repository."""
        entry = random.choice(game_data.data)
        # Extract the attributes of the chosen profile
        entry_name = entry["name"]
        entry_description = entry["description"]
        entry_country = entry["country"]
        entry_followers = entry["follower_count"]
        return entry_followers, f"{entry_name}, a(n) {entry_description}, from {entry_country}."  # return as tuple

    def compare_profiles(choice, prof1, prof2):
        """This function compares the number of followers of the two profiles and returns the result whether the player is
        right or wrong."""
        if choice.upper() == "A" and prof1[0] > prof2[0]:
            return 1
        elif choice.upper() == "B" and prof2[0] > prof1[0]:
            return 1
        else:
            return 0

    run_again = True
    while run_again:  # Main game loop
        # Set initial score
        score = 0

        # Get initial entry from the data repository
        profile1 = get_random_data()

        is_game_over = False  # Game is over if player guessed wrong
        while not is_game_over:
            print(proj_art.logo)
            # Get a new random profile from the repository
            profile2 = get_random_data()
            print(f"Compare A: {profile1[1]}")
            print(proj_art.vs)
            print(f"Against B: {profile2[1]}")

            # Ask player to guess who has more followers
            is_invalid = True
            while is_invalid:
                player_choice = input("Who has more followers? Type 'A' or 'B': ")
                if player_choice.upper() in ["A", "B"]:
                    is_invalid = False

            # Compare the number of followers for both profiles and check result
            points_obtained = compare_profiles(player_choice, profile1, profile2)
            score += points_obtained

            if points_obtained == 0:
                # print(proj_art.logo)
                print(f"Sorry, that's wrong. Final score: {score}")
                is_game_over = True
            else:
                # print(proj_art.logo)
                print(f"You're right! Current score: {score}")
                if player_choice == "B":
                    profile1 = profile2

        if input("Do you want to play again? Type 'Y' or 'N': ").upper() == "Y":
            run_again = True
        else:
            run_again = False


# If the program is run (instead of imported), run the program
if __name__ == "__main__":
    main()
