from turtle import Screen
from character import Character

screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)


character=Character()


screen.update()
screen.exitonclick()