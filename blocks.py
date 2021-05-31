from turtle import Turtle

COLOURS = ["blue", "green", "orange", "yellow"]
STARTING_POSITIONS = [(-220, 180), (-220, 150), (-220, 120), (-220, 90)]


class Blocks(Turtle):

    def __init__(self):
        super().__init__()
        self.blocks = []
        self.row = []

    def create_block(self):
        self.shape("square")
        self.shapesize(stretch_len=4)
        self.row.append()




