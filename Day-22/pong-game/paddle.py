from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        """Represents a movable player paddle along the vertical axis."""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """Translate paddle upwards by 20 units."""
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        """Translate paddle downwards by 20 units."""
        self.goto(self.xcor(), self.ycor() - 20)
