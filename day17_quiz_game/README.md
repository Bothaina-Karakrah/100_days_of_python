# 📅 Day 17: Object-Oriented Programming (OOP) - The Quiz Project

🧠 What I Learned
	•	How to create and use classes and objects
	•	Understanding __init__() constructor
	•	Creating methods inside a class
	•	Looping through a list of question objects
	•	Managing object state (self.score, self.question_number, etc.)

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

📁 Files Created

File	Description
question_model.py	Defines the Question class
data.py	Contains a list of questions in dictionary format
quiz_brain.py	Main quiz logic: handles questions, scoring, and user input
main.py	Entry point for running the quiz

💡 Takeaways / Gotchas
	•	Use self to access instance attributes and methods inside the class.
	•	The quiz can be controlled using a while self.still_has_questions() loop.
	•	Use dot notation to access object attributes: question.text, quiz.score.

🧪 Challenges & Practice
	•	Implemented OOP design using 3 classes
	•	Replaced procedural code with class-based structure
	•	Validated user input and updated score

🛠️ Tools & Libraries Used
	•	Built-in Python libraries only
	•	No external packages used today

🔗 Resources
	•	Python Classes Documentation
	•	OOP Cheat Sheet (Real Python)
	•	Course: 100 Days of Code

🚀 Project of the Day: Quiz Game
	•	Displays multiple choice questions (True/False)
	•	User answers interactively in the terminal
	•	Displays final score and game over message

# Sample output
<img width="1128" alt="image" src="https://github.com/user-attachments/assets/1da21f92-5857-48bb-908c-b8803600e0bd" />


📓 Notes
	•	You can import question data from an external API or JSON to scale the quiz.
	•	This day sets the foundation for GUI-based projects that follow (Tkinter version in Day 34+).
