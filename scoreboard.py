from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.color("black")
        self.goto(-290, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)  # The scoreboard is initialised

    def scoreboard(self):  # Increases the level by 1 when called
        self.level = self.level + 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):  # This function is called if the game ends
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)