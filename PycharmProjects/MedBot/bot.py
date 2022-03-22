from tkinter import *
from PIL import ImageTk,Image
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3 as pp
import random
import urllib.request
import urllib.parse
import re
switch =0;count1=0;count2=0
engine = pp.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 120)

def reset_tabstop(event):
    event.widget.configure(tabs=(event.width-8, "right"))

def hellow(event):
   print('Hi')

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot()

def bolo():
    speak(instanswer)

convo1 = []
f = open("conver.txt")
for lines in f:
    lines.strip()
    convo1.append(lines[:-1])
    lines.strip()
#print(convo)
convo2 = []
f = open("conver2.txt")
for lines in f:
    lines.strip()
    convo2.append(lines[:-1])
    lines.strip()
#print(convo)
trainer = ListTrainer(bot)

trainer.train(convo1)
trainer.train(convo2)

def findcategory(disease_n2):
    listofdis2 = disease_n2.split(" ")
    disease_name2 = "+".join(listofdis2)
    print(disease_name2)
    url2 = "https://www.nhsinform.scot/search?q="+disease_name2+"&locpt=&ds=&tab=inform"
    print(url2)

    values2  = {'s':'basics','submit':'search'}
    data2 = urllib.parse.urlencode(values2)
    data2 = data2.encode('utf-8')
    req2 = urllib.request.Request(url2,data2)
    resp2 = urllib.request.urlopen(req2)
    respData2 = resp2.read()


    paragraphs2 = re.findall(r'class="search__title">(.*?)</a>',str(respData2))
    #print(list(paragraphs2))
    paragraphs2.reverse()
    statements2 = {}
    for eachP in list(set(paragraphs2)):
        #print(eachP)
        if "NHS" in eachP:
            continue
        p1=[0];p2=[0]
        p1 = re.findall(r'<a href="(.*?)" title',str(eachP))
        p2 = re.findall(r'title="(.*?)">',str(eachP))
        #print(p1,p2)
        statements2[p2[-1]] = p1[-1]

    return statements2

def findcategory2(dis3):
    url3 = "https://www.nhsinform.scot"+dis3
    print(url3)

    values3  = {'s':'basics','submit':'search'}
    data3 = urllib.parse.urlencode(values3)
    data3 = data3.encode('utf-8')
    req3 = urllib.request.Request(url3,data3)
    resp3 = urllib.request.urlopen(req3)
    respData3 = resp3.read()

    paragraphs3 = list(re.findall(r'<h2(.*?)</h2>',str(respData3)))
    statements3= []
    for eachP in list(set(paragraphs3)):
        #print(eachP)
        if "NHS" in eachP or "About" in eachP:
            continue
        aaa = eachP.split(">")
        if aaa[-1] == "" or aaa[-1] == " ":
            continue

        statements3.append(aaa[-1])

    return statements3

def findcategory3(dis3):
    url3 = "https://www.nhsinform.scot"+dis3
    print(url3)

    values3  = {'s':'basics','submit':'search'}
    data3 = urllib.parse.urlencode(values3)
    data3 = data3.encode('utf-8')
    req3 = urllib.request.Request(url3,data3)
    resp3 = urllib.request.urlopen(req3)
    respData3 = resp3.read()


    paragraphs3 = list(re.findall(r'<h2(.*?)</h2>',str(respData3)))
    paragraphs4 = list(re.findall(r'<h2(.*?)<h2',str(respData3)))
    x = str(respData3).find(paragraphs4[0])
    paragraphs4 += list(re.findall(r'<h2(.*?)<h2',str(respData3)[x:]))

    statements3= [];statements4 = [];statements5 = []
    for eachP in list(set(paragraphs3)):
        #print(eachP)
        if "About" in eachP:
            continue
        #print(eachP)
        aaa = eachP.split(">")
        if aaa[-1] == "" or aaa[-1] == " ":
            continue
        statements3.append(aaa[-1])
    #print(statements3)
    #print(paragraphs4)
    for eachP in list(set(paragraphs4)):
        if "About" in eachP:
            continue
        eachP = eachP[1:]
        if eachP[:2] == "id":
            y = eachP.find(">")
            eachP = eachP[y+1:]
        #print(eachP)
        x = []
        p5 = list(re.findall(r'<p>(.*?)</p>',str(eachP)))
        for j in p5:
            if "href" in j:
                continue
            else:
                x.append(j)
        statements4.append((eachP[:50],x))
    #print(statements4)
    for i in statements3:
        n = len(i)
        for j,k in statements4:
            if i in j:
                statements5.append((i,k))
                break
    return statements5




