import time
from turtle import Turtle, Screen
from food import Food
from scoreboard import Scoreboard

from snake import Snake

WALL_BOUNDARY = 285

# Display & screen buffer setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# Disable automatic screen updates for smooth frame rendering
screen.tracer(0)

# Instantiate game elements
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Bind directional keyboard controls
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

game_is_on = True
while game_is_on:
    # Manually refresh the frame buffer
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() < -WALL_BOUNDARY or snake.head.xcor() > WALL_BOUNDARY or snake.head.ycor() < -WALL_BOUNDARY or snake.head.ycor() > WALL_BOUNDARY:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail (if head collides with any segment in the tail trigger game_over)
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()





screen.exitonclick()