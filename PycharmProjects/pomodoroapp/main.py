import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps=0
timer=None
from tkinter import *
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(textc, text="00:00")
    checkmark.config(text="")
    global reps
    reps=0




# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    if reps%8==0:
        countdown(count=60*LONG_BREAK_MIN)
        label.config(text="Long Break",fg=RED)
    elif reps%2!=0:
        countdown(count=60*WORK_MIN)
        label.config(text="Timer",fg=GREEN)

    elif reps%2==0:
        countdown(count=60*SHORT_BREAK_MIN)
        label.config(fg=PINK,text="Short Break")



# --------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    checks = ""
    # if countm >=0:
    #      if count>0:
    #          window.after(1000, countdown, countm, count - 1)
    #
    #          canvas.itemconfig(textc, text=f"{countm-1}:{count}")
    #      else:
    #          count=59
    #          window.after(1000, countdown, countm-1, count )
    #          canvas.itemconfig(textc,text=f"{countm-1}:{count}")
    countm=math.floor(count/60)
    counts=count%60
    if counts<10:
        counts="0"+str(counts)

    canvas.itemconfig(textc, text=f"{countm}:{counts}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)

    else:
        start_timer()
        compl=math.floor(reps/2)
        for i in range(compl):
            checks+="✔"
        checkmark.config(text=checks)
# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Pomodoro App")

window.config(bg=YELLOW,padx=100,pady=100)
label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,35))
label.grid(row=0,column=1)


#window.minsize(height=500,width=500)
canvas =Canvas(width="200",height="224",bg=YELLOW,highlightthickness=0)

tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,109,image=tomato)
textc=canvas.create_text(100, 135, text='25:00',fill="white", font=(FONT_NAME, 35, 'bold'))

canvas.grid(row=1,column=1,padx=10,pady=10)


button1 = Button(text="Start",highlightthickness=0,command=start_timer)
button1.grid(row=3,column=0,ipadx=10,ipady=5)
button2 = Button(text="Reset",highlightthickness=0,command=reset_timer)
button2.grid(row=3,column=2,ipadx=10,ipady=5)

checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(row=4, column=1)

window.mainloop()