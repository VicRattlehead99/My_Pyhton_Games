from turtle import Turtle

# Coordinates for 3 body segments at the start
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0), (-100, 0), (-120, 0), (-140, 0), (-160, 0),
                      (-180, 0), (-200, 0), (-220, 0), (-240, 0)]

# Distance set as constant to tweak the game if wanted in the future
MOVE_DISTANCE = 20

# Appointing angles
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:
    # self.segments[0] represents head of the snake

    def __init__(self):
        # Turtle objects list to represent body
        self.segments = []
        self.create_snake()

    def create_snake(self):
        # Taking list and using its tuples for coordinates
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Starting from end one by one
            self.segments[seg_num].goto(x=self.segments[seg_num - 1].xcor(), y=self.segments[seg_num - 1].ycor())
        self.segments[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if self.segments[0].heading() != DOWN:  # To prevent going backwards
            self.segments[0].setheading(UP)

    def move_right(self):
        if self.segments[0].heading() != LEFT:  # To prevent going backwards
            self.segments[0].setheading(RIGHT)

    def move_down(self):
        if self.segments[0].heading() != UP:  # To prevent going backwards
            self.segments[0].setheading(DOWN)

    def move_left(self):
        if self.segments[0].heading() != RIGHT:  # To prevent going backwards
            self.segments[0].setheading(LEFT)
