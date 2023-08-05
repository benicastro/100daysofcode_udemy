"""
US States Game by Benedict Z. Castro | benedict.zcastro@gmail.com
"""

# Import needed modules
import pandas as pd
from turtle import Screen
from game_master import GameMaster
import turtle

# Initialize GameMaster objects
game_master = GameMaster()
bg_master = GameMaster()  # This handles the background image

# Configure screen
screen = Screen()
screen.title("0xAstroc's US States Quiz")

# Make the local image file as background
image_bg = "blank_states_img.gif"
screen.addshape(image_bg)
bg_master.create_background(image_bg)

# Extract data from the csv file using pandas
df = pd.read_csv("50_states.csv")


def main():

    game_is_on = True
    while game_is_on:  # Main game loop

        user_answer = screen.textinput(title=f"{game_master.score}/50 States Correct",
                                       prompt="Please give another state name?").title()

        # Check if user answer is correct
        if user_answer in df["state"].values:
            game_master.increase_score(user_answer)

            # Get the x and y coordinates of the user's answer from the csv file, and then display it on the screen
            x = int(df[df["state"] == user_answer].x)
            y = int(df[df["state"] == user_answer].y)
            game_master.display_answer(x, y, user_answer)

        elif user_answer == "Exit":  # End the game
            break

        if game_master.score == 50:
            game_is_on = False

    # Save the states that the user missed to a csv file
    missing_states = []
    for state in df["state"]:
        if state not in game_master.correct_answers:
            missing_states.append(state)
    pd.DataFrame(missing_states).to_csv("states_to_learn.csv")


# Run the game
if __name__ == "__main__":
    main()

# Keep the screen open
screen.mainloop()

#########################################################################################################################################
# # Make the screen listen on mouse click
# def get_mouse_click_coor(x, y):
#     """This function takes the location or coordinates of the mouse button upon clicking."""
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#########################################################################################################################################
