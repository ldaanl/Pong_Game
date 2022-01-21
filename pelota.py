from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.pelota_init()
    
    def pelota_init(self):
        self.ball = Turtle("circle")
        self.ball.color("blue")
        self.ball.pu()
    
    @property
    def movement(self):
        x = self.ball.xcor() + 0.1
        y = self.ball.ycor() + 0.1
        self.ball.goto(x, y)