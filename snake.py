from turtle import Turtle

BEGINNING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        # self.head.shape("circle")
        # self.head.shapesize(stretch_len=1.5, stretch_wid=1)
    def create_snake(self):
        for i in range(0, 3):
            new_segment = Turtle()
            new_segment.penup()
            new_segment.color("white")
            new_segment.shape("square")
            new_segment.goto(BEGINNING_POSITIONS[i])
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, -1, -1):
            if seg_num == 0:
                self.segments[seg_num].forward(MOVE_DISTANCE)
            else:
                self.segments[seg_num].goto(self.segments[seg_num - 1].position())


    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def get_bigger(self):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.color("white")
        new_segment.shape("square")
        self.segments.append(new_segment)

    def restart(self):
        for seg in self.segments:
            seg.goto(10000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]













