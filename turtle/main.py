import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    # Spawn a car from time to time :)
    if random.randint(0, 2) == 1:
        car_manager.spawn_car(300, random.randint(-250, 250))

    # Move all cars
    car_manager.move_all_cars()

    # Detect collision with car
    if car_manager.detect_collision(player):
        game_is_on = False
        score_board.game_over()

    # Check if player is at the end of the screen
    if player.finish():
        player.reposition()
        car_manager.speed_up()
        score_board.increase_level()

screen.exitonclick()