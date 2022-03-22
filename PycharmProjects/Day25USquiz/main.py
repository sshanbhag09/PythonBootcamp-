import turtle
from turtle import Turtle,Screen
import pandas as pd

screen=Screen()
screen.title("US state Quiz")

image='blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data=pd.read_csv("50_states.csv")
state_list=data.state.to_list()
states_left=data.state.to_list()
#print(ans)
guess_state=[]
while len(guess_state)<50:
    ans = screen.textinput(f"{len(guess_state)}/50 guessed", "Name of the State").title()
    if ans == "Exit":
        break

    if ans in state_list:
        t=Turtle()
        t.penup()
        t.hideturtle()
        correct = data[data["state"] == ans]
        guess_state.append(ans)
        t.goto(float(correct.x),float(correct.y))
        if ans in states_left:
            states_left.remove(ans)
        t.write(ans)

print(guess_state)
df=pd.DataFrame({
    "State":states_left
})
df.to_csv("states_left.csv")

screen.mainloop()