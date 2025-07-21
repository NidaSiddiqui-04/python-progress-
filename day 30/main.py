# with open("my_file.txt") as data:
#     print(data.read()) FileNotFoundError: [Errno 2] No such file or directory: 'my_file.txt'
# try:
#     file=open("my_file.txt")
#     dict1={"key":"value"}
#     print(dict1["key"])
# except FileNotFoundError  :
#     file=open("my_file.txt",mode="w")
#     file.write("something")
#
#
# except KeyError as code:
#     print(f" there is no such {code} key exist")
#
# else:
#     data=file.read()
#     print(data)
# finally:
#     raise KeyboardInterrupt("this is an error that i made up")
# try:
#     file=open("new_file.txt",mode="w")45
#     # file.write("something")
# except:
#     print("no error found")
# else:
#     file.write("___")
height=float(input("height :"))
weight=int(input("weight :"))
if height >3:
    raise ValueError
if weight>200:
    raise ValueError


bmi=weight/height**2
print(bmi)