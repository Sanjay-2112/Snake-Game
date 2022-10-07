from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for post in POSITION:
            self.add_snake(post)

    def add_snake(self, position):
        top = Turtle()
        top.penup()
        top.shape(name="square")
        top.color("white")
        top.goto(position)
        self.snake_body.append(top)

    def extend_snake(self):
        self.add_snake(self.snake_body[-1].position())

    def move(self):
        for t in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[t - 1].xcor()
            new_y = self.snake_body[t - 1].ycor()
            self.snake_body[t].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def reset(self):
        for i in self.snake_body:
            i.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]