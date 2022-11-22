from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.move_speed = 0.1
        self.shapesize(stretch_wid=1, stretch_len=1, outline=None)
        self.y_move = 10
        self.x_move = 10

    def move_ball(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        """
         a bounce method for multiplying y-coordinate by -1 so that if the y value is in negative then
        should add the y value so that it can bounce to the safe side
        of the screen, and that is through multiplying a negative by
        a negative hence making it a positive
        :return:
        """
        self.y_move *= -1

    def bounce_x(self):
        """
         a bounce method for multiplying x-coordinate by -1 so that if the y value is in negative then
        should add the y value so that it can bounce to the safe side
        of the screen, and that is through multiplying a negative by
        a negative hence making it a positive
        :return:
        """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

