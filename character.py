from turtle import Turtle
TURTLE_STARTING_POSITION=(0,-280)
class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(TURTLE_STARTING_POSITION)
        self.move_speed=0.1

    def move_up(self):
        self.forward(10)

    def reset_game(self):
        self.goto(TURTLE_STARTING_POSITION)
        self.move_speed*=0.9