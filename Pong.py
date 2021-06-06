import turtle
import winsound

#Score
score_a = 0
score_b = 0

#Main Window
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#Bat A
bat_a = turtle.Turtle()
bat_a.speed(0)
bat_a.shape("square")
bat_a.shapesize(stretch_wid=5, stretch_len=1)
bat_a.color("red")
bat_a.penup()
bat_a.goto(-350, 0)

#Bat B
bat_b = turtle.Turtle()
bat_b.speed(0)
bat_b.shape("square")
bat_b.shapesize(stretch_wid=5, stretch_len=1)
bat_b.color("blue")
bat_b.penup()
bat_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = -0.5 

#Menu
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player Red: 0  |  Player Blue: 0", align = "center", font=("Courier", 24, "normal"))

#Function

#Bat A Functions
def bat_a_up():
    y = bat_a.ycor()
    y += 30
    bat_a.sety(y)

def bat_a_down():
    y = bat_a.ycor()
    y -= 30
    bat_a.sety(y)

#Bat B Functions
def bat_b_up():
    y = bat_b.ycor()
    y += 30
    bat_b.sety(y)

def bat_b_down():
    y = bat_b.ycor()
    y -= 30
    bat_b.sety(y)

#Keyboard binding
wn.listen()

#Bat A Keyboard binding
wn.onkeypress(bat_a_up, "w")
wn.onkeypress(bat_a_down, "s")

#Bat B Keyboard binding
wn.onkeypress(bat_b_up, "Up")
wn.onkeypress(bat_b_down, "Down")

#Main game loop
while True:
    wn.update()

    #Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player Red: {}  |  Player Blue: {}".format(score_a, score_b), align = "center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player Red: {}  |  Player Blue: {}".format(score_a, score_b), align = "center", font=("Courier", 24, "normal"))

    #Paddle and Ball Collisions
    if (ball.xcor() > 340  and ball.xcor() < 350) and (ball.ycor() < bat_b.ycor() + 40 and ball.ycor() > bat_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340  and ball.xcor() > -350) and (ball.ycor() < bat_a.ycor() + 40 and ball.ycor() > bat_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)