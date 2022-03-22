from turtle import Turtle
ALIGN="CENTER"
FONT=("Verdana",20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update()


    def leftpoint(self):

        self.l_score=self.l_score+1
        self.clear()

        self.update()


    def rightpoint(self):
        self.r_score+=1
        self.clear()
        self.update()

    def update(self):
         self.goto(-100, 200)
         self.write(f"{self.l_score}", align=ALIGN, font=FONT)
         self.goto(100, 200)
         self.write(f"{self.r_score}", align=ALIGN, font=FONT)