def findans(disease_n):
    disease_n = disease_n.lower()
    if disease_n == "hairfall" or disease_n == "hair fall":
        disease_n = "baldness"
    listofdis = disease_n.split(" ")
    disease_name = "%20".join(listofdis)
    print(disease_name)
    url = "https://www.merriam-webster.com/dictionary/" + disease_name
    #print(url)

    #fp = open('C:/Users/ABHISHEK JAISWAL/Documents/Hackathon/diseases.txt','w+')

    #fp.write(soup.select('div p')[0].get_text() + '\n')
    #fp.close()

    values  = {'s':'basics','submit':'search'}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url,data)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    #print(respData)

    paragraphs = re.findall(r'<strong class="mw_t_bc">: </strong>(.*?)</span>',str(respData))
    #print(list(paragraphs))
    statement = []
    for eachP in list(set(paragraphs)):
        if "<" not in eachP:
            statement.append(eachP)

    if len(statement) == 0:
        loc = paragraphs[0].find("<")
        statement.append(paragraphs[0][:loc])
    return statement

root = Tk()
root.geometry("1000x750")
root.configure(background='#0a0a0a')
root.iconbitmap('abcd.ico')
root.title('MedGuru')
my_img =ImageTk.PhotoImage(Image.open("MG4.jpg"))
my_label = Label(image = my_img)
my_label.place(x=430,y=0)
text2  = Label(root,text = "Note: If you want information about any disease then type \"getinfo\"",fg = "#b8b8b8")
text2.place(x=320,y=158)

satisfy = ['ok','okk','okkk','all right','stop','chup','keep quiet','shut up','understand']
exitgreet = ['bye','byee','by by','bye bye','goodbye','good bye','byeee','byeeee','ok bye','okk bye']
unwanted = ['friend','marry','love','kiss','miss','kill','murder','fuck','idiot','sex','sexy','sing','play','dance','joke','climate','weather','favourite']
greet = ['hi','hii','hiii','hiiii','hello','helloo','hola','hiiiii','hlo','hlw','hey','heyy','whats up','helo',':)','yo','namaste']
greetresponse = ['namaste','hey there!','hi','hii','hiii','hiiii','hello','helloo','namaste','namaste','hola','hiiiii','hlo','hlw','hey','heyy',"hello, how may i help you?",]
satisfyresponse = ['you can ask any medical related question','you can type getinfo to know more','i can help you','i am not bad as you think so']

def ask_from_bot_():
    if switch == 0:
        ask_from_bot()
    else:
        findsolution()


def ask_from_bot():
    query = textF.get()
    tquery = query
    query = query.lower()
    global instanswer
    flag= 0
    if flag==0:
        if query == "getinfo":
            flag = 1
            info()
    if flag==0:
        if query in greet:
            flag = 1
            answer = random.choice(greetresponse)
            txt.configure(state = NORMAL)
            txt.insert(END," \t"+str(tquery)+"   \n "+ str(answer)+"\t  \n")
            #txt.insert(END,"MedGuru: " + str(answer)+"\n")
            txt.tag_add('demo', '0.0', '5.7')
            txt.tag_config('demo', background='#2ce6e2',foreground = "#000000")
            txt.tag_bind('demo', '<Double-1>', hellow)
            txt.yview(END)
            txt.configure(state = DISABLED)
            textF.delete(0,END)
            instanswer = answer
    if flag==0:
        if query in unwanted:
            flag =1
            answer = "please ask only medical related questions"
            txt.configure(state = NORMAL)
            txt.insert(END," \t"+str(tquery)+"   \n "+ str(answer)+"\t  \n")
            #txt.insert(END,"MedGuru: " + str(answer)+"\n")
            txt.tag_add('demo', '0.0', '5.7')
            txt.tag_config('demo', background='#2ce6e2',foreground = "#000000")
            txt.tag_bind('demo', '<Double-1>', hellow)
            txt.yview(END)
            txt.configure(state = DISABLED)
            textF.delete(0,END)
            instanswer = answer
    if flag==0:
        if query in satisfy:
            flag =1
            answer = random.choice(satisfyresponse)
            txt.configure(state = NORMAL)
            txt.insert(END," \t"+str(tquery)+"   \n "+ str(answer)+"\t  \n")
            #txt.insert(END,"MedGuru: " + str(answer)+"\n")
            txt.tag_add('demo', '0.0', '5.7')
            txt.tag_config('demo', background='#2ce6e2',foreground = "#000000")
            txt.tag_bind('demo', '<Double-1>', hellow)
            txt.yview(END)
            txt.configure(state = DISABLED)
            textF.delete(0,END)
            instanswer = answer
    if flag==0:
        answer = bot.get_response(query)
        instanswer = answer
        txt.configure(state = NORMAL)
        txt.insert(END," \t"+str(tquery)+"   \n "+ str(answer)+"\t  \n")
        #txt.insert(END,"MedGuru: " + str(answer)+"\n")
        txt.tag_add('demo', '0.0', '5.7')
        txt.tag_config('demo', background='#2ce6e2',foreground = "#000000")
        txt.tag_bind('demo', '<Double-1>', hellow)
        txt.yview(END)
        txt.configure(state = DISABLED)
        textF.delete(0,END)
        if query in exitgreet:
            speak("Good Bye")
            speak("See you soon")
            root.quit()
