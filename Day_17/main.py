from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    new_question = Question(i['text'],i['answer'])
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question:
    quiz_brain.next_question()

print(" You've completed the quiz")
print(f"Your final score was:{quiz_brain.score}/{quiz_brain.question_number}")