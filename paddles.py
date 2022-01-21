from turtle import Turtle, color

class Paddles(Turtle):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.paddle_init()
    
    def paddle_init(self):
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.turtlesize(5,1)
        self.paddle.pu()
        self.paddle.goto(self.x, self.y)
    
    def move_up(self):
        y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), y)
    
    def move_down(self):
        y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), y)
    