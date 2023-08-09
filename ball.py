from turtle import Turtle
from random import randint
from paddle import Paddle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")

    def ball_moves(self, object1):
        collided = False
        while not collided:
            self.speed("normal")
            self.forward(10)
            if self.collide_with_top_or_bottom() or self.collide_with_side_wall() or self.collide_with_paddle(object1):
                collided = True

    def collide_with_top_or_bottom(self):
        if self.ycor() <= -290:
            return True
        elif self.ycor() >= 290:
            return True

    def collide_with_side_wall(self):
        if self.xcor() <= -295 or self.xcor() >= 295:
            return True

    def collide_with_paddle(self, object1):
        if (self.xcor() == object1.xcor()) and (
                (self.ycor() - object1.ycor() <= 60) or (self.ycor() - object1.ycor() >= -60)):
            return True