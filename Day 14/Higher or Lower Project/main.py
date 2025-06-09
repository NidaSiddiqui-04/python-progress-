import random
import game_data
import art

data= game_data.data
def taking_input():
    score=0

    rand=random.choice(data)


    game_over=False
    while not game_over:
        rand = rand
        rand2 = random.choice(data)

        print("Compare A:", rand["name"], ", a", rand["description"], ", from", rand["country"])
        print(art.vs)

        print("Against B:",rand2["name"],",a",rand2["description"],", from",rand2["country"])
# +taking_input()

# function to compare  follower_count
# def comparison():
        choose = input("Who has more followers? Type 'A' or 'B'.").upper()

        if choose=="A":
             if rand["follower_count"]>rand2["follower_count"]:
                  rand =rand


                  score+=1
                  print(f"You are right.Current Score ={score} ")

             else:
                  game_over=True

                  print("\n"*20)
                  print(art.logo)
                  print(f"Sorry you're wrong .Your final score is {score}")
        else:
             if rand["follower_count"] < rand2["follower_count"]:
                  rand=rand2
                  score+=1
                  print(f"You are right.Current Score ={score} ")

             else:
                  game_over=True
                  print("\n"*20)
                  print(art.logo)
                  print(f"Sorry you're wrong .Your final score is {score}")
#comparison()

def game():
    print(art.logo)


    taking_input()

game()