from turtle import Screen,Turtle
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Arcade Game")
screen.tracer(0)

ball=Ball()
paddle_l=Paddle((-350,0))
paddle_r=Paddle((350,0))
scoreboard=Scoreboard()



screen.listen()
screen.onkey(paddle_r.upwards,"Up")
screen.onkey(paddle_r.downwards,"Down")

screen.onkey(paddle_l.upwards,"u")
screen.onkey(paddle_l.downwards,"j")

game_is_on=True
while game_is_on:
      time.sleep(0.1)
      screen.update()
      ball.move()
      # if ball.xcor()>= 370  or ball.xcor()<=-370:
      #       ball.detect()
      if ball.ycor()>=290 or ball.ycor()<=-290:
            ball.bounce_y()

      if ball.distance(paddle_r)<50 and ball.xcor()>320 or ball.distance(paddle_l)<50 and ball.xcor()<-320:

            ball.bounce_x()

      if ball.xcor()>380:

            ball.reset_position()
            scoreboard.leftpoint()

      if ball.xcor()<-380:
            scoreboard.rightpoint()
            ball.reset_position()




screen.exitonclick()