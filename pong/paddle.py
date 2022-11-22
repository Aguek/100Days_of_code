from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xcord, ycord):
        super().__init__()
        self.xcord = xcord
        self.ycord = ycord
        self.shape("square")
        self.hideturtle()
        self.create_paddle()
        self.goto(x=xcord, y=ycord)
        self.showturtle()

    def create_paddle(self):
        self.shapesize(stretch_len=1, stretch_wid=5, outline=None)
        self.color("white")
        self.penup()

    def go_up(self):
        new_y = self.ycor() + 20
        if self.ycor() < 240:
            self.goto(x=self.xcord, y=new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if self.ycor() > -240:
            self.goto(x=self.xcord, y=new_y)