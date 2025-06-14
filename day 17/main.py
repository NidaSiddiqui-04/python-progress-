# # class Student:#.PascalCase is used to name a class
#     collage_name="mata gujri "#class attributes
#     #default constructor
#     def __init__(self):# this function wont run
#             #parameterised constructor
#     def __init__(self,fullname,roll_no,marks):
#         self.name=fullname  #obj attributes
#         self.roll_no=roll_no
#         self.marks=marks
#         print("student")
#
#     def hello(self):
#         print("hello!" ,self.name)
#     def get_marks(self):
#         return self.marks
#
#
#
# s1=Student("nida","21","90")
# print(s1.collage_name)
# print(s1.name,s1.roll_no,s1.marks)
# s2=Student("sahil","22","87")
# print(s2.name,s2.roll_no,s2.marks)
# s3=Student("sarwar","23","92")
# print(s3.name,s3.roll_no,s3.marks)
# s3.hello()
# print(s3.get_marks())
class Student:
    @staticmethod#decorator
    def collage_name():# class method
        print("Mata Gujri ")
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):# instance method
        sum=0
        for i in self.marks:
            sum+=i
        print("hi",self.name,"your average marks is",sum/3)
stu1=Student("Nida",[89,89,77])
stu1.collage_name()
stu1.average()
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.acc=True
        self.clutch=True
        print("car started...")
    def stop(self):
        self.brk=True
        print("car stoped..")
c1=Car()
c1.start()
c1.stop()
""" creating an amount class with instance attributes
 balance and account no and creating methods to debit and credit amount"""
class Account:
    def __init__(self,balance,account_no):
        self.balance=(balance)
        self.account_no=account_no
    def debit(self,balance_deduct):
        self.balance_deduce=balance_deduct
        self.balance-=self.balance_deduce
        print("Rs",self.balance_deduce,"was debited from your account.Your current amount is:",self.balance)
    def credit(self,balance_credit):
        self.credit=balance_credit
        self.balance+=self.credit
        print("Rs",self.credit,"was credited in your account .Your current amount is:",self.balance)


user1=Account(8967.00,"5534101005160")
print(user1.account_no)
print(user1.balance)
user1.debit(2000)
user1.credit(1000)
