COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager():

    def __init__(self):

        self.all_cars=[]
        self.increment = STARTING_MOVE_DISTANCE

    def generation(self):
        randomchance=random.randint(1,6)
        if randomchance==1:
            block=Turtle()
            block.shape("square")
            block.color(random.choice(COLORS))
            block.shapesize(stretch_wid=1, stretch_len=2)
            block.hideturtle()
            block.penup()
            block.goto(300,random.randint(-250,250))
            block.showturtle()
            self.all_cars.append(block)

    def move_left(self):
        for car in self.all_cars:
            car.backward(self.increment)

    def level_up(self):
        self.increment+=MOVE_INCREMENT






