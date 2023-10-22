from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.paused = False
        self.penup()
        self.hideturtle()
        self.level = 0
        self.write_level()

    def increase_level(self):
        self.level += 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"LEVEL: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
