from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        """Manages snake body segment creation, movement kinematics, and resets."""
        self.snake = []
        self.initial_body()
        self.head = self.snake[0]

    def create_segment(self, position):
        """Append a new square segment at a given (x, y) coordinate."""
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake.append(segment)

    def reset(self):
        """Send existing segments offscreen and reconstruct initial snake."""
        for segment in self.snake:
            segment.goto(1000,1000)
        self.snake.clear()
        self.initial_body()
        self.head = self.snake[0]

    def extend(self):
        """Add a segment to the tail of the snake."""
        self.create_segment(self.snake[-1].position())

    def initial_body(self):
        """Construct the starting 3-segment snake body."""
        for i in range(3):
            self.create_segment((i*-20, 0))

    def move(self):
        """Propagate positions from tail forward, then step head forward."""
        for seg_num in range(len(self.snake)-1, 0, -1):
            (new_x, new_y) = self.snake[seg_num-1].pos()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Direction setters preventing 180-degree instant reversal
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

