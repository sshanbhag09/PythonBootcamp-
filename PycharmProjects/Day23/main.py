import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(player.upwards, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generation()
    car_manager.move_left()
    # collision
    for car in car_manager.all_cars:
        if car.distance(player)<10:
            scoreboard.gameOver()
            game_is_on=False
            break
    # crossed successfully
    if player.ycor()==280:
        scoreboard.increase()
        player.restore()
        car_manager.level_up()


screen.exitonclick()
