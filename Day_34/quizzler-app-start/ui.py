from tkinter import *
from quiz_brain import *
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz:QuizBrain):
        self.quiz_brain = quiz
        self.window = Tk()
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.window.title("Quizzler")

        #------------------- Score Label ---------------#
        self.score_label = Label(text="Score: 0",fg="white",bg=THEME_COLOR,font=("Arial",10,"italic"))
        self.score_label.grid(row=1,column=2)

        #------------------- Canvas -------------------- #
        self.canva_question = Canvas(height=250,width=300,bg="white")
        self.question = self.canva_question.create_text(150,100,
                                                        text="Welocme to quizzers",
                                                        font=("Arial",20,"italic"),
                                                        width = 280,
                                                        )
        self.canva_question.grid(row=2,column=1,columnspan=2,pady=50)

        #-------------------- right Button --------------- #
        right_image = PhotoImage(file=r"D:\projects\Udemy\100-days-of-code-Python\Day_34\quizzler-app-start\images\true.png")
        self.right_button = Button(image=right_image,command=self.correct_function)
        self.right_button.grid(row=3,column=1)

        #-------------------- wrong Button --------------- #
        wrong_image = PhotoImage(file=r"D:\projects\Udemy\100-days-of-code-Python\Day_34\quizzler-app-start\images\false.png")
        self.wrong_button = Button(image=wrong_image,command=self.wrong_function)
        self.wrong_button.grid(row=3,column=2)
        self.get_next_question()
    
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz_brain.still_has_questions():
            self.canva_question.config(bg="white")
            question = self.quiz_brain.next_question()
            self.canva_question.itemconfigure(self.question,text=question)
            self.update_score()
        else:
            self.canva_question.config(bg="orange")
            self.canva_question.itemconfigure(self.question,text="You've reached the end of the quiz!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def update_score(self):
        score = self.quiz_brain.score
        self.score_label.config(text=f"Score: {score}")

    def correct_function(self):
        self.feedback(self.quiz_brain.check_answer(user_answer="True"))
        

    def wrong_function(self):
        self.feedback(self.quiz_brain.check_answer(user_answer="False"))
        

    def feedback(self,resp):
        print(resp)
        if resp:
            print("inside")
            self.canva_question.config(bg='green')
        else:
            self.canva_question.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
        #self.canva_question.config(bg="white")
        
