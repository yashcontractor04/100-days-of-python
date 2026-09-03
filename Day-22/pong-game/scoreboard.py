from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        """Tracks and renders two-player scoreboard state."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        """Re-render both players' scores at their designated coordinates."""
        self.clear()
        self.goto(-100, 220)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 220)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        """Increment left player's score and update UI."""
        self.l_score += 1
        self.update()

    def r_point(self):
        """Increment right player's score and update UI."""
        self.r_score += 1
        self.update()
