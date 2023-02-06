class QuizBrain:
    def __init__(self,questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?:")
        self.check_answer(answer,current_question.answer)

    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score +=1
        else:
            print("That is wrong.")
        print(f"The Correct Answer was: {correct_answer}")
        print(f"You current scaore is {self.score}/{self.question_number}")


    def still_has_question(self):
       return self.question_number < len(self.question_list)
        