# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import pyperclip
import  json
def generatePassword():

    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f"Your password is: {password}")
    entryp.insert(0,password)
    pyperclip.copy(password)

def find_password():

    website=entryw.get()
    try:
        with open("data.json") as data_json:
            data_file=json.load(data_json)
    except FileNotFoundError:
        details = messagebox.showinfo(title=website, message="File not found")
    else:
        if f"{website}" in data_file:
            strp=data_file[f"{website}"]["password"]
            stre=data_file[f"{website}"]["email"]
            str=f"Email:{stre}\nPassword:{strp}"

            details = messagebox.showinfo(title=website, message=str)
        else:
            details = messagebox.showinfo(title=website, message="No details Found")

# ---------------------------- SAVE PASSWORD ------------------------------- #
# def check(str):
#     with open("data.txt") as fcheck:
#         for line in fcheck:
#             if str in line:
#                 return True

# def check(newdata): update takes care
#     with open("data.json") as json_dictionary:
#         for key in json_dictionary:
#             if newdata[f"{entryw.get()}"]['email'] in json_dictionary and newdata['website']['password'] in json_dictionary:
#                 return True
def saveinfile():
    website=entryw.get()
    password=entryp.get()
    email=entrye.get()
    newdata={
        website:{
            'email':email,
            'password':password
        }
    }
    #str=f"{entryw.get()} | {entrye.get()} | {entryp.get()}"
    if len(entryw.get())==0 or len(entryp.get())==0:
        isincomplete=messagebox.showinfo(title="Oops!Error",message="You have incomplete details")
    else:
        isOk = messagebox.askokcancel(title=entryw.get(),message=f"{website}|{email}|{password} are your details.\nIs it Ok to save?")
        if isOk :#and check(newdata)!=True:
            try:

                with open("data.json", 'r') as data_file:
                    old_data=json.load(data_file)


            except FileNotFoundError:
                data_file=open("data.json","w")
                json.dump(newdata,data_file,indent=4)
                data_file.close()
            else:
                old_data.update(newdata)
                with open("data.json","w") as data_file:
                    json.dump(old_data,data_file,indent=4)
            entryw.delete(0,END)
            entryp.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
FONT_NAME = "Courier"
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
#canvas img

canvas =Canvas(width="200",height="200")
logo=PhotoImage(file="logo.png")
canvas.create_image(100,109,image=logo)
canvas.grid(row=0,column=1)

#website
labelw=Label(text="Website")
labelw.grid(row=1,column=0,sticky="W")

#email login
labele=Label(text="Email/Username")
labele.grid(row=2,column=0,sticky="W")

#password
labelp=Label(text="Pasword")
labelp.grid(row=3,column=0,sticky="W")

#entry
entryw = Entry(width=40)
entryw.grid(row=1,column=1,columnspan=2,pady=10,sticky="W")

entrye = Entry(width=50)
entrye.grid(row=2,column=1,columnspan=2,pady=10,sticky="W")
entrye.insert(0,'sshanbhag01@gmail.com')
entryp = Entry(width=32)
entryp.grid(row=3,column=1,pady=10,sticky="W")

#Generate Password
button1 = Button(text="Generate Password",command=generatePassword)
button1.grid(row=3,column=2,sticky="W")
#add button
button2 = Button(text="Add",width=42,command=saveinfile)
button2.grid(row=4,column=1,columnspan=2,padx=20,pady=20,sticky="W")

button3=Button(text="Search",command=find_password)
button3.grid(row=1,column=2)
window.mainloop()
