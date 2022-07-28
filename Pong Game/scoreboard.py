from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.score_left = 0
        self.score_right = 0
        self.goto(0, 260)
        self.write(arg=f"{self.score_left} - {self.score_right}", move=False, align="center", font=('Montserrat Medium', 24, 'normal'))

    def increase_left_score(self):
        self.clear()
        self.score_left += 1
        self.write(arg=f"{self.score_left} - {self.score_right}", move=False, align="center", font=('Montserrat Medium', 24, 'normal'))

    def increase_right_score(self):
        self.clear()
        self.score_right += 1
        self.write(arg=f"{self.score_left} - {self.score_right}", move=False, align="center", font=('Montserrat Medium', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        if self.score_left > self.score_right:
            self.write(arg="LEFT IS WON!", move=False, align="center", font=('Calibri', 40, 'normal'))
        else:
            self.write(arg="RIGHT IS WON!", move=False, align="center", font=('Calibri', 40, 'normal'))
        self.goto(0, -20)
        self.write(arg="(Press SPACE to exit.)", move=False, align="center", font=('Calibri', 16, 'italic'))