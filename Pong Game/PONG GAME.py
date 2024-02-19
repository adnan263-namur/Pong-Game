import turtle

win = turtle.Screen()
win.title("First Pong Game")
win.bgcolor("grey")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle A
p_a = turtle.Turtle()
p_a.speed(0)
p_a.shape("square")
p_a.color("blue")
p_a.shapesize(stretch_wid=5, stretch_len=1)
p_a.penup()
p_a.goto(-350, 0)

# Paddle B
p_b = turtle.Turtle()
p_b.speed(0)
p_b.shape("square")
p_b.color("green")
p_b.shapesize(stretch_wid=5, stretch_len=1)
p_b.penup()
p_b.goto(350, 0)

# Balls
b = turtle.Turtle()
b.speed(0)
b.shape("circle")
b.color("red")
b.shapesize(stretch_wid=1, stretch_len=1)
b.penup()
b.goto(0, 0)
b.dx = 0.125
b.dy = 0.125

# Score
score_a = 0
score_b = 0

# Scoring
pen = turtle.Turtle()
pen.speed = 1
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


# Functions
def p_a_up():
    y = p_a.ycor()
    y += 20
    p_a.sety(y)


def p_a_down():
    y = p_a.ycor()
    y -= 20
    p_a.sety(y)


def p_b_up():
    y = p_b.ycor()
    y += 20
    p_b.sety(y)


def p_b_down():
    y = p_b.ycor()
    y -= 20
    p_b.sety(y)


# Keyboard binding
win.listen()
win.onkeypress(p_a_up, "w")
win.onkeypress(p_a_down, "s")
win.onkeypress(p_b_up, "Up")
win.onkeypress(p_b_down, "Down")
# Main Game Loop
while True:
    win.update()

    # Move the Ball
    b.setx(b.xcor() + b.dx)
    b.sety(b.ycor() + b.dy)

    # Border checking

    # Top and bottom
    if p_a.ycor() > 290:
        p_a.sety(290)

    if p_a.ycor() < -290:
        p_a.sety(-290)

    if p_b.ycor() > 290:
        p_b.sety(290)

    if p_b.ycor() < -290:
        p_b.sety(-290)

    if b.ycor() > 290:
        b.sety(290)
        b.dy *= -1

    if b.ycor() < -290:
        b.sety(-290)
        b.dy *= -1

    # Left and Right

    if b.xcor() > 390:
        b.goto(0, 0)
        b.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if b.xcor() < -390:
        b.goto(0, 0)
        b.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (b.xcor() > 340 and b.xcor() < 350) and (b.ycor() < p_b.ycor() + 50 and b.ycor() > p_b.ycor() - 50):
        b.setx(340)
        b.dx *= -1

    elif (b.xcor() < -340 and b.xcor() > -350) and (b.ycor() < p_a.ycor() + 50 and b.ycor() > p_a.ycor() - 50):
        b.setx(-340)
        b.dx *= -1