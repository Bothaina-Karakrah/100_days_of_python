from turtle import Turtle
ALIGN = "left"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level=0
        self.goto(-270, 270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)