# This class is responsible for creating and enlarging the snake as the player progresses in the game.
from turtle import Turtle

# Different angles for controlling snake movement
START_POS = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


# Initialize new snake object
class Snake:
    def __init__(self):
        self.t_list = []
        self.start_game()
        self.head = self.t_list[0]
        self.head.color("green")
        self.head.shape("circle")

    # Initialize snake shape / color / size
    def start_game(self):
        x = 0
        for i in range(0, 3):
            new_turtle = Turtle(shape="square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(x, 0)
            x -= 20
            self.t_list.append(new_turtle)

    # Method is responsible for the forward movement of the snake
    def move(self):
        for seg in range(len(self.t_list)-1, 0, -1):
            temp = self.t_list[seg-1]
            self.t_list[seg].goto(temp.xcor(), temp.ycor())
        self.head.forward(START_POS)

    # Method responsible for changing the direction of the snake by 90 degrees - upwards
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Method responsible for changing the direction of the snake by 90 degrees - right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # Method responsible for changing the direction of the snake by 90 degrees - left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Method responsible for changing the direction of the snake by 90 degrees - down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # method responsible for enlarging the snake when the user managed to collect another point by eating food object
    def increase_length(self):
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color("white")
        list_length = len(self.t_list)
        new_turtle.goto(self.t_list[list_length-1].pos())
        self.t_list.append(new_turtle)

