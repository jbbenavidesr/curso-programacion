import turtle
import os # Linux and Mac
# Windows import winsound

# Set up the screen
wn = turtle.Screen()
wn.title("Pong game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
scoreA = 0
scoreB = 0

# Paddle A
padA = turtle.Turtle()
padA.speed(0)
padA.shape("square")
padA.color("white")
padA.shapesize(stretch_wid=5, stretch_len=1)
padA.penup()
padA.goto(-350, 0)

# Paddle B
padB = turtle.Turtle()
padB.speed(0)
padB.shape("square")
padB.color("white")
padB.shapesize(stretch_wid=5, stretch_len=1)
padB.penup()
padB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))

# Functions
def padA_up():
    y = padA.ycor()
    y += 20
    padA.sety(y)

def padA_down():
    y = padA.ycor()
    y -= 20
    padA.sety(y)

def padB_up():
    y = padB.ycor()
    y += 20
    padB.sety(y)

def padB_down():
    y = padB.ycor()
    y -= 20
    padB.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(padA_up, "w")
wn.onkeypress(padA_down, "s")
wn.onkeypress(padB_up, "Up")
wn.onkeypress(padB_down, "Down")

#Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        # Mac: os.system("afplay bounce.wav&")
        # Linux
        os.system("aplay bounce.wav&")
        # Windows: winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions (Give them some time)
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < padB.ycor() + 50 and ball.ycor() > padB.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    if (ball.xcor() > -350 and ball.xcor() < -340) and (ball.ycor() < padA.ycor() + 50 and ball.ycor() > padA.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")