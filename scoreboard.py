from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.goto(0, 260)
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Montserrat Medium', 24, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Montserrat Medium', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(arg="GAME OVER", move=False, align="center", font=('Calibri', 40, 'normal'))
        self.goto(0, -20)
        self.write(arg="(Press SPACE to exit.)", move=False, align="center", font=('Calibri', 16, 'italic'))
