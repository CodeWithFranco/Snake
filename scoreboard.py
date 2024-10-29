from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        """
        Below statements are attributes
        """
        self.score = 0
        with open(r"\Users\franc\OneDrive\Desktop\data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()  # clear the previous text
        self.write(f"Score: {self.score} Hight Score: {self.high_score}", align="center", font=("Arial", 10, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"..\Users\franc\OneDrive\Desktop\data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
           
        self.score = 0
        self.update_score()

    # def game_end(self):
    #     self.penup()
    #     self.goto(x=0, y=0)
    #     self.write("Game Over", align="center", font=("Arial", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

