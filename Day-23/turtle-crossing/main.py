import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Display configuration
screen = Screen()
screen.setup(width=600, height=600)
# Disable automatic rendering for frame control
screen.tracer(0)

# Initialize actors
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# Register single-axis movement listener
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate obstacles probabilistically and step positions based on level
    car_manager.create_cars()
    car_manager.move(scoreboard.level)

    # Detect collision with cars
    for car in car_manager.all_cars:
        if  player.distance(car) < 15:
            game_is_on = False
            scoreboard.game_is_over()

    # Detect finish line
    if player.ycor() >= 280:
        scoreboard.increase_level()
        player.restart()

screen.exitonclick()