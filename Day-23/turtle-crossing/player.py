from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """User-controlled player turtle constrained to vertical progression."""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.restart()

    def move_up(self):
        """Step vertically forward toward the finish line."""
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)

    def restart(self):
        """Reset player to starting rank facing North."""
        self.goto(STARTING_POSITION)
        self.setheading(90)
