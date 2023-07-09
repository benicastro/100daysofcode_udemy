"""
Turtle Racing Game by Benedict Castro | benedict.zcastro@gmail.com
"""

# Import needed modules
from turtle import Turtle, Screen
import random

# Declare screen class
screen = Screen()

# Define turtle colors
COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "black", "gray", "magenta", "cyan"]


def main():
    """
    Turtle Racing Game
    by Benedict Castro | benedict.zcastro@gmail.com
    """

    def ask_num_racers():
        """This function asks the user how many turtle racers should be part of the game. The more the racers, the less chance
        of winning. It returns True if the user entered a valid input."""
        valid_input = False
        num_racers = 0
        while not valid_input:
            try:
                num_racers = (screen.numinput(title="Choose difficulty",
                                              prompt="How many turtles do you want to race? (2 - 10): ",
                                              default=6, minval=2, maxval=10))
                if num_racers.is_integer():
                    valid_input = True
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid integer number from 2 to 10.")
        return int(num_racers)

    def ask_bet(color_list):
        """This function asks the user what turtle color is that he/she going to bet. Returns the inputted color."""
        valid_input = False
        turtle_bet = ''
        while not valid_input:
            try:
                turtle_bet = screen.textinput(title="Which turtle will win the race?", prompt=f"Enter a color: {color_list}")
                if turtle_bet in color_list:
                    valid_input = True
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid color from the given options.")
        return turtle_bet

    def configure_screen(num_racers):
        """This function configures the screen properties based on the number of racers.It returns a tuple variable describing
        the screen size."""
        screen_width = 1100
        if num_racers > 5:
            screen_height = 55 * num_racers
        else:
            screen_height = 100 * num_racers
        screen_size = (screen_width, screen_height)
        screen.setup(screen_width, screen_height)
        return screen_size

    def get_turtle_positions(num_racers, screen_size):
        """This function returns the starting position of the turtle racers in the game."""
        spacing = 10
        turtle_size = 40
        race_space = (spacing + turtle_size) * (num_turtles-1)
        x_position = -(screen_size[0]/2) + 40
        y_positions = []
        for i in range(num_racers):
            y_positions.append((-race_space/2) + i*(spacing + turtle_size))
        return x_position, y_positions

    def gen_finish(screen_size):
        """This function generates a finish line object."""
        finish_loc = screen_size[0]/2 - 40
        is_finished = False
        alt = 0
        while not is_finished:
            new_block = Turtle("square")
            new_block.penup()
            if alt % 2 == 0:
                new_block.color("black")
            else:
                new_block.color("white")
            new_block.goto(x=finish_loc, y=-(screen_size[1]/2 - 40) + alt*20)
            if new_block.ycor() > screen_size[1]/2 - 40:
                break
            alt += 1

    # Create a variable telling if the game is still on going
    game_is_on = False
    num_turtles = ask_num_racers()
    turtle_colors = []
    if num_turtles:
        game_is_on = True

        # Select turtle colors based on number of racers
        turtle_colors = COLORS[:num_turtles]

    while game_is_on:  # Main game loop

        # Ask user for bet
        user_bet = ask_bet(turtle_colors)

        # Configure screen and turtle positions
        racing_screen = configure_screen(num_turtles)
        x_coord, y_coord = get_turtle_positions(num_turtles, racing_screen)

        all_turtles = []
        for index in range(num_turtles):
            new_turtle = Turtle(shape="turtle")
            new_turtle.color(turtle_colors[index])
            new_turtle.penup()
            new_turtle.goto(x_coord, y_coord[index])
            all_turtles.append(new_turtle)

        # Simulate race
        race_finished = False
        gen_finish(racing_screen)
        finish_line = racing_screen[0]/2 - 40
        while not race_finished:
            for index in range(num_turtles):
                all_turtles[index].forward(random.randint(0, 10))
                if all_turtles[index].xcor() > finish_line:
                    race_finished = True
                    if user_bet == all_turtles[index].pencolor():
                        print(f"You've won! The {all_turtles[index].pencolor()} turtle was the winner.")
                    else:
                        print(f"You've lost! The {all_turtles[index].pencolor()} turtle was the winner.")

            game_is_on = False

    screen.exitonclick()


# If the game is run (instead of imported), run the game
if __name__ == "__main__":
    main()
