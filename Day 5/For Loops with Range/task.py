# range() function is used in conjunction with another function
sum=0
for i in range(1,101):
    sum+=i
print(sum)
import random

list=" "
fruits=["apple ","banana "," ","cherry"]
for fruit in range(0,2):
    random_fruit=random.choice(fruits)
    list+=random_fruit
print(list)