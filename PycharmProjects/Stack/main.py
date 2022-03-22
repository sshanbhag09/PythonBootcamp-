top=-1
list=[]
def stackunderflow(list):
    global top
    if top==-1:
        return True
    else:
        return False
def push(list,e):
    global top
    if stackunderflow(list)==False:

        top =top + 1
        list[top]=e
    else:
        pass

def pop(list):
    global  top

    x = list[top]
    top=top-1
    return x

def display(list):
    global top
    for i in range(top,-1,-1):
        print(list[i])


push(list,20)
push(list,30)
push(list,45)

display(list)