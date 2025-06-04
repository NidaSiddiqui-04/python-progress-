from random import randint
from art import logo
print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number in between 1 and 100")
rand_num=randint(1,100)
e_or_h=input("Choose a difficulty.Type 'easy' or 'hard'").lower()


if e_or_h=="easy":
    i = 10
    print(f"You have {i} attempts to guess the number")
    guessing_over = False

    while not guessing_over:
        num = int(input("Make a Guess:"))
        i -= 1

        if num > rand_num:
            print("Too high")
        elif num < rand_num:
            print("Too low")
        else:
            print("Congratulations! You guessed the correct number.")
            guessing_over = True
            continue

        if i > 0:
            print("Try again")
            print(f"You have {i} attempts left")
        else:
            print("You run out of guesses. Refresh the page to run again")
            guessing_over = True

else:
    i = 5
    print(f"You have {i} attempts to guess the number")
    guessing_over = False

    while not guessing_over:
        num = int(input("Make a Guess:"))
        i -= 1

        if num > rand_num:
            print("Too high")
        elif num < rand_num:
            print("Too low")
        else:
            print("Congratulations! You guessed the correct number.")
            guessing_over = True
            continue

        if i > 0:
            print("Try again")
            print(f"You have {i} attempts left")
        else:
            print("You run out of guesses. Refresh the page to run again")
            guessing_over = True


