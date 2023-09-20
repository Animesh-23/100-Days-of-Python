from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []
for que in question_data:
    question = Question(que['question'], que['correct_answer'])
    question_bank.append(question)

quiz = Quiz(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"You got {quiz.correct_que} out of {len(quiz.question_list)}")
