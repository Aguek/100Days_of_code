from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:
    score_turtle = Turtle()

    def __init__(self):
        self.score = 1
        self.score_turtle.hideturtle()

    def scores(self):
        self.score_turtle.penup()
        self.score_turtle.goto(-220, 260)
        self.score_turtle.clear()
        self.score_turtle.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.score_turtle.goto(0, 0)
        self.score_turtle.write("GAME OVER", align="center", font=FONT)