ignorelist = ["i","am","suffering","suffer","from","help","me","are","problem","tell","about","this","should","would","will","do",
                "disease","condition","conditions","matter","a","is","what","could","please","feeling","may","feel","we","can","my","get","gets","have","how","to",
                "away","from","rid","of","prevent","against","precautions","character","characteristics","feature","features","qualities","us","protect",
                "secure","precautions","precaution","symptom","affect","keep","avoid","treat","remove","reduce","cure","symptoms","away","how",
                "we","masure","major","measures","relief","relax","be","remedies","heal","take","stay","in","on","restore","recover","fall","mention",
                "expcect","reason","conditions","condition","treatment","benefit","benefits","gain","above","upon","below","down","up","the","well",
                "behind","diseases","quality","affected","secured","measured","number","not","for"," ","  ","which"]

def solveproblem():
    global switch
    if switch == 0:
        answer = "Tell me your problem!"
        instanswer = answer
        txt.configure(state = NORMAL)
        txt.insert(END,"\n "+str(answer)+"\t  \n")
        txt.tag_add('demo', '0.0', '5.7')
        txt.tag_config('demo', background='#2ce6e2',foreground = "#000000")
        txt.tag_bind('demo', '<Double-1>', hellow)
        txt.yview(END)
        txt.configure(state = DISABLED)
        textF.delete(0,END)
    if switch ==0:
        labelText.set("ON")
        label4.config(fg = "green")
        switch = 1
    else:
        labelText.set("OFF")
        label4.config(fg = "red")
        switch = 0

def findsolution():
    global count1
    global count2
    global category1keys
    global firstchoice
    global category1
    global category2
    answer = textF.get()
    instanswer = answer
    txt.configure(state = NORMAL)
    txt.insert(END,"\n "+str(answer)+"\t  \n")
    txt.tag_add('demo', '0.0', '5.7')
    txt.tag_config('demo', background='#2ce6e2',foreground = "#000000")
    txt.tag_bind('demo', '<Double-1>', hellow)
    txt.yview(END)
    txt.configure(state = DISABLED)
    count1+=1
    if count1<= 2:
        answer = "Type the correct number according to your match"
        instanswer = answer
        txt.configure(state = NORMAL)
        txt.insert(END,"\n "+str(answer)+"\t  \n")
        txt.tag_add('demo', '0.0', '5.7')
        txt.tag_config('demo', background='#2ce6e2',foreground = "#000000")
        txt.tag_bind('demo', '<Double-1>', hellow)
        txt.yview(END)
        txt.configure(state = DISABLED)
    if count1==1:
        query = textF.get()
        if query[-1] == "?":
            query = query[:-1]
        query= query.lower()
        print(query)
        textF.delete(0,END)
        txt.yview(END)
        ourlist = query.split(" ")
        print(ourlist)
        ourlist2=[]
        for l in ourlist:
            if l not in ignorelist:
                ourlist2.append(l)
        newquery = " ".join(ourlist2)
        category1 = findcategory(newquery)
        print(category1)
        category1keys = list(category1.keys())
        for l in range(len(category1keys)):
            answer = category1keys[l]
            instanswer = answer
            txt.configure(state = NORMAL)
            txt.insert(END,"\n "+str(l+1)+" : "+str(answer)+"\t  \n")
            txt.tag_add('demo', '0.0', '5.7')
            txt.tag_config('demo', background='#2ce6e2',foreground = "#000000")
            txt.tag_bind('demo', '<Double-1>', hellow)
            txt.yview(END)
            txt.configure(state = DISABLED)
    if count1 == 2:
        query = textF.get()
        firstchoice = category1keys[int(query)-1]
        category2 = findcategory2(category1[firstchoice])
        print(category2)
        n=1
        textF.delete(0,END)
        for l in range(len(category2)):
            answer = category2[l]
            if answer == "" or answer == " ":
                continue
            instanswer = answer
            txt.configure(state = NORMAL)
            txt.insert(END,"\n "+str(n)+" : "+str(answer)+"\t  \n")
            txt.tag_add('demo', '0.0', '5.7')
            txt.tag_config('demo', background='#2ce6e2',foreground = "#000000")
            txt.tag_bind('demo', '<Double-1>', hellow)
            txt.yview(END)
            n+=1
            txt.configure(state = DISABLED)

    if count1 == 3:
        count1-=1
        query = textF.get()
        secondchoice = category2[int(query)-1]
        #print(secondchoice)
        category3 = findcategory3(category1[firstchoice])
        textF.delete(0,END)
        for i, j in category3:
            if i == secondchoice:
                for k in j:
                    answer = k
                    instanswer = answer
                    txt.configure(state = NORMAL)
                    txt.insert(END,"\n  " +str(answer)+"\n")
                    txt.tag_add('demo', '0.0', '5.7')
                    txt.tag_config('demo', background='#2ce6e2',foreground = "#000000")
                    txt.tag_bind('demo', '<Double-1>', hellow)
                    txt.yview(END)
                    txt.configure(state = DISABLED)
                break



