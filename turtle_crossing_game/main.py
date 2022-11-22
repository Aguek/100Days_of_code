import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.title("MABIL'S TURTLE")
screen.onkeypress(key="Up", fun=player.go_up)

car_manager = CarManager()
score_board = Scoreboard()

game_is_on = True
num_of_loops = 0
car_speed = 5
while game_is_on:
    num_of_loops += 1
    time.sleep(0.1)
    screen.update()
    score_board.scores()
    if score_board.score < 3:
        if num_of_loops % 6 == 0:
            car_manager.create_car()
    elif 3 <= score_board.score <= 6:
        if num_of_loops % 3 == 0:
            car_manager.create_car()
    else:
        if num_of_loops % 1 == 0:
            car_manager.create_car()
    car_manager.move_car(car_speed)
    # detect collision with car

    for car in car_manager.all_cars:
        if car.distance(player) < 22:
            game_is_on = False
            score_board.game_over()

    # detect if player has reached the finish line

    if player.ycor() >= 280:
        print("YOU WIN")
        car_speed += 5
        score_board.score += 1
        player.reset()
        car_manager.move_car(car_speed)



screen.exitonclick()