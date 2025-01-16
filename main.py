from turtle import Screen
from character import Character
from cars import Cars
from scoreboard import Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)

character=Character()
car=Cars()
scoreboard= Scoreboard()

screen.listen()
screen.onkey(character.move_up,"Up")
screen.onkey(character.move_up,"space")

game_is_on=True

while game_is_on:
    time.sleep(character.move_speed)
    car.create_car()
    car.move_car()
    screen.update()

    #detection of collision with the cars
    for i in car.total_car:
        if character.distance(i)<20:
            game_is_on=False
            scoreboard.game_over()

    #detection when turtle reaches other end
    if character.ycor()>280:
        scoreboard.next_round()
        character.reset_game()


screen.update()
screen.exitonclick()