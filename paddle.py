from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=6)
        self.goto(position)
        self.color("white")



