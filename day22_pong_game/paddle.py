from turtle import Turtle

# Define the Paddle class that inherits from Turtle
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    # Method to move the paddle up
    def up(self):
        self.sety(self.ycor() + 20)  # Increase the y-coordinate by 20 units

    # Method to move the paddle down
    def down(self):
        self.sety(self.ycor() - 20)  # Decrease the y-coordinate by 20 units