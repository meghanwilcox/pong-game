from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.pendown()
        self.pencolor("white")
        self.write("0", False, "center", font=('Arial', 20, 'normal'))

    def increment_score(self, position, score):
        self.hideturtle()
        self.clear()
        self.penup()
        self.goto(position)
        self.pendown()
        self.pencolor("white")
        self.write(f"{score}", False, "center", font=('Arial', 20, 'normal'))

    def game_over_winner(self, score1, score2):
        if score1 > score2:
            self.hideturtle()
            self.pencolor("white")
            self.write("Player 1 Wins!", False, "center", font=('Arial', 20, 'normal'))
        elif score1 < score2:
            self.hideturtle()
            self.pencolor("white")
            self.write("Player 2 Wins!", False, "center", font=('Arial', 20, 'normal'))
        else:
            self.hideturtle()
            self.pencolor("white")
            self.write("Tie!", False, "center", font=('Arial', 20, 'normal'))
