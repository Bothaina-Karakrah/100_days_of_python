import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# -------------------- Screen Setup --------------------
# Create the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
# -------------------- Create Game Objects --------------------
player = Player()
car_manager = CarManager()
# -------------------- Keyboard Controls --------------------
screen.listen()
screen.onkey(player.up, "Up")

loop_num=0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if loop_num%6 == 0:
        car_manager.add_car()
    loop_num = (loop_num+1)%6
    car_manager.move_cars()

    ## check if the turtle arrived to the finish line
    if player.is_at_finished_line():
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.increase_level()

    ## Detect collusion with cars
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            break


# Wait for the user to click to close the window after the game ends
screen.exitonclick()