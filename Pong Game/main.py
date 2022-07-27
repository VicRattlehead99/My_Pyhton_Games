from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')
# Caps Lock might be ON
screen.onkey(l_paddle.go_up, 'W')
screen.onkey(l_paddle.go_down, 'S')
screen.onkeypress(screen.bye, "space")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    # Detect collision between wall and ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision between paddles and ball
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.increase_speed()
        ball.bounce_x()

    # Detect missing the ball
    if ball.xcor() < -420:
        ball.reset_ball()
        scoreboard.increase_right_score()

    if ball.xcor() > 420:
        ball.reset_ball()
        scoreboard.increase_left_score()

    if scoreboard.score_left == 5 or scoreboard.score_right == 5:
        scoreboard.game_over()
        game_is_on= False

screen.exitonclick()
