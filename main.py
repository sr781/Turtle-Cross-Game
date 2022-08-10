import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.tracer(0)
turtle = Player()
car = CarManager()
screen.setup(width=600, height=600)
score = Scoreboard()
screen.listen()
screen.onkey(turtle.move_up, "w")
game_is_on = True
speed = -5 #Initial speed of the car
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.spawn_car()
    car.move(speed)
    for num in range(0, len(car.cars)):  # If any of the cars touch the turtle, it is game over
        if ((car.cars[num].ycor() - 22) <= turtle.ycor() <= (car.cars[num].ycor() + 22)) and ((car.cars[num].xcor() - 25) <= turtle.xcor() <= (car.cars[num].xcor() + 25)):  # The marked boundaries of each car
            game_is_on = False
            score.game_over()
    if turtle.ycor() > 290:  # If statement is run when the turtle gets to the other side
        speed = speed - 2  # Speed of the cars increase
        score.scoreboard()  # Increase level by 1
        turtle.reset()  # Resets the position of the turtle
screen.exitonclick()
