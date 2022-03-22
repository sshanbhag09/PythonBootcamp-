# import tkinter
#
# window = tkinter.Tk()
# window.title("My first Gui")
# window.minsize(height=500,width=500)
# label = tkinter.Label(text="This is label",font=("Arial",24,"bold"))
#
# label.pack(expand="True")
# def button_clicked():
#     label["text"]="This Is Sushant"
#     label.config(text="This is Sanvi")
# button=tkinter.Button(text="Click me",command=button_clicked)
# button.pack(expand="True")
# window.mainloop()

from tkinter import *
def button_clicked(*args):

    label["text"]=change.get()
window = Tk()
window.title("My first Gui")
window.minsize(height=500,width=500)
window.config(padx=100,pady=200)
label = Label(text="This is label",font=("Arial",24,"bold"))

label.grid(column=0,row=0)



button=Button(text="Click me 2 pos",command=button_clicked)
button.grid(column=1,row=1)

button=Button(text="Click me",command=button_clicked)
button.grid(column=2,row=0)
#Entry
change=Entry(width=20)
change.grid(column=2,row=2)
window.mainloop()

