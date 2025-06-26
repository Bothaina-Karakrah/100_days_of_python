from turtle import Turtle
from random import randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_Y = -250
FINISH_Y = 250

class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        car = Turtle(shape="square")
        car.color(COLORS[randint(0, len(COLORS)-1)])
        car.penup()
        car.setheading(180)
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(300, randint(STARTING_Y, FINISH_Y))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)
            if car.xcor() < -280:
                car.goto(300, randint(STARTING_Y, FINISH_Y))

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
