def add(*args):
    sum=0
    for n in args:
        sum=sum+n
    return sum

print(add(8,5,6,3))

def calculate(no,**kwargs):
    no+=kwargs["add"]
    no/=kwargs["divide"]
    print(no)
calculate(3,add=9,divide=0.5)