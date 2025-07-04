class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {curr_question.text} (True/False): ")
        self.check_answer(user_answer, curr_question.answer)

    def check_answer(self, user_answer, q_answer):
        if user_answer.lower() == q_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {q_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def increase_score(self):
        self.score += 1