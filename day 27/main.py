from tkinter import *

window=Tk()
""" pack ,place ang grid manager layout"""
window.title("my first gui program")
window.minsize(width=500,height=300)
window.config(padx=30,pady=40)
my_label=Label(text="i am a label",font=("arial",20,"bold"))

my_label.grid(column=0,row=0)
my_label.config(padx=10,pady=40)
"""After object creation, treating the option name like a dictionary index"""

my_label["text"]="my name is nida"

"""Use the config() method to update multiple attrs subsequent to object creation"""
my_label.config(text="something")

# Button
def button_clicked():
    my_label.config(text=entry.get())
button =Button(text="click me",command=button_clicked)
button1=Button(text="press me")
button.grid(column=1,row=1)
button1.grid(column=3,row=0)
# Entry
entry=Entry(width=20)
entry.insert(END,string="used to enter a string.")
print(entry.get())
entry.grid(column=4,row=4)

# print(input.get())

# text
text=Text(width=20,height=5)

text.insert(END,"example of multiline text entry\n vhg")
print(text.get("2.0",END))
text.grid(column=5,row=5)
# # spin box
# def value():
#     print(spinbox.get())
#
# spinbox=Spinbox(from_=1,to=11,command=value)
# spinbox.pack()
#
#
# # scales
# def scale_value(value):
#     print(value)
# scale=Scale(from_=1, to=90,command=scale_value)
# scale.pack()
#
# #check button
# def check_on_off():
#     print(on_off.get())
# on_off=IntVar()
# checkbutton=Checkbutton(text="button",variable=on_off,command=check_on_off)
#
# checkbutton.pack()
# # radio button
# def choose_answer():
#     print(choose_option.get())
# choose_option=IntVar()
# radio_button_1=Radiobutton(text="option 1",value=1,variable=choose_option,command=choose_answer)
# radio_button_2=Radiobutton(text="option 2",value=2,variable=choose_option,command=choose_answer)
# radio_button_1.pack()
# radio_button_2.pack()
# # list box
# def choose_fruit(event):
#     print(list_box.get(list_box.curselection()))
# fruits=["apple","banana","cherry","litchi"]
# list_box=Listbox(height=7,width=30)
# for  fruit in fruits:
#     list_box.insert(fruits.index(fruit),fruit)
# list_box.bind("<<ListboxSelect>>",choose_fruit)
#
# list_box.pack()
window.mainloop()