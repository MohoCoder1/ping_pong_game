from turtle import Turtle

BALL_MOVE_DISTANCE = 3


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = BALL_MOVE_DISTANCE
        self.y_move = BALL_MOVE_DISTANCE
        self.move_speed = .04

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= .9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = .1
        self.bounce_x()

