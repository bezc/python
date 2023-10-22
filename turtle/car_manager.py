from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_CAR_AMOUNT = 10
MOVE_INCREMENT = 5
INITIAL_SPEED = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = INITIAL_SPEED
        for i in range(0, 20):
            self.spawn_car(random.randint(0, 250), random.randint(-250, 250))

    def spawn_car(self, x_coord, y_coord):
        car = Turtle()
        car.penup()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.turtlesize(stretch_wid=1, stretch_len=2)
        car.goto(x_coord, y_coord)
        car.seth(180)
        self.cars.append(car)

    def move_all_cars(self):
        for each_car in self.cars:
            new_x = each_car.xcor() - self.car_speed
            each_car.goto(new_x, each_car.ycor())

    def detect_collision(self, player):
        for each_car in self.cars:
            if each_car.distance(player) < 20:
                return True

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
