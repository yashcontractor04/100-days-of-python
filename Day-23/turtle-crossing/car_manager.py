import random
import time
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


def generate_random_cars():
    while True:
        time.sleep(0.1)
        car = CarManager()


class CarManager:
    """Handles continuous stochastic vehicle generation and directional kinematics."""
    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        """Generate a vehicle at a 1-in-6 frequency per tick to throttle spawn rates."""
        if random.randint(0, 5) == 0:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self, level):
        """Translate vehicles leftwards at velocities scaling with game progression."""
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + level * MOVE_INCREMENT)
