from turtle import Turtle

COLOR = 'white'
ALIGNMENT = 'center'
FONT = ('Arial', 18, 'normal')
POSITION = (0, 310)
class Score(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.goto(POSITION)
        self.color(COLOR)
        self.l_score = 0
        self.r_score = 0
        self.update()

    def increase_l(self):
        self.l_score += 1
        self.update()

    def increase_r(self):
        self.r_score += 1
        self.update()
    
    def update(self):
        self.clear()    
        self.write(f"{self.l_score} X {self.r_score}", align=ALIGNMENT, font=FONT)