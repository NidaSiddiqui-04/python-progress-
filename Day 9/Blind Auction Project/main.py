# TODO-1: Ask the user for input
import art

print(art.logo)
name=input("What is your name?:")
price=int(input("What is your bid?: $"))
# TODO-2: Save data into dictionary {name: price}
dict1={}
dict1[name]=price

# TODO-3: Whether if new bids need to be added

game_over=False
while not game_over:
    yes_or_no = input("any bidders ? Type 'yes' or 'no'")
    if yes_or_no=="yes":
        print("\n"*100)
        name = input("What is your name?:")
        price = int(input("What is your bid?:"))
        dict1[name]=price

    max_value = max(dict1.values())
    max_key = max(dict1, key=dict1.get)
    if yes_or_no=='no':
        game_over=True
        print(f"The winner is {max_key}  with a bid of ${max_value}")

# TODO-4: Compare bids in
