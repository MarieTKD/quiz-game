

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True or False?)")
        self.check_answer(user_answer, current_question.answer)




    def check_answer(self, user_answer, correct_answer):
        #current_question = self.question_list[self.question_number - 1]
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("That's right!")
        else:
            print("This is not the right answer, sorry.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


    def final_score(self):
        if self.still_has_questions() == False:
            print("You completed the quiz!")
            print(f"Your final score is: {self.score}/{self.question_number}")
