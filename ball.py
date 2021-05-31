from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=0.7,stretch_wid=0.7)
        self.penup()
        self.hideturtle()
        self.goto(random.randint(-250,250),0)
        self.showturtle()
        self.setheading(self.towards(0,-220))

    def move(self):
        self.hideturtle()
        self.forward(10)
        self.showturtle()
