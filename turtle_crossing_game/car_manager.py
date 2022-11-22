from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.setheading(180)
        new_car.xposition = 280
        y_pos = random.randint(-250, 250)
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(new_car.xposition, y_pos)

        new_car.color(random.choice(COLORS))
        self.all_cars.append(new_car)

    def move_car(self, car_speed):
        for car in self.all_cars:
            car.forward(car_speed)


