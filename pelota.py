from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.pelota_init()
        self.x = 0.1
        self.y = 0.1
    
    def pelota_init(self):
        self.shape("circle")
        self.color("blue")
        self.pu()
    
    @property
    def reset_ball(self):
        self.goto(0, 0)
        self.luffyg4x
    
    @property
    def movement(self):
        x2 = self.xcor() + self.x
        y2 = self.ycor() + self.y
        self.goto(x2, y2)
    
    @property
    def luffyg4(self):
        self.y *= -1
    
    @property
    def luffyg4x(self):
        self.x *= -1
    


