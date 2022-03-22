from turtle import Turtle

ALIGN="center"
FONT=("Verdana",15, "normal")

class ScoreBd(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.update()


    def reset(self):
        print(self.score)
        if self.score>self.high_score:
            self.highscore=self.score

        self.score=0
        self.update()

    def increase(self):
        self.score+=1

        self.update()

    def update(self):
        self.clear()
        self.write(f"Score ={self.score} High Score={self.high_score}", align=ALIGN, font=FONT)

    #def game_over(self):
    #   self.goto(0,0)
    #   self.write(f"Game Over", align=ALIGN, font=FONT)
