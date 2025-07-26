from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)

        self.label=Label(text="Score:0",bg=THEME_COLOR)
        self.label.config(fg="white")
        self.label.grid(column=1,row=0)


        self.wrong_image=PhotoImage(file="C:/Users/nidas/PycharmProjects/day 34/quizzler-app-start/images/false.png")
        self.wrong_button=Button(image=self.wrong_image,highlightthickness=0,bg=THEME_COLOR,command=self.false_pressed)
        self.wrong_button.config(pady=100,padx=100)
        self.wrong_button.grid(column=1,row=4)
        self.right_image=PhotoImage(file="C:/Users/nidas/PycharmProjects/day 34/quizzler-app-start/images/true.png")
        self.right_button=Button(image=self.right_image,bg=THEME_COLOR,command=self.true_pressed)
        self.right_button.config(padx=100,pady=100)
        self.right_button.grid(column=0,row=4)


        self.canvas=Canvas(height=250,width=300)
        self.question_text=self.canvas.create_text(150,125,width=280,text="some text",font=("arial",20,"italic"),fill=THEME_COLOR)

        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
    # def get_next_question(self):
    #     q_text=self.quiz.next_question()
    #     self.canvas.itemconfig(self.question_text,text=q_text)
    #

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
             self.label.config(text=f"Score:{self.quiz.score}")

             q_text = self.quiz.next_question()
             self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz game")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    def true_pressed(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right=  self.quiz.check_answer("false")
        self.give_feedback(is_right)
    def give_feedback(self,is_right):

        if is_right :
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,func=self.get_next_question)

