from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-270, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level:{self.level}", align='left', font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(arg="GAME OVER", move=False, align="center", font=('Calibri', 40, 'normal'))
        self.goto(0, -20)
        self.write(arg="(Press SPACE to exit.)", move=False, align="center", font=('Calibri', 16, 'italic'))
