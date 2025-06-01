# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")
# Function with more than one input
def greet_with(name,location):
    print(f"hello {name}")
    print(f"What is it like in {location}")
greet_with("Nida", "Sihora")#positional  arguments
#greet_with("sihora","Nida")
# keyword argument
greet_with(location="Nowhere",name="Jack Baure")
# love calculator

def calculate_love_score(name1, name2):
    if "t" not in(name1 ,name2):
         t=name1.count("t")+name2.count("t")
         print(f"T occurs {t} times")
    if "r"not in(name1,name2) :
        r = name1.count("r") + name2.count("r")
        print(f"R occurs {r} times")
    if "u"not in(name1,name2) :
        u = name1.count("u") + name2.count("u")
        print(f"U occurs {u} times")
    if "e"not in(name1,name2) :
        e= name1.count("e") + name2.count("e")
        print(f"E occurs {e} times")
    true=str(t+r+u+e)
    print("Total="+true)
    if "l"not in(name1,name2) :
        l = name1.count("l") + name2.count("l")
        print(f"L occurs {l} times")
    if "o"not in(name1,name2) :
        o= name1.count("o") + name2.count("o")
        print(f"O occurs {o} times")
    if "v"not in(name1,name2) :
        v = name1.count("v") + name2.count("v")
        print(f"V occurs {v} times")
    if "e"not in(name1,name2) :
        e = name1.count("e") + name2.count("e")
        print(f"E occurs {e} times")
    love= str(l+o+v+e)
    print("Total="+love)
    print("Love Score=" +true+love)
calculate_love_score( name1 ="Teelo".lower(),name2="Trell".lower())
