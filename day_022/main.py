"""
Pong Game by Benedict Z. Castro | benedict.zcastro@gmail.com
"""

# Import needed modules
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time




# Configure screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("0xAstroc's Pong Game")
screen.tracer(0)

# Make the screen listen for keystrokes and create the paddles
screen.listen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

ball = Ball()
scoreboard = Scoreboard()


def main():

    play_again = True  # Create a variable and condition to tell if the user wants to play again
    while play_again:

        game_is_on = True  # Create a variable and condition to tell if the game is running
        while game_is_on:

            # Configure animation on screen
            screen.update()
            time.sleep(ball.move_speed)

            # Make the ball move
            ball.move()

            # Detect collision with the walls and paddles
            if ball.ycor() >= 280 or ball.ycor() <= -280:
                ball.bounce()
            if (ball.distance(r_paddle) <= 20 and ball.xcor() > 320) or (ball.distance(l_paddle) <= 20 and ball.xcor() < 320):
                ball.hit()

            # Detect when the ball goes out of bounds
            if ball.xcor() >= 380:
                ball.reset_position()
                scoreboard.l_point()
            elif ball.xcor() <= -380:
                ball.reset_position()
                scoreboard.r_point()
            else:
                continue

            scoreboard.update_scoreboard()
            print(ball.move_speed)




# Run the game
if __name__ == "__main__":
    main()

# Make the screen exit on click for convenience
screen.exitonclick()