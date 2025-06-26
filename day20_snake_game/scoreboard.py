from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        with open("data.txt", 'a+') as file:
            content = file.read()
            self.high_score = int(content) if content else 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        # We will write after position it and style it
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        # Delete what previously writen
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_the_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()