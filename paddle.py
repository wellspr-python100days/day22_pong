from turtle import Turtle

SPEED = 'fastest'
COLOR = 'white'

class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__(shape='square')
        self.x = x
        self.y = y

        self.color(COLOR)
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.initialize()
        
        
    def initialize(self):
        self.goto(self.x, self.y)

    def up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 20)
