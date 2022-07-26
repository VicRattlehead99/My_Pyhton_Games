import time
from turtle import Screen
from food import Food
from snake import Snake

# Creating screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("SNAKE GAME")
screen.bgcolor("black")
screen.tracer(0)  # Hiding the creation of snake by stopping animations

snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(snake.move_up, "Up")
screen.onkeypress(snake.move_down, "Down")
screen.onkeypress(snake.move_left, "Left")
screen.onkeypress(snake.move_right, "Right")
screen.onkeypress(screen.bye, "space")

game_is_on = True

while game_is_on:
    screen.update()  # Updates the screen since there is no animations
    time.sleep(0.05)
    snake.move()

    # Detecting collision with food
    if snake.segments[0].distance(food) < 1:

        # Avoiding food spawn in body
        food_in_body = True  # To get in while loop
        while food_in_body:
            food_coordinate = food.refresh()  # Taking the coordinate of food
            food_in_body = False  # Assuming no collision with body
            for segment in snake.segments:  # Iterating through snake body
                # Spawning the food at least 10 distance away from the body
                if segment.distance(x=food_coordinate[0], y=food_coordinate[1]) < 20:
                    # Detecting collision with body
                    food_in_body = True
                    break  # Breaking the for loop and creating food in another location

        snake.extend()  # Increasing the snake size

    # Detecting collision with wall
    if snake.segments[0].xcor() >= 320:
        snake.segments[0].goto(x=-300, y=snake.segments[0].ycor())
    elif snake.segments[0].xcor() <= -320:
        snake.segments[0].goto(x=300, y=snake.segments[0].ycor())
    elif snake.segments[0].ycor() >= 320:
        snake.segments[0].goto(x=snake.segments[0].xcor(), y=-300)
    elif snake.segments[0].ycor() <= -320:
        snake.segments[0].goto(x=snake.segments[0].xcor(), y=300)

# Exiting when clicked
screen.exitonclick()
