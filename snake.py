from turtle import Turtle

starting_position = [(0, 0), (-20, 0), (-40, 0)]  # [0, 1, 2] Three pixels on the x-axis
move_distance = 20  # 20 pixels
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []  # attribute for an empty list. Always remember to use "self" when working within a class
        self.create_snake()  # method from function below
        self.head = self.segments[0]  # Creates the head of the snake at [0, 0]

    def create_snake(self):  # self is implied denoting that it is part of the initialization
        for position in starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)  # Refer to our attribute segment: [1, 2, 3] --> 3

    def extent(self):
        # add a new segment to the snake
        
        self.add_segment(self.segments[-1].position())  # start counting from the end of the list
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]  # Creates the head of the snake at [0, 0]

    def move(self):
        """
        First pixel should move and all following pixels should follow up to the last known location of
        the first one.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # for seg_num in range(start=len(segments) - 1, stop=0, step=-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # self.head.forward(move_distance) # another way to write it
        self.head.forward(move_distance)

        # self.segments[0].left(90)

    # Methods: up, down, left, and right
    def up(self):
        if self.head.heading() != DOWN:  # Make sure the snake is not moving down
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:  # Make sure the snake is not moving up
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:  # Male sure the snake is not moving right
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:  # Make sure the snake is not moving left
            self.head.setheading(RIGHT)
