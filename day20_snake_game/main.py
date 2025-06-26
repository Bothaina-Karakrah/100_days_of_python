# Import necessary modules and classes
from turtle import Screen  # For creating the game window
from snake import Snake    # Custom Snake class to manage the snake behavior
from food import Food      # Custom Food class to handle the food
from scoreboard import Scoreboard  # Custom Scoreboard class to manage score display
import time                # For controlling the speed of the game loop

# -------------------- Screen Setup --------------------
# Create the game screen
screen = Screen()
screen.setup(width=600, height=600)  # Set screen dimensions
screen.bgcolor("black")              # Set background color
screen.title("Snake Game")           # Set window title
screen.tracer(0)                     # Turn off automatic screen updates (manual update control)

# -------------------- Create Game Objects --------------------
snake = Snake()            # Initialize the snake
food = Food()              # Initialize the food
scoreboard = Scoreboard()  # Initialize the scoreboard

# -------------------- Keyboard Controls --------------------
screen.listen()                   # Listen for keyboard input
screen.onkey(snake.up, "Up")     # Bind the "Up" key to move the snake up
screen.onkey(snake.down, "Down") # Bind the "Down" key to move the snake down
screen.onkey(snake.left, "Left") # Bind the "Left" key to move the snake left
screen.onkey(snake.right, "Right")# Bind the "Right" key to move the snake right

# -------------------- Game Loop --------------------
game_is_on = True
while game_is_on:
    time.sleep(0.1)        # Pause to control game speed (snake movement delay)
    screen.update()        # Manually update the screen after all drawing changes
    snake.move()           # Move the snake forward

    # ---------- Collision with Food ----------
    if snake.head.distance(food) < 17:
        food.refresh()            # Move food to a new random location
        snake.extend_snake()      # Add a new segment to the snake
        scoreboard.increase_score()  # Increase the score

    # ---------- Collision with Wall ----------
    if snake.hit_the_wall():      # Check if the snake hits the wall boundaries
        scoreboard.reset_the_scoreboard()
        snake.reset()

    # ---------- Collision with Tail ----------
    for segment in snake.segments[1:]:  # Exclude the head in collision check
        if snake.head.distance(segment) < 10:
            scoreboard.reset_the_scoreboard()
            snake.reset()

# Wait for the user to click to close the window after the game ends
screen.exitonclick()