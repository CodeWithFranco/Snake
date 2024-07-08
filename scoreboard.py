from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        """
        Below statements are attributes
        """
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()  # clear the previous text
        self.write(f"Score: {self.score}", align="center", font=("Arial", 10, "normal"))

    def game_end(self):
        self.penup()
        self.goto(x=0, y=0)
        self.write("Game Over", align="center", font=("Arial", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

