import time
from turtle import Screen
from snake import Snake

# Creating screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("SNAKE GAME")
screen.bgcolor("black")
screen.tracer(0)  # Hiding the creation of snake by stopping animations

snake = Snake()
game_is_on = True

while game_is_on:
    screen.update()  # Updates the screen since there is no animations
    time.sleep(0.05)
    snake.move()

# Exiting when clicked
screen.exitonclick()
