import turtle
import pygame

pygame.mixer.init()
pygame.mixer.music.load("./pong.mp3")
pygame.mixer.music.play(-1)

# width and height
width = 800
height = 700

# set up game screen
turtle.setup(width, height)

# set game screen background color
turtle.bgcolor("black")


# GAME RULES

game_over = False
winner = None
points = {
    "player1" : 0, 
    "player2" : 0
}

game_rules = {
    "max_points": 3,
    "ball_speed": 3
}


# SCORE DISPLAY

score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player 1: 0 Player 2: 0", align="center", font=("Arial", 24, "normal"))


# creating the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0
ball.dy = 0


# left paddle
paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.color("red")
paddle1.shapesize(stretch_wid=5, stretch_len=1) # make the paddle wider
paddle1.penup()
paddle1.goto(-350, 0)
paddle1.dy = 0


# right paddle
paddle2 = turtle.Turtle()
paddle2.shape("square")
paddle2.color("blue")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)
paddle2.dy = 0


# FUNCTIONS

# move paddle1 up
def paddle1_up():
    paddle1.dy = 40

def paddle1_down():
    paddle1.dy = -40

def paddle2_up():
    paddle2.dy = 40

def paddle2_down():
    paddle2.dy = -40

def quit_game():
    game_over = True

def restart_game():
    game_over = False


# BALL SPEED
ball.dx = -50
ball.dy = 4

while game_over==False:

    paddle1.sety(paddle1.ycor() + paddle1.dy)
    paddle2.sety(paddle2.ycor() + paddle2.dy)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # check for game over conditions

    if points["player1"] == game_rules["max_points"]:
        game_over = True
        winner = "Player1"
    elif points["player2"] == game_rules["max_points"]:
        game_over = True
        winner = "Player2"


    # check for ball collision with paddles

    if ((ball.xcor() > (paddle2.xcor()-50)) and (ball.ycor() < (paddle2.ycor() + 50) and ball.ycor() > (paddle2.ycor() - 50))):
        
        ball.dx *= -1
        ball.dy *= -1

    elif ((ball.xcor() < (paddle1.xcor()+50)) and (ball.ycor() < (paddle1.ycor() + 50) and ball.ycor() > (paddle1.ycor() - 50))):
        
        ball.dx *= -1
        ball.dy *= -1

    # check for ball going off screen

    if ball.xcor() > 390:
        ball.goto(0, 0)
        paddle1.goto(-350, 0)
        paddle2.goto(350, 0)
        ball.dx *= -1
        points["player1"] += 1
        score_display.clear()
        score_display.write("Player_1: {} Player2: {}".format(points["player1"], points["player2"]), align="center", font=("Arial", 24, "normal"))

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        paddle1.goto(-350, 0)
        paddle2.goto(350, 0)
        ball.dx *= -1
        points["player2"] += 1
        score_display.clear()
        score_display.write("Player_1: {} Player2: {}".format(points["player1"], points["player2"]), align="center", font=("Arial", 24, "normal"))


    # check for ball colliding with the top or bottom of the screen

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    # check for paddles going offscreen

    if paddle1.ycor() > height/2:
        paddle1.dy *= -1

    elif paddle1.ycor() < -(height/2):
        paddle1.dy *= -1

    if paddle2.ycor() > (height/2):
        paddle2.dy *= -1

    elif paddle2.ycor() < -(height/2):
        paddle2.dy *= -1

   
    # event handling

    turtle.listen()
    turtle.onkeypress(paddle1_up, "w")
    turtle.onkeypress(paddle1_down, "s")
    turtle.onkeypress(paddle2_up, "Up")
    turtle.onkeypress(paddle2_down, "Down")
    turtle.onkeypress(quit_game, "q")

# GAME OVER

while game_over:

    game_over_display = turtle.Turtle()
    game_over_display.color("white")
    game_over_display.penup()
    game_over_display.hideturtle()
    game_over_display.goto(0, 0)
    game_over_display.write("Game Over! {} wins!".format(winner), align="center", font=("Arial", 36, "normal"))
    
    

