from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")



class Scoreboard(Turtle):
    """Tracks current and persistent high score with local file read/write."""
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Redraw score overlay."""
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """Persist new high score to disk and reset session score."""
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Increment score by 1 and update display."""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Render centered game-over screen."""
        self.goto(0,0)
        self.write("GAME OVER :(", align=ALIGNMENT, font=FONT)