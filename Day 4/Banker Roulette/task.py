friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random

random_name=random.randint(1,5)
if random_name==1:
    print("Alice")
elif random_name==2:
    print("Bob")
elif random_name==3:
    print("Charlie")
elif random_name==4:
    print("David")
else:
    print("Emanuel")
# 2 method
random_name=random.randint(0,4)
print(friends[random_name])
# 3 method
print(random.choice(friends))# random.choice(seq.)
