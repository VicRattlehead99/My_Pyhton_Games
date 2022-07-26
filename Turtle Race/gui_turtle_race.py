from turtle import Turtle, Screen
import random

# Creating screen
screen = Screen()
screen.setup(width=800, height=400)
screen.title("TURTLE RACE")

# Creating turtles
turtle1 = Turtle("turtle")
turtle2 = Turtle("turtle")
turtle3 = Turtle("turtle")
turtle4 = Turtle("turtle")
turtle5 = Turtle("turtle")
turtle6 = Turtle("turtle")
turtle7 = Turtle("turtle")

# Creating finish line
pen = Turtle(visible=False)
pen.color("red")
pen.speed(0)
pen.penup()
pen.width(2)
pen.goto(x=270, y=180)
pen.pendown()
pen.goto(x=270, y=-180)

# Creating turtle object list to proceed randomly
turtle_list = [turtle1, turtle2, turtle3, turtle4, turtle5, turtle6, turtle7]

# Not to leave a track
turtle1.penup()
turtle2.penup()
turtle3.penup()
turtle4.penup()
turtle5.penup()
turtle6.penup()
turtle7.penup()

# Adjusting speeds
turtle1.speed(4)
turtle2.speed(4)
turtle3.speed(4)
turtle4.speed(4)
turtle5.speed(4)
turtle6.speed(4)
turtle7.speed(4)

# Adjusting colors
turtle1.color("blue")
turtle2.color("red")
turtle3.color("yellow")
turtle4.color("pink")
turtle5.color("black")
turtle6.color("orange")
turtle7.color("green")

# Adjusting locations
turtle7.goto(x=-350, y=150)
turtle6.goto(x=-350, y=100)
turtle5.goto(x=-350, y=50)
turtle4.goto(x=-350, y=0)
turtle3.goto(x=-350, y=-50)
turtle2.goto(x=-350, y=-100)
turtle1.goto(x=-350, y=-150)


# Function to check if the user input is valid
def check_input_is_valid(turtle_given):
    for a_turtle in turtle_list:
        if turtle_given == a_turtle.color()[0]:
            return True
    return False


# Reading input
chosen_turtle = screen.textinput(title="Make your bet.", prompt="Which turtle will win? Choose a color:")
chosen_turtle = str.lower(chosen_turtle)

# Not passing until valid input given
while not check_input_is_valid(chosen_turtle):
    chosen_turtle = screen.textinput(title="", prompt="Please select an appropriate choice:")
    chosen_turtle = str.lower(chosen_turtle)


# Basic move function to go forward
def move_forward(turtle_to_move):
    turtle_to_move.forward(10)


# Boolean value to indicate race is finished
finished = False


# Function to check race is finished
def check_finished(list_of_turtle):
    global finished
    for a_turtle in list_of_turtle:
        if a_turtle.position()[0] > 250:
            finished = True
            return a_turtle


# Moving randomly chosen turtles forward
while not finished:
    winner = check_finished(turtle_list)
    move_forward(random.choice(turtle_list))

# Checking if user win
if chosen_turtle == winner.color()[0]:
    print("CONGRATULATIONS! You won!")
else:
    print("Next time buddy.")

# Exiting when clicked
screen.exitonclick()
