from tkinter import  *

def button_clicked():

    m=int(entry.get())
    k=m*1.6
    change.config(text=k)

window = Tk()
window.title("My Mile To km Converter")
window.minsize(height=200,width=300)


#Mile
label = Label(text="Mile")
label.grid(column=3,row=0,padx=5,pady=5)
#Entry
entry=Entry(width=20)
entry.grid(column=2,row=0,padx=5,pady=5)
#Is equal
label1 = Label(text="is equal to")
label1.grid(column=0,row=1,padx=5,pady=5)
#change km
change=Label()
change.grid(column=1,row=1,sticky="e")
#km
label2 = Label(text="Km")
label2.grid(column=3,row=1)
#button
button=Button(text="Click me",command=button_clicked)
button.grid(column=2,row=2)

window.mainloop()
