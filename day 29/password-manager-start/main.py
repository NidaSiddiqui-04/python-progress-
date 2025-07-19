from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
from random import shuffle
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']




    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)
    list=[]
    l1=[random.choice(letters) for letter in range(0,nr_letters)]
    list+=l1

    l2=[random.choice(numbers) for number in range(0,nr_numbers)]
    list+=l2

    l3=[random.choice(symbols) for sym in range(0,nr_symbols)]
    list+=l3


    shuffle(list)

    string_list="".join(list)
    # print( "the password is:",string_list)
    entry3.insert(0,string_list)
    # save_password()
    pyperclip.copy(text=string_list)
    save_password()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_entry=entry1.get()
    email=entry2.get()
    password_entry=entry3.get()
    if len(website_entry)==0 or len(password_entry)==0 :
        messagebox.showerror(title="Oops",message="Please make sure you haven't left any field empty")
    else:
        if_ok=messagebox.askokcancel(title=website_entry,message=f"These are the details entered:\nEmail :{email}\npassword :{password_entry}\n is it ok to save?")
        if if_ok:
            with open("data.txt",mode="a") as data:
                data.write(f"{website_entry} | {email} | {password_entry}\n")

    entry1.delete(0,"end")
    entry3.delete(0,"end")


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")

window.config(padx=50,pady=50)




# Creating label
website=Label(text="Website :")
website.grid(column=0,row=1)
user_name=Label(text="Email/Username :")
user_name.grid(column=0,row=2)
password=Label(text="Password :")
password.grid(column=0,row=3)

#creating entry
entry1=Entry(width=50)
entry1.focus()

entry1.grid(row=1,column=1,columnspan=2)
entry2=Entry(width=50)
entry2.insert(0,string= "nidasiddiqui.0404@gmail.com")
entry2.grid(row=2,column=1,columnspan=2)
entry3=Entry(width=32)
entry3.grid(column=1,row=3)
# creating button
generate_password=Button(text="Generate Password",width=14,command=generate_password)
generate_password.grid(column=2,row=3)
add=Button(text="Add",width=43,command=save_password)
add.grid(columnspan=2,column=1,row=4)
add.config()


# creating canvas
canvas=Canvas(width=200,height=200)
image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(column=1,row=0)








window.mainloop()