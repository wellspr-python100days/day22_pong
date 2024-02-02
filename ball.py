from turtle import Turtle
import random

COLOR = 'white'

class Ball(Turtle):

    def __init__(self):
        super().__init__(shape='square')
        self.color(COLOR)
        self.penup()
        self.x_increment = 0
        self.y_increment = 0
        self.initialize()

    def initialize(self, direction='right'):
        self.goto(0, 10)
        new_x_increment = random.randint(15, 25)
        self.x_increment = new_x_increment if direction == 'right' else - new_x_increment
        self.y_increment = random.randint(5, 15)

    def move(self):
        self.goto(self.xcor()+self.x_increment, self.ycor()+self.y_increment)
        