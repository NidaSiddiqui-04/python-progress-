print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age= int(input("Enter the age:"))
if height >= 120:
    print("You can ride the rollercoaster")
    if age<=18:
        print("pay $7")
    elif age<22:
        print("pay $12")
    else:
        print("pay $14")
else:
    print("Sorry you have to grow taller before you can ride.")
