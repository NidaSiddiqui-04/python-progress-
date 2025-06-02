import art
print(art.logo)
def add(n1, n2):
    return n1+n2
def sub(n1, n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2



operation={ "+":add,
               "_":sub,
               "*":multiply,
               "/":divide,
            }
def calculator():
    calculation_over=False
    num1 = float(input("Enter your first number:"))
    while not calculation_over:

        for keys in operation:
            print(keys)
        operator=input("Choose the operation:")

        num2=float(input("Enter next number:"))
        num3=operation[operator](n1=num1,n2=num2)
        print(f"{num1} {operator} {num2} = {num3}")
        yes_or_no=input(f"Type 'y' to continue with {num3}. Type 'n' to start again: ").lower()
        if yes_or_no=="y":
            num1=num3
        if yes_or_no=="n":
            calculation_over=True
            print("\n"*20)
            calculator()
        if yes_or_no!="y" and yes_or_no!="n":
            calculation_over=True
calculator()
