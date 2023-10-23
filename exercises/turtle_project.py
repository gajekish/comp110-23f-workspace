"""A checkerboard set up with checker pieces."""
__author__ = "730662291"

from turtle import Turtle, colormode, done


def main() -> None:
    """The entrypoint of my scene."""
    yertle: Turtle = Turtle()
    yertle.speed(50)
    yertle.hideturtle()
    colormode(255)

    index: int = 0
    ends_in_red: bool = False
    y_pos: int = 350
    while (index < 6):
        if (ends_in_red):
            first_inner_index: int = 0
            first_x_pos: int = -350
            while (first_inner_index < 3):
                draw_red_square(yertle, first_x_pos, y_pos, 115)
                first_x_pos += 115
                draw_black_square(yertle, first_x_pos, y_pos, 115)
                first_x_pos += 115
                first_inner_index += 1
            ends_in_red = False
        else:
            second_inner_index: int = 0
            second_x_pos: int = -350
            while (second_inner_index < 3):
                draw_black_square(yertle, second_x_pos, y_pos, 115)
                second_x_pos += 115
                draw_red_square(yertle, second_x_pos, y_pos, 115)
                second_x_pos += 115
                second_inner_index += 1
            ends_in_red = True
        y_pos -= 115
        index += 1

    draw_black_checker(yertle, -180, -210, 40)
    draw_black_checker(yertle, 50, -210, 40)
    draw_black_checker(yertle, 285, -210, 40)
    draw_black_checker(yertle, -295, -325, 40)
    draw_black_checker(yertle, -60, -325, 40)
    draw_black_checker(yertle, 170, -325, 40)
    draw_red_checker(yertle, -295, 255, 40)
    draw_red_checker(yertle, -60, 255, 40)
    draw_red_checker(yertle, 170, 255, 40)
    draw_red_checker(yertle, -180, 140, 40)
    draw_red_checker(yertle, 50, 140, 40)
    draw_red_checker(yertle, 285, 140, 40)

    done()


def draw_red_square(turtle_name: Turtle, x: float, y: float, width: float) -> None:
    """Draws a red square of any desired size and at any desired position."""
    turtle_name.penup()
    turtle_name.goto(x, y) 
    turtle_name.setheading(0.0)
    turtle_name.pencolor('red')
    turtle_name.fillcolor('red')
    turtle_name.pendown()
    turtle_name.begin_fill()
    square(turtle_name, width)
    turtle_name.end_fill()


def draw_black_square(turtle_name: Turtle, x: float, y: float, width: float) -> None:
    """Draws a red square of any desired size and at any desired position."""
    turtle_name.penup()
    turtle_name.goto(x, y) 
    turtle_name.setheading(0.0)
    turtle_name.pencolor('black')
    turtle_name.fillcolor('black')
    turtle_name.pendown()
    turtle_name.begin_fill()
    square(turtle_name, width)
    turtle_name.end_fill()


def square(turtle_object: Turtle, size: float) -> None:
    """Draws a general square given a specified size."""
    i: int = 0
    while i < 4:
        turtle_object.forward(size)
        turtle_object.right(90)
        i = i + 1


"""Something interesting I found was the circle() method from the turtle module which I 
used in the following functions to draw the round red and black checker pieces."""


def draw_black_checker(turtle_name: Turtle, x: float, y: float, radius: float) -> None:
    """Draws a black checker piece of any desired size and at any desired position."""
    turtle_name.penup()
    turtle_name.goto(x, y) 
    turtle_name.setheading(0.0)
    turtle_name.pencolor('black')
    turtle_name.fillcolor('black')
    turtle_name.pendown()
    turtle_name.begin_fill()
    turtle_name.circle(radius)
    turtle_name.end_fill()


def draw_red_checker(turtle_name: Turtle, x: float, y: float, radius: float) -> None:
    """Draws a red checker piece of any desired size and at any desired position."""
    turtle_name.penup()
    turtle_name.goto(x, y) 
    turtle_name.setheading(0.0)
    turtle_name.pencolor('red')
    turtle_name.fillcolor('red')
    turtle_name.pendown()
    turtle_name.begin_fill()
    turtle_name.circle(radius)
    turtle_name.end_fill()


if __name__ == "__main__":
    main()