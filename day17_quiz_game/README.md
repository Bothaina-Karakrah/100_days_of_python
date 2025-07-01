# 📅 Day 17: Object-Oriented Programming (OOP) - The Quiz Project

## 🧠 What I Learned
<ul>
    <li>How to create and use <strong>classes</strong> and <strong>objects</strong></li>
    <li>Understanding <code>__init__()</code> constructor</li>
    <li>Creating methods inside a class</li>
    <li>Looping through a list of question objects</li>
    <li>Managing object state (<code>self.score</code>, <code>self.question_number</code>, etc.)</li>
</ul>

<pre><code class="language-python">
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
</code></pre>

## 📁 Files Created
<table border="1" cellpadding="5" cellspacing="0">
    <tr>
      <th>File</th>
      <th>Description</th>
    </tr>
    <tr>
      <td><code>question_model.py</code></td>
      <td>Defines the <code>Question</code> class</td>
    </tr>
    <tr>
      <td><code>data.py</code></td>
      <td>Contains a list of questions in dictionary format</td>
    </tr>
    <tr>
      <td><code>quiz_brain.py</code></td>
      <td>Main quiz logic: handles questions, scoring, and user input</td>
    </tr>
    <tr>
      <td><code>main.py</code></td>
      <td>Entry point for running the quiz</td>
    </tr>
  </table>

## 💡 Takeaways / Gotchas
<ul>
    <li>Use <code>self</code> to access instance attributes and methods inside the class.</li>
    <li>The quiz can be controlled using a <code>while self.still_has_questions()</code> loop.</li>
    <li>Use dot notation to access object attributes: <code>question.text</code>, <code>quiz.score</code>.</li>
  </ul>

## 🧪 Challenges & Practice
  <ul>
    <li>✅ Implemented OOP design using 3 classes</li>
    <li>✅ Replaced procedural code with class-based structure</li>
    <li>✅ Validated user input and updated score</li>
  </ul>

## 🛠️ Tools & Libraries Used
<ul>
    <li>Built-in Python libraries only</li>
    <li>No external packages used today</li>
  </ul>

## 🔗 Resources
<ul>
    <li><a href="https://docs.python.org/3/tutorial/classes.html" target="_blank">Python Classes Documentation</a></li>
    <li><a href="https://realpython.com/python3-object-oriented-programming/" target="_blank">OOP Cheat Sheet (Real Python)</a></li>
    <li><a href="https://www.udemy.com/course/100-days-of-code/" target="_blank">100 Days of Code - Course Link</a></li>
</ul>

## 🚀 Project of the Day: Quiz Game
	•	Displays multiple choice questions (True/False)
	•	User answers interactively in the terminal
	•	Displays final score and game over message

# Sample output
<img width="1128" alt="image" src="https://github.com/user-attachments/assets/1da21f92-5857-48bb-908c-b8803600e0bd" />


## 📓 Notes
<ul>
    <li>You can import question data from an external API or JSON to scale the quiz.</li>
    <li>This day sets the foundation for GUI-based projects that follow (Tkinter version in Day 34+).</li>
</ul>
