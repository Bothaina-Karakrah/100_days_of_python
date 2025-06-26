from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions_bank = []
for e in question_data:
    questions_bank.append(Question(e["text"], e["answer"]))

# print(questions[0].answer)
quiz = QuizBrain(questions_bank)
while(quiz.still_has_questions()):
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")