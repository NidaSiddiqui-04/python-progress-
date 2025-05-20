import random
import my_module

# random integer
random_int= random.randint(2,10)
print(random_int)
print(random.randint(21,25))

print(my_module.name)
#random floating point number
random_float_0_to_1=random.random()
print(random_float_0_to_1) # print 0.0<=num<1.0(1 is not included)
random_float_0_to_1=random.random()*10
# 0*10=0 amd 1*10=10 . print 0.0<=num<10(10 is not included)
#[0.0,10)
print(random_float_0_to_1)
random_float=random.uniform(1,10)
print(random_float)# print 1<=num<=10,i.e.[1,10]

coin= random.randint(0,1)
if coin==0:
    print("heads")
else:
    print("tails")