from random import randint
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.9, stretch_len=0.9, outline=1)
        self.color("blue")
        self.speed("fastest")
        self.refresh()  # Moving the object to random location

    def refresh(self):
        random_x = 20 * randint(-14, 14)
        random_y = 20 * randint(-14, 14)
        self.goto(random_x, random_y)
        return random_x, random_y
