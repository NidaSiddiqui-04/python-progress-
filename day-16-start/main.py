# import turtle
#
# rumi=turtle.Turtle()
#
#
# rumi.shape("turtle")
# rumi.color("coral")
# rumi.forward(100)
#
# my_screen=turtle.Screen()
# print(my_screen.canvheight)
#
# print(my_screen.getshapes())
# print(my_screen.exitonclick())

from prettytable import PrettyTable

table=PrettyTable()


table.add_column("pokemon name",["Pikachu","Squirtle","Charmander"],"l")
table.add_column("type",["Electric","Water","Fire"],"l")
table.header_style="title"

# table.align="l"
print(table.align)
print(table)





