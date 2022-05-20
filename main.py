from turtle import Screen
import snake
import time
from food import Food
from scoreboard import Scoreboard

UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'

# Configuring the screen (color / size)
screen = Screen()
screen.tracer(0)
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
t_list = []
game_is_on = True

# Defining objects of the game
snake_game = snake.Snake()
food = Food()
score = Scoreboard()

# Setting user keys
screen.listen()
screen.onkey(snake_game.up, UP)
screen.onkey(snake_game.down, DOWN)
screen.onkey(snake_game.left, LEFT)
screen.onkey(snake_game.right, RIGHT)

# Running the game.
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake_game.move()
    if snake_game.head.distance(food) < 20:
        food.refresh()
        snake_game.increase_length()
        score.add_point()
        # checking for collision with wall/tail
    if snake_game.head.xcor() > 290 or snake_game.head.xcor() < -290 or snake_game.head.ycor() > 290\
            or snake_game.head.ycor() < -290:
        score.game_over()
        game_is_on = False

    for segment in snake_game.t_list[1:len(snake_game.t_list)]:
        if snake_game.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False

screen.exitonclick()

