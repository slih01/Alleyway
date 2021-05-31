from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
paddle = Paddle()
ball = Ball()

screen.setup(600,500)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onkey(paddle.move_left,key="a")
screen.onkey(paddle.move_right,key="d")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.distance(paddle) <=20:
        ball.setheading(360 - ball.heading())




screen.exitonclick()
