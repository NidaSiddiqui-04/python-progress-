"""Many positional arguments"""

def add(*args):
    print(args)
    sum=0
    for n in args:
        sum+=n
    print(sum)

add(1,2,3,4,100)

""" Many keyword arguments"""
def calculate(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for key,value in kwargs.items():
        print(key)

calculate(add=3,multiply=7)
class Car:
    def __init__(self,**kwargs):
        self.model=kwargs.get("model")
        self.color=kwargs.get("color")


car=Car(model="brezza")
print(car.model )