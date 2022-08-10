from turtle import Turtle
STARTING_POSITION = (0, -280)  # Starting coordinates of the turtle
MOVE_DISTANCE = 10


class Player(Turtle):  # Turtle is created
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.speed("fastest")
        self.setheading(90)
        self.reset()

    def reset(self):  # Resets position of the turtle
        self.goto(STARTING_POSITION)

    def move_up(self):  # These functions control the direction of the board
        self.forward(MOVE_DISTANCE)


