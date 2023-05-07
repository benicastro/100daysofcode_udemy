def batopick(user_input):
    # This function simulates a rock paper scissors game where it asks for a user input based on the three possible choices
    # and compare it against the computer's choice
    import random
    from game_art import ROCK, PAPER, SCISSORS

    choices = [ROCK, PAPER, SCISSORS]
    user_choice = choices[user_input]
    print(f"You chose: \n {user_choice}")

    # Give computer a random choice
    computer_choice = choices[random.randint(0, 2)]
    print(f"Computer chose: \n {computer_choice}")

    # Create conditions for winning

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == ROCK and computer_choice == SCISSORS) or (user_choice == PAPER and computer_choice == ROCK) or (
            user_choice == SCISSORS and computer_choice == PAPER):
        print("You won!")
    else:
        print("You lose!")


keep_playing = "Y"

while keep_playing:
    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
    batopick(user_input)

    keep_playing = input('Do you still want to play? Type "Y" or "N": ')
    if keep_playing.upper() != "Y":
        break
