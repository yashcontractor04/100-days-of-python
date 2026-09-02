import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        """Food target inheriting from Turtle that repositions randomly on consumption."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Teleport food to random coordinates within boundary margins."""
        (random_x, random_y) = (random.randint(-280, 280), random.randint(-280, 260))
        self.goto(random_x, random_y)
