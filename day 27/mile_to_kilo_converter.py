from tkinter import *



""" creating window"""
window=Tk()
window.title("Miles to Kilomiles Converter")
window.minsize(width=100,height=100)

"""creating entry"""
num=IntVar
entry=Entry(width=10)
entry.focus()


entry.grid(column=2,row=0)

"""creating labels"""
label1=Label(text="Miles",font=("arial",16))
label2=Label(text="km",font=("arial",16))
label3=Label(text="is equal to",font=("arial",16))
label4=Label(text=0,font=("arial",16))
label1.grid(column=3,row=0)

label2.grid(column=3,row=1)
label3.grid(column=0,row=1)
label4.grid(column=2,row=1)

"""creating button """
def calculation():
    miles=int(entry.get())
    km=(miles*1.609)
    print(label4.config(text=km))
button=Button(text="calculate",command=calculation)
button.grid(column=2,row=3)




window.mainloop()