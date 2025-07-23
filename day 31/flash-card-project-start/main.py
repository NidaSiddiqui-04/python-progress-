from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TIME=3000

current_word={}
data_to_dict={}
try:
   data_frame=pandas.read_csv("data/word_to_learn.csc")
   data_to_dict=pandas.DataFrame.to_dict(data_frame,orient="records")
except FileNotFoundError:
    originaldata=pandas.read_csv("data/french_words.csv")
    data_to_dict=originaldata.to_dict(orient="records")

else:
    data_to_dict=data_frame.to_dict(orient="records")



def change_word():


    global current_word,timer
    window.after_cancel(timer)
    current_word=random.choice(data_to_dict)


    front_canvas.itemconfig(image,image=card_front)
    front_canvas.itemconfig(text1,text="French",fill="black")
    front_canvas.itemconfig(text2,text=current_word["French"],fill="black")
    window.after(3000,func=flip_card)

def right_click():

    data_to_dict.remove(current_word)
    data=pandas.DataFrame(data_to_dict)
    data.to_csv("data/word_to_learn.csc",index=False)
    print(len(data_to_dict))
    change_word()
def flip_card():


        global current_word
        front_canvas.itemconfig(image,image=back_image)
        front_canvas.itemconfig(text1,fill="white",text="English")
        front_canvas.itemconfig(text2,fill="white",text=current_word["English"])
         






window=Tk()
window.title(string="Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
timer=window.after(3000,func=flip_card)

right_image=PhotoImage(file="C:/Users/nidas/PycharmProjects/day 31/flash-card-project-start/images/right.png")
right_button=Button(image=right_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=right_click)
right_button.grid(column=1,row=1)
left_image=PhotoImage(file="C:/Users/nidas/PycharmProjects/day 31/flash-card-project-start/images/wrong.png")
left_button=Button(image=left_image,bg=BACKGROUND_COLOR,highlightthickness=0,command=change_word)
left_button.grid(column=0,row=1)


back_image=PhotoImage(file="images/card_back.png")
card_front=PhotoImage(file="C:/Users/nidas/PycharmProjects/day 31/flash-card-project-start/images/card_front.png")
front_canvas=Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
image=front_canvas.create_image(400,263,image=card_front)
text1=front_canvas.create_text(400,150,font=("arial",40,"italic"))
text2=front_canvas.create_text(400,263,font=("arial",60,"bold"))
front_canvas.grid(column=0,row=0,columnspan=2)

change_word()
flip_card()





window.mainloop()
