from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.score_paddle1 = 0
        self.score_paddle2 = 0
        self.scoreboard
    
    @property
    def scoreboard(self):
        self.goto(-50,250)
        self.write(self.score_paddle1, align='center', font = ('Arial', 30, 'normal'))
        self.goto(50,250)
        self.write(self.score_paddle2, align='center', font = ('Arial', 30, 'normal'))
        
    
    @property
    def points_paddle1(self):
        self.score_paddle1 += 1
        self.clear()
        self.scoreboard
    
    @property
    def points_paddle2(self):
        self.score_paddle2 += 1
        self.clear()
        self.scoreboard