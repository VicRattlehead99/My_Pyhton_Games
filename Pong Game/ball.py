from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()

    def move(self):
        new_x = self.xcor() + 3
        new_y = self.ycor() + 3
        self.goto(new_x,new_y)
