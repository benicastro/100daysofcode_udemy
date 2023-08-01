"""
The Turtle Crossing Game by Benedict Z. Castro | benedict.zcastro@gmail.com
"""

# Import needed modules
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Declare global variables or constants
WIDTH = 600
HEIGHT = 600
TITLE = "0xAstroc's Turtle Crossing Game"

# Configure screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title(TITLE)
screen.tracer(0)

# Make the screen listen to keystrokes
player = Player()  # Create player class
screen.listen()
screen.onkey(fun=player.move, key="Up")

# Create car and scoreboard objects
car_manager = CarManager()
scoreboard = Scoreboard()


def main():

    play_again = True  # Create a variable and condition for an option to play again the game
    while play_again:

        num_loop = 0  # Create a placeholder for the number of loops already made
        game_is_on = True  # Create a variable and condition telling if the game is still running
        while game_is_on:

            # Configure animation settings
            time.sleep(0.1)
            screen.update()

            # Create cars only every 6th time the game loop runs
            if num_loop % 6 == 0:
                car_manager.create_cars()
            car_manager.drive_cars()

            # Detect when player collides with a car
            for car in car_manager.all_cars:
                if car.distance(player) < 20:
                    game_is_on = False

            # Detect when the turtle reaches the finish line
            if player.is_at_finish_line():
                player.go_to_start()
                car_manager.increase_speed()
                scoreboard.increase_level()
                scoreboard.update_scoreboard()

            # Monitor the number of loops made
            num_loop += 1

        # Ask user if they want to play again
        if screen.textinput(title="GAME OVER", prompt="Do you want to play again? Y or N: ").lower() != "y":
            play_again = False

    # Make sure to exit screen after the game by clicking
    screen.exitonclick()


# Run the game
if __name__ == "__main__":
    main()
