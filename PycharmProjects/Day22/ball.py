from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.color("white")
        self.xmo = 10
        self.ymo = 10

    def move(self):
        new_x=self.xcor()+self.xmo
        new_y=self.ycor()+self.ymo
        self.setposition(new_x,new_y)

    def detect(self):
        self.home()
        self.move()

    def bounce_y(self):
        self.ymo *= -1

    def bounce_x(self):
        self.xmo *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()