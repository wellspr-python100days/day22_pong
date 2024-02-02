from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score

import time

s = Screen()
s.setup(width=900, height=700, startx=0, starty=0)
s.screensize(canvwidth=800, canvheight=600)
s.bgcolor('black')
s.title("PyPong")
s.listen()
s.tracer(0)

writer = Turtle(visible=False)
writer.color('white')
writer.write(f"Press 'space' key to start game.", align='center', font=('Arial', 18, 'normal'))

def pong_game():
    pencil = Turtle(visible=False)
    pencil.color('white')
    pencil.penup()
    pencil.goto(-400, 300)
    pencil.pendown()
    pencil.goto(400, 300)
    pencil.goto(400, -300)
    pencil.goto(-400, -300)
    pencil.goto(-400, 300)

    score = Score()

    r_paddle = Paddle(350, 0)
    l_paddle = Paddle(-350, 0)

    s.onkey(r_paddle.up, 'Up')
    s.onkey(r_paddle.down, "Down")

    s.onkey(l_paddle.up, 'w')
    s.onkey(l_paddle.down, "s")

    ball = Ball()

    s.onkey(s.bye, 'q')

    def print_coords(x, y):
        print(x, y)

    s.onscreenclick(print_coords)

    max_points = 5

    while score.r_score < max_points and score.l_score < max_points:
        s.update()
        time.sleep(.1)

        ball.move()
        
        # paddle - ball collisions
        r_hits_the_ball = 350 - ball.xcor() < 20 and abs(ball.ycor() - r_paddle.ycor()) < 60
        l_hits_the_ball = ball.xcor() + 350 < 20 and abs(ball.ycor() - l_paddle.ycor()) < 60

        if r_hits_the_ball or l_hits_the_ball:
            ball.x_increment *= -1

        # ball - top and bottom walls collisions
        ball_hits_top = abs(300 - ball.ycor()) < 20
        ball_hits_bottom = abs(-300 - ball.ycor()) < 20

        if ball_hits_top or ball_hits_bottom:
            ball.y_increment *= -1

        # misses
        r_misses_ball = ball.xcor() > 350
        l_misses_ball = ball.xcor() < -350
        
        if l_misses_ball:
            score.increase_r()
            s.update()
            ball.initialize('left')
            time.sleep(1)

        if r_misses_ball:
            score.increase_l()
            s.update()
            ball.initialize('right')
            time.sleep(1)

    l_score = score.l_score
    r_score = score.r_score

    writer.goto(0, 0)
    writer.color('white')
    
    if l_score > r_score:
        writer.write(f"Left player wins.", align='center', font=('Arial', 18, 'normal'))
        print(f"Left player wins.")

    else:
        writer.write(f"Right player wins.", align='center', font=('Arial', 18, 'normal'))
        print(f"Right player wins.")

def play():
    s.resetscreen()
    pong_game()

s.onkey(play, 'space')

s.mainloop()