from turtle import Turtle, Screen

from ball import Ball
from paddle import Paddle
import time

from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)

screen.title("PONG")
screen.bgcolor("black")
screen.setup(width=800, height=600)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

ball = Ball()
score = Scoreboard()
screen.listen()

screen.onkeypress(key="Up", fun=right_paddle.go_up)
screen.onkeypress(key="Down", fun=right_paddle.go_down)
screen.onkeypress(key="w", fun=left_paddle.go_up)
screen.onkeypress(key="s", fun=left_paddle.go_down)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move_ball()
    # collision with upper and downer walls
    if ball.ycor() == 290 or ball.ycor() < -290:
        ball.bounce_y()
    # detect collision with paddle
    if ball.distance(right_paddle) < 40 and ball.xcor() > 330 or ball.distance(left_paddle) < 40 and ball.xcor() < -330:
        ball.bounce_x()
    # detect a miss

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()



screen.exitonclick()
