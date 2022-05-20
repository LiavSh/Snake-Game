# This Class is responsible for the scoreboard. Its initial setting and update when a player gets a point.
from turtle import Turtle

ALIGNMENT = "center"
SCORE = ("courier", 25, "normal")
OVER = ("courier", 45, "normal")


# Initialize the score-board size/shape/color/etc..
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("green")
        self.txt()

    # adding a point to the score-board
    def add_point(self):
        self.score += 1
        self.clear()
        self.txt()

    # turtle txt object showing the current score
    def txt(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=SCORE)

    # Game-over notification when the player hits the wall or its tail
    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=OVER)





