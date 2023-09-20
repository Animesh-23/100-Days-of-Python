class Quiz:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.correct_que = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, ans, question):
        if ans == question.answer:
            self.correct_que += 1
            print(f"You got it right ({self.correct_que}/{self.question_number})")
        else:
            print(f"Wrong answer ({self.correct_que}/{self.question_number})")
        print(f"The correct answer was: {question.answer}")
        print('\n')

    def next_question(self):
        self.question_number += 1
        question = self.question_list[self.question_number - 1]
        ans = input(f"Q {question.text}? (True/False): ")
        self.check_answer(ans, question)
