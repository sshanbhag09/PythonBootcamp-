from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBd

WALL=300

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreb = ScoreBd()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    pos = snake.head.position()
    if snake.head.distance(pos[0],WALL) <= 0 or snake.head.distance(WALL,pos[1]) <=0 or snake.head.distance(-WALL,pos[1])<=0 or snake.head.distance(pos[0],-WALL)<=0:
        scoreb.reset()
        #game_is_on = False

    #collision
    if snake.head.distance(food)<15:
        food.generate()
        scoreb.increase()
        snake.extend()

    for segment in snake.segments[1:]:

            if snake.head.distance(segment) <= 10:

                #game_is_on=False
                scoreb.reset()






screen.exitonclick()

