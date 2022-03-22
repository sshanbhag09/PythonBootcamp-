class Conversion:

    def isEmpty(self):
        return True if self.top == -1 else False

    def __init__(self):
        self.arr=[]
        self.conv=[]
        self.top=-1

    def stacktop(self):
        return self.arr[-1]

    def push(self,element):
        self.arr.append(element)

    def popped(self):
        return self.arr.pop()

    def prec(self,op):
        if op == '^':
            return 5
        elif op == "/":
            return 4
        elif op == "*":
            return 3
        elif op == "+":
            return 2
        elif op == "-":
            return 1
        else:
            return 0

    def infix_postfix(self,exp):

        for ch in exp:
            if ch>='A' and ch<='Z' or ch>="a" and ch<="z":
                self.conv.append(ch)
            elif ch=='(':

                self.arr.append(ch)
            elif ch == ')':
                a=""
                while(a!='('):
                    a= self.popped()

            else:
                while(self.isEmpty()==False and self.prec(ch)<=self.prec(self.stacktop())):
                    el=self.popped()
                    print("f")
                    self.conv.append(el)
                self.push(ch)
        print(self.conv)

exp=input("Enter expression")
obj=Conversion()
obj.infix_postfix(exp)
