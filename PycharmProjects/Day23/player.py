STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.restore()

    def upwards(self):
        self.forward(MOVE_DISTANCE)

    def restore(self):
        self.hideturtle()
        self.penup()
        self.goto(STARTING_POSITION)
        self.showturtle()