def info():
    engine = pp.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate', 120)
    textF.delete(0,END)

    def speak2(word):
        engine.say(word)
        engine.runAndWait()

    top = Toplevel()
    top.title("Disease Info")
    top.geometry("1000x750")
    b = Label(top,text = "Search for your disease",font = ("Impact",25),bd = 4)
    #b.grid(row = 0,column = 1,padx = 10,pady = 10)
    b.pack()
    a = Entry(top,font = ("Verdana",20),width = 40)
    #a.grid(row=1,column =1,columnspan = 5 )
    a.pack()

    def buttonpress():
        temp = a.get()
        global instanswer2
        temp = temp.lower()
        disanswer = findans(temp)
        txt2.configure(state = NORMAL);temp2 = ""
        txt2.delete('1.0',END)
        if len(disanswer) != 0:
            txt2.insert(END," " + str(temp.upper())+ " :" + "\n\n")
            for k in disanswer:
                temp2+= ", ," + k
                txt2.insert(END," * " + str(k) + "\n\n")
        txt2.configure(state = DISABLED)
        instanswer2 = temp2
        a.delete(0,END)
        txt2.yview(END)

    def call():
        print(instanswer2)
        speak2(instanswer2)

    e = Button(top,text = "Listen",font = ("Verdana",15),fg = "black",bg = "#b8b8b8",command = call)
    e.place(x =900,y = 137 )
    c = Button(top,text = "Search",font = ("Verdana",15),fg = "blue",bg = "#b8b8b8",command = buttonpress)
    #c.grid(row = 1,column = 4,padx = 10)
    c.pack()
    txt2 = Text(top)
    txt2.place(x=2,y=179,width=994,height = 530)
    #sc2 = Scrollbar(txt2)
    txt2.configure(state = DISABLED,yscrollcommand=sc.set,font = ("Helvetica Neue",15))
    #sc2.place(x=980,y=0,height = 500)
    def enter_function2(event):
        c.invoke()
    top.bind('<Return>',enter_function2)


# 12-22 is for frame where msgs are to be displayed
txt = Text(root)
txt.place(x=0,y=179,width=1000,height = 500)
sc = Scrollbar(txt)
txt.configure(state = DISABLED,yscrollcommand=sc.set,font = ("Helvetica Neue",15))
sc.place(x=980,y=0,height = 500)



#Input field
textF = Entry(root,font = ("Verdana",20),width = 58)
textF.place(x=0,y=679)

#for button
labelText = StringVar()
labelText.set('OFF')
label4 = Label(root,textvariable = labelText,bg = "#b8b8b8",fg = "red")
label4.place(x = 230,y=140,height = 30)
btn = Button(root,text = "Ask",font = ("Verdana",20),command = ask_from_bot_)
btn.place(x=928,y=679,height=37)
btn2 = Button(root,text = "listen",font = ("Verdana",20),command = bolo)
btn2.place(x=832,y=679,height=37)
btn3 = Button(root,text = "Solve My Problem",font = ("Verdana",13),command = solveproblem)
btn3.place(x=50,y=140,height = 30)

#footer = Label(root,text = "team khatarnak")
#footer.pack(side = LEFT)

def enter_function(event):
    btn.invoke()

root.bind('<Return>',enter_function)

#bot.storage.drop()
txt.bind("<Configure>", reset_tabstop)

root.mainloop()
