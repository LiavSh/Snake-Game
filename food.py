# This class is responsible for creating the food objects in different places,
# as well as identifying when they were eaten by the snake.
from turtle import Turtle
import random

# Max coordinates that the food can appear, not too close to the edges
FOODLOCATIONMAX = 280
FOODLOCATIONMIN = -280


# Initialize food objects (green circle shape objects)
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    # Making a new food object every time the old one gets eaten
    def refresh(self):
        self.goto(random.randint(FOODLOCATIONMIN, FOODLOCATIONMAX), random.randint(FOODLOCATIONMIN, FOODLOCATIONMAX))



