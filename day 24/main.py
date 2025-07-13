# 1
file=open("C:/Users/nidas/PycharmProjects/day 24/my_file.txt")
content=file.read()
print(content)
# 2
""" by default mode is set to "r" read only 
to write new text set mode="w"
if mode="a" is to append existing  text in file at the end"""
with open("my_file.txt",mode="w") as file:

    file.write("\n student")
file.close()


# with open("new_file.txt") as new:
"""this wont work until we set mode to "a" """
with open("new_file.txt",mode="w") as new:
    new.write("Creating new file in python")
