from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.createpaddle(pos)

    def createpaddle(self,pos):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(pos)


    def upwards(self):
        new_y =self.ycor()+20
        self.sety(new_y)

    def downwards(self):
        new_y =self.ycor()-20
        self.sety(new_y)

