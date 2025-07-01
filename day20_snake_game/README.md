# 🐍 Day 20 & 21: Snake Game

Welcome to Days 20–21 of my **100 Days of Code - Python** challenge!  
Over these two days, I built the classic **Snake Game** using **Python's `turtle` module**, applying **Object-Oriented Programming (OOP)**, **animation loops**, and **event-driven programming**.

This project marks a major step in building interactive GUI apps and structuring Python code with clean, modular design.

---

## 🧠 What I Learned
- Building custom classes: `Snake`, `Food`, and `Scoreboard`
- Controlling real-time animation using `while` loop and `.update()`
- Handling keyboard events - `onkey`, `listen` - for direction control
- Detecting collisions with food, walls, and the snake’s own body
- Dynamically growing the snake and updating the score

---

## 🧱 Classes Used

| Class       | Responsibility                                  |
|-------------|--------------------------------------------------|
| `Snake`     | Controls the movement, segments, and growth      |
| `Food`      | Generates food objects randomly on the screen    |
| `Scoreboard`| Handles the score display and game over message  |
| `main.py`   | Initializes game loop and screen                 |

---

## 🎮 How to Play

1. Run `main.py`
2. Use the **arrow keys** to control the snake:
   - 🠖 Right arrow → move right  
   - 🠔 Left arrow → move left  
   - 🠕 Up arrow → move up  
   - 🠗 Down arrow → move down
3. Eat the food to grow and increase your score
4. Avoid hitting the wall or your own tail — or it's game over!

> The window stays open until you click anywhere to close it.

---

## 📁 Files Created

| File          | Description                                     |
|---------------|-------------------------------------------------|
| `main.py`     | Main game loop and screen setup                 |
| `snake.py`    | Snake class logic: create, move, grow, reset    |
| `food.py`     | Food class logic: randomly place food           |
| `scoreboard.py` | Manages score tracking and game over message |

---

## ✅ Features Implemented

- ✅ Snake made of multiple segments
- ✅ Continuous movement with arrow key control
- ✅ Real-time food collision and growth
- ✅ Score tracking and screen updates
- ✅ Wall collision detection
- ✅ Self-collision detection
- ✅ Game over message

---

## 🛠 Tools & Libraries

- `turtle` – graphics and animation
- `random` – food position generation
- `time` – animation delay
- `OOP` – clean structure and reusability

---

## 📸 Screenshot

<img width="400" alt="snake game preview" src="https://github.com/user-attachments/assets/39f9e226-044e-4d00-bb01-fc9ffa69de89" />

---

## 🔗 Resources

- [Turtle Graphics – Python Docs](https://docs.python.org/3/library/turtle.html)
- [100 Days of Code - Python Bootcamp](https://www.udemy.com/course/100-days-of-code/)
