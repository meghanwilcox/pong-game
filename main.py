from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from random import randint

# set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")

score1 = 0
score2 = 0

#  scoreboard objects
scoreboard_player_1 = Scoreboard((-270, 260))
scoreboard_player_2 = Scoreboard((270, 260))

game_is_on = True
while game_is_on:
    # paddle objects
    paddle1 = Paddle((-275, 0))
    paddle2 = Paddle((275, 0))

    # ball object
    ball = Ball()

    # determine starting heading
    if randint(0, 1) == 0:
        ball.setheading(randint(145, 215))
    else:
        ball.setheading(randint(35, 305))

    # ball starts moving
    ball.ball_moves(paddle1)

    # detect collisions with the roof or ceiling
    while ball.collide_with_top_or_bottom():
        ball.setheading(360 - ball.heading())
        ball.ball_moves(paddle1)

    # detect collisions with the side wall, cause a score increase and a reset of the game
    if ball.collide_with_side_wall():
        if ball.xcor() < 0:
            score2 += 1
            scoreboard_player_2.increment_score((270, 260), score2)
        if ball.xcor() > 0:
            score1 += 1
            scoreboard_player_1.increment_score((-270, 260), score1)
        ball.hideturtle()

        if ball.collide_with_paddle(paddle1):
            ball.setheading(360 - ball.heading())
            ball.ball_moves(paddle1)

screen.exitonclick()
