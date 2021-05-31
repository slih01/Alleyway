from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=4)
        self.goto(0, -220)

    def starting_pos(self):
        self.hideturtle()
        self.goto(0, -220)


    def move_left(self):
        self.back(20)

    def move_right(self):
        self.forward(20)