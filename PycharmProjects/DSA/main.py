from sys import maxsize
top=-1
stack=[]

def push(e,stack):
    stack.append(e)
    return stack

print(push(20,stack))
print(push(30,stack))
