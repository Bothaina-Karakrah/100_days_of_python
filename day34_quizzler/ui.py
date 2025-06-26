from tkinter import *
from quiz_brain import QuizBrain
# Constants
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        # Create score label
        self.score_label = Label(self.window, text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        # Create Canvas
        self.canvas = Canvas(self.window, width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width = 280,
            text ="some_text", fill=THEME_COLOR,
            font=("Arial", 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Define buttons
        check_img = PhotoImage(file="images/true.png")
        self.true_button = Button(self.window, image=check_img, command=self.true_pressed)
        self.true_button.config(highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        cross_img = PhotoImage(file="images/false.png")
        self.false_button = Button(self.window, image=cross_img, command=self.false_pressed)
        self.false_button.config(highlightthickness=0)
        self.false_button.grid(row = 2, column = 1)
        self.get_next_question()
        # Keep window open
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def false_pressed(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)

    def true_pressed(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        self.quiz.check_answer("Feedback")
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)