FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("red")
        self.hideturtle()
        self.goto(-270, 270)
        self.write(f"level={self.score}", align="left", font=FONT)

    def increase(self):
        self.score+=1
        self.clear()
        self.write(f"level ={self.score}", align="left", font=FONT)

    def gameOver(self):
        self.clear()
        self.home()
        self.write("Game Over", align="center", font=FONT)


