
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    window.after_cancel(timer)
    label.config(text="Timer")
    label_mark.config(text="")
    canvas.itemconfig(timer_text,text="00:00")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    # timer_on=True
    # while timer_on:
        global reps
        reps+=1
        work_sec=WORK_MIN*60
        short_break=SHORT_BREAK_MIN*60
        long_break=LONG_BREAK_MIN*60
        if reps==8:
            count_down(long_break)
            label.config(text="Break",fg=RED)
        elif reps==2 or reps==4 or reps==6:
            count_down(short_break)
            label.config(text="Break",fg=PINK)
        elif reps==1 or reps==3 or reps==5 or reps==7:
            count_down(work_sec)
            label.config(text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=  (count//60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        for mark in range(reps//2):
            marks+="✓"
        label_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("pomodoro")

window.config(padx=100,pady=100,bg=YELLOW)




# label
label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,25,"bold"))
label_mark=Label(fg=GREEN,bg=YELLOW,font=("arial",16))
label_mark.grid(column=2,row=3)

label.grid(column=2,row=1)


#button
button_start=Button(text="Start",highlightthickness=0,command=start_timer)
button_reset=Button(text="Reset",highlightthickness=0,command=reset_time)
button_start.grid(column=1,row=3)
button_reset.grid(column=3,row=3)
#image
canvas=Canvas(width=210,height=224,bg=YELLOW,highlightthickness=0)
image=PhotoImage(file="tomato.png")
canvas.create_image(102,112,image=image)
timer_text=canvas.create_text(102,125,text="00:00",fill="white",font=("arial",16,"bold"))

canvas.grid(column=2,row=2)


window.mainloop()