len("12345")
# type() function
print(type("Name"))
print(type(123))
print(type(3.14159))
print(type(False))
# type conversion or type casting
print(int("45")+int("31"))

print(type("Number of letters in your name: "))#string datatype
print(type(len(input("Enter your name"))))#integer datatype
#print("Number of letters in your name: " + len(input("Enter your name")))
#str+str concatenate allowed
# str+int concatenate not allowed
print("Number of letters in your name: " + str(len(input("Enter your name"))))