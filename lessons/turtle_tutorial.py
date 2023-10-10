from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.pencolor(173, 32, 189)
leo.up()
leo.goto(-150, -100)
leo.down()
leo.fillcolor(32, 67, 93)
leo.speed(10)
leo.hideturtle()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()


bob: Turtle = Turtle()

bob.color(110, 255, 0)
bob.up()
bob.goto(-150,-100)
bob.down()
bob.speed(50)
bob.hideturtle()


side_length: int = 300
i: int = 0
while (i < 30):
    side_length *= 0.97
    bob.forward(side_length)
    bob.left(120.7)
    i += 1

done()