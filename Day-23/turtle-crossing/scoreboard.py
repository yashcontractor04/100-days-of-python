from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    """Manages active stage levels and game-over overlay states."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 1
        self.update()

    def update(self):
        """Render level indicator in the top-left HUD corner."""
        self.clear()
        self.goto(-210, 260)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        """Advance stage progression and update UI."""
        self.level += 1
        self.update()

    def game_is_over(self):
        """Render centered game-over text notification."""
        self.goto(0, 0)
        self.write("GAME OVER :(", align=ALIGNMENT, font=FONT)