# 📅 Day 19: Turtle Race

## 🧠 What I Learned
<ul>
  <li>How to use the <code>turtle</code> module for graphics in Python</li>
  <li>Creating multiple turtle instances and controlling their attributes</li>
  <li>Setting screen dimensions and using event listeners</li>
  <li>Using while loops to animate motion in the GUI window</li>
</ul>

<pre><code class="language-python">
from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# Create turtles and set position
# Loop to move turtles forward by a random amount
</code></pre>

## 📁 Files Created
<table border="1" cellpadding="6" cellspacing="0">
  <thead>
    <tr>
      <th>File</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>main.py</code></td>
      <td>Builds the turtle race simulation</td>
    </tr>
  </tbody>
</table>

## 💡 Takeaways / Gotchas
<ul>
  <li>Turtle graphics is stateful — always call <code>penup()</code> before repositioning</li>
  <li><code>turtle.textinput()</code> allows for simple GUI-based user input</li>
  <li><code>random.randint(a, b)</code> is useful to create dynamic motion</li>
  <li>Use <code>screen.exitonclick()</code> to keep the window open</li>
</ul>

## 🧪 Challenges & Practice
<ul>
  <li>✅ Created a multi-turtle race game</li>
  <li>✅ Used user input to place a bet</li>
  <li>✅ Displayed result based on which turtle won</li>
</ul>

## 🛠️ Tools & Libraries Used
<ul>
  <li><code>turtle</code> – for GUI graphics</li>
  <li><code>random</code> – to vary turtle speeds</li>
</ul>

## 🔗 Resources
<ul>
  <li><a href="https://docs.python.org/3/library/turtle.html" target="_blank">Turtle Documentation</a></li>
  <li><a href="https://www.udemy.com/course/100-days-of-code/" target="_blank">100 Days of Code - Course</a></li>
</ul>

## 🚀 Project of the Day: <em>Turtle Race Game</em>
<p>User picks a turtle by color and watches the turtles race to the finish line. The winner is announced based on the user's bet.</p>
