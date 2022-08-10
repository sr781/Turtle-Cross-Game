from turtle import Turtle
import random
COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []

    def spawn_car(self):
        if random.randint(0, 100) < 10:  # 10 percent chance a car is generated
            turt = Turtle("square")
            turt.penup()
            turt.shapesize(1, 2)
            turt.color(random.choice(COLOURS))
            turt.speed("fastest")
            turt.goto(300, random.randint(-250, 300))
            self.cars.append(turt)

    def move(self, speed):  # Regulates the speed of each car
        for a in range(0, len(self.cars)):
            self.cars[a].forward(speed)
