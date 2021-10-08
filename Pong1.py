# Made it to 17:10 in tutorial
# Link: https://youtu.be/XGf2GcyHPhc
import turtle
import winsound


# Test turtle code. Turtle starts near center and goes as far as you put. 100 not far. Runs before pong game.
# turtle.speed(1) - Dictates speed.
# turtle.forward(500) - Dictates distance.

# for i in range(10):         or loop range() dictates how long it lasts.
#     turtle.speed(10-i)      Goes fast then slow. i begins as 1. 1-10=9. Unless range is greater than 10. 0 is fastest.
#     turtle.forward(50+20*i)  This is the motion. (50+20*(i=1)=70. 90 degree turn. 50+20(i=2)=90. 90 degree turn.
#     turtle.right(90)

wm = turtle.Screen()
wm.title("Pong with Dave")
wm.bgcolor("black")
wm.setup(width=900, height=600)
wm.tracer(0)


# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
# .speed() gives whatever is attached to it a speed. 0 being fastest, 10-fast - 1-slowest.
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
# Keeps the ball from leaving a white trail. As in pen up, does not write on screen.
ball.penup()
ball.goto(0, 0)
ball.dx = .25
ball.dy = -.25

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player_A: 0    Player_B: 0", align="center", font=("Courier", 24, "normal"))


# Function ~~~~~~~~~
# Paddle a

def paddle_a_up():
    y = paddle_a.ycor()
    y += 50
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 50
    paddle_a.sety(y)


# Paddle b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 50
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 50
    paddle_b.sety(y)


# Keyboard binding
wm.listen()
wm.onkeypress(paddle_a_up, "w")
wm.onkeypress(paddle_a_down, "s")
wm.onkeypress(paddle_b_up, "Up")
wm.onkeypress(paddle_b_down, "Down")

# Main game loop.
while True:
    wm.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


# Border checking

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player_A: {}    Player_B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player_A: {}    Player_B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and Ball Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
