from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        """Handles ball ballistics, reflection vectors, and resets."""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """Increment ball position along current trajectory vectors."""
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_x(self):
        """Invert horizontal trajectory on paddle deflection."""
        self.x_move *= -1

    def bounce_y(self):
        """Invert vertical trajectory on boundary wall collision."""
        self.y_move *= -1

    def refresh(self):
        """Reset ball to center and serve toward the opposing player."""
        self.goto(0, 0)
        self.bounce_x()
