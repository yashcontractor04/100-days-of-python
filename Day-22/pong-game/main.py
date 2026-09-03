import time
import turtle
from turtle import Turtle, Screen

from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

# Display setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# Turn off auto-rendering for manual frame-rate management
screen.tracer(0)

# Initialise game objects
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-375, 0))
ball = Ball()
scoreboard = Scoreboard()

# Bind key listeners for two-player controls
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Frame refresh delay (decreases as rallies lengthen)
speed = 0.1

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(speed)
    ball.move()

    # Detect collision with the top and bottom edges of screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        speed *= 0.8

    # Right wall breach -> Left player scores
    if ball.xcor() > 380:
        ball.refresh()
        speed = 0.1
        scoreboard.l_point()

    # Left wall breach -> Right player scores
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()

screen.exitonclick()
