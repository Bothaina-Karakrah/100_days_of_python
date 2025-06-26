import turtle
from turtle import Turtle, Screen
from random import randint

is_race_started = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "purple", "cyan"]
y_position = [-100, -60, -20, 20, 60, 100]

all_turtles = []
for idx in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[idx])
    new_turtle.penup()
    new_turtle.goto(-230,y_position[idx])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_started = True

while is_race_started:
    for turtle in all_turtles:
        rand_dict = randint(0, 10)
        turtle.forward(rand_dict)
        if turtle.xcor() >= 250:
            winner_turtle_color = turtle.pencolor()
            if winner_turtle_color == user_bet:
                print(f"Congratulations, you won! the {winner_turtle_color} turtle won")
            else:
                print(f"Sorry, you lost! the {winner_turtle_color} turtle won")
            is_race_started = False
            break


screen.mainloop()