"""Number Guessing Game, by Benedict Castro | benedict.castro11@gmail.com
A digital number guessing game.
Tags: game, logic"""

# Import needed modules
import proj_art
import random
import os


def main():
    print(proj_art.logo)

    def choose_difficulty():
        """This function asks the user for the game difficulty. It returns the number of attempts the player can guess depending on the
        difficulty, 10 for 'easy', or 5 for 'hard'."""
        difficulty = ''
        while difficulty not in ["easy", "hard"]:
            difficulty = input('Choose a difficulty. Type "easy" or "hard": ')
            if difficulty.lower() == "easy":
                return 10
            elif difficulty.lower() == "hard":
                return 5
            else:
                print("Please provide a valid answer among the options.")

    def get_number():
        """This function returns a random number to be guessed by the user"""
        return random.randint(1, 100)

    def compare_guess(guess, answer, attempts):
        """This function compares the player's guess to the correct number.
        It returns a number to be deducted to the number of attempts."""
        if guess == answer:
            print("You've got the right number. You won!")
            return 0
        elif guess > answer:
            print("Too high!")
            if attempts > 1:
                print("Guess again.")
            return 1
        else:
            print("Too low!")
            if attempts > 1:
                print("Guess again.")
            return 1

    run_game = True
    while run_game:  # Main game loop
        print("I'm thinking of a number between 1 and 100.")
        number_in_mind = get_number()  # Get number to be guessed by the player
        attempt_count = choose_difficulty()  # Ask user for game difficulty

        number_guess =[]  # Create a variable to store the player's guesses
        while (attempt_count != 0) or (number_in_mind not in number_guess):
            print(f"You have {attempt_count} attempt(s) remaining to guess the number.")  # Display the number of attempts of the player
            player_guess = int(input("Make a guess: "))  # Ask player to guess the number
            number_guess.append(player_guess)

            # Compare the player's guess to the right number
            guess_result = compare_guess(player_guess, number_in_mind, attempt_count)
            attempt_count -= guess_result
            if guess_result == 0:
                break  # The player already won the game

            # Print the player's guesses so far, for reference
            if attempt_count == 0:
                print(f"The answer is {number_in_mind}. You lose!")
                break
            else:
                print(f"Your guesses: {number_guess}")

        # Ask user if they want to play again
        if input('Do you want to play again? Type "Y" or "N": ').upper() != "Y":
            print("Thanks for playing! Have a nice day")
            run_game = False
        else:
            os.system('cls' if os.name == 'nt' else 'clear')


# If game is run (instead of imported), then run the game
if __name__ == "__main__":
    main()

