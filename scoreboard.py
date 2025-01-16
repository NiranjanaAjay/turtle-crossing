from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",20,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.level=1
        self.goto(0,260)
        self.write(f"LEVEL:{self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!",align=ALIGNMENT,font=FONT)

    def next_round(self):
        self.level+=1
        self.clear()
        self.write(f"LEVEL:{self.level}", align=ALIGNMENT, font=FONT)