from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep
# -------------------- Screen Setup --------------------
# Create the game screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)        # Turn off automatic screen updates (manual update control)
# -------------------- Create Game Objects --------------------
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
# -------------------- Keyboard Controls --------------------
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
# -------------------- Game Loop --------------------
game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    ## Detect collusion with right paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor()> 320) or (ball.distance(left_paddle) < 50 and ball.xcor()) < -320:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_l_point()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_r_point()



# Wait for the user to click to close the window after the game ends
screen.exitonclick()