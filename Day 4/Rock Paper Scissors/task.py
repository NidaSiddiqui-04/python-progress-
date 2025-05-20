rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Rock Paper Scissors\ntype 0 for rock ,1 for paper,2 for scissor")
game=int(input("type:"))
if game==0:
    print(rock)
elif game==1:
    print(paper)
else :
    print(scissors)
import random
random_num=random.randint(0,2)
print("Computer")
if random_num==0:
    print(rock)
    if game==1:
        print("you won")
    elif game==0:
        print("its a tie")
    else:
        print("you lose")
elif random_num==1:
    print(paper)
    if game==1:
        print("its a tie")
    elif game==0:
        print("you won")
    else:
        print("you lose")
else :
    print(scissors)
    if game==1:
        print("you lose")
    elif game==0:
        print("you won")
    else:
        print("its a tie")