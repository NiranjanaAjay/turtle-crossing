from turtle import Turtle
import random
from types import new_class
STARTING_MOVE_DISTANCE=10


class Cars:
    def __init__(self):
        self.total_car=[]
        self.colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

    def create_car(self):
        random_num=random.randint(0,6)
        if random_num==6:
            new_car=Turtle()
            y_cor=random.randint(-200,200)
            x_cor= 390
            new_car.goto(x_cor, y_cor)
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(self.colors))
            self.total_car.append(new_car)

    def move_car(self):
        for i in self.total_car:
            i.backward(STARTING_MOVE_DISTANCE)
