# Modifying Global Scope

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

list1=[2,34,68,9]
def my_list():

    list1.append(100)
    return list1
print(my_list())

str1="nida"
def my_string():
    global str1
    print(str1.replace("nida","sahil"))
    return str1.replace("nida","sahil")
print(my_string())


