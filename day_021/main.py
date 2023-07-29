"""
The Snake Game by Benedict Castro | benedict.zcastro@gmail.com
"""

# Import needed modules #######################################################################################################
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Declare constants #################################################################################################
WIDTH = 600
HEIGHT = 600
BG_COLOR = "black"
TITLE = "Milyastroc's Snake Game"


###############################################################################################################################
def main():
    """The Snake Game
    by Benedict Castro | benedict.zcastro@gmail.com"""

    play_again = True  # Create a variable to determine if the player wants to try the game again
    while play_again:

        # Configure screen
        screen = Screen()
        screen.setup(width=WIDTH, height=HEIGHT)
        screen.bgcolor(BG_COLOR)
        screen.title(TITLE)
        screen.tracer(0)

        # Initialize the imported classes
        snake = Snake()
        food = Food()
        score = Scoreboard()

        # Make the screen listen to keypress
        screen.listen()
        screen.onkey(snake.up, "Up")
        screen.onkey(snake.down, "Down")
        screen.onkey(snake.left, "Left")
        screen.onkey(snake.right, "Right")

        game_is_on = True  # Main game loop
        while game_is_on:

            # Configure animation settings
            screen.update()
            time.sleep(0.1)

            # Make the snake move by default
            snake.move()

            # Detect collision with food
            if snake.head.distance(food) < 15:
                food.refresh()
                snake.extend()
                score.increase_score()

            # Detect collision with wall
            if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
                game_is_on = False
                score.game_over()

            # Detect collision with tail
            for segment in snake.segments[1:]:
                if snake.head.distance(segment) < 10:
                    game_is_on = False
                    score.game_over()

        if screen.textinput(title=TITLE, prompt="Do you want to play again? (Yes | No): ").lower() != "yes":
            play_again = False
        else:
            screen.clear()


# If the game is run (instead of imported), run the game.
if __name__ == "__main__":
    main()

# Prevent the window from closing without user intervention
Screen().exitonclick()
