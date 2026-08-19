import time
from turtle import Screen
from player import Player
from car import Car
from car_manager import CarManager
from Scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

p1=Player()
car=Car()
scoreboard=Score()


p1.move_up()

screen.listen()
screen.onkey(p1.move_up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

#     Detect collision wit the cars
    for detection in car.cars:
        if detection.distance(p1)<20:
            game_is_on=False
            scoreboard.game_over()


    if p1.finish_line():
        p1.goto_starting_position()
        car.level_increase()
        scoreboard.score_increase()







screen.exitonclick()