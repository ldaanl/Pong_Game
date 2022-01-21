from turtle import Turtle

class Paddles(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(5,1)
        self.pu()
        self.goto(x,y)
    
    def move_up(self):
        if self.ycor() < 250:
            y = self.ycor() + 40
            self.goto(self.xcor(), y)
    
    def move_down(self):
        if self.ycor() > -250:
            y = self.ycor() - 40
            self.goto(self.xcor(), y)
        