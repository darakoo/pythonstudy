
###################
#The turtle module allows us to make the graphics dynamic 
import turtle

wind = turtle.Screen() #initialize the screen
wind.title("Ping Pong") #Window's name
wind.bgcolor("black") #Window's color
wind.setup(width=800, height=800*5/9) #window's height and width
wind.tracer(0) #Stop the window from updating automatically so that we'll be able to control the upadte of the window

#First paddle
paddle1 = turtle.Turtle() #initializes turtle objet(shape) (create an instance)
paddle1.speed(0) #set the speed animation
paddle1.shape("square") #set the object's shape
paddle1.color("blue") #set the object's color
paddle1.shapesize(stretch_wid=5, stretch_len=1) #modify the object's size
paddle1.penup() #stop the object from drawing lines while moving 
paddle1.goto(-370, 0) #set the position of the object

#Second paddle
paddle2 = turtle.Turtle() 
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("red")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(370, 0)

#The ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,190)
score.write("player1 : 0    Player2 : 0", align="center", font = ("Ariel",22,"normal") )

#functions
def paddle1_up(): #moving the paddle up/down by 20px
    if paddle1.ycor()+50 < 222.2222:
        y = paddle1.ycor() 
        y += 20
        paddle1.sety(y)

def paddle2_up():
    if paddle2.ycor()+50 < 222.2222:
      y = paddle2.ycor()
      y += 20
      paddle2.sety(y)
    
def paddle2_down():
    if paddle2.ycor()-50 > -222.2222:
       y = paddle2.ycor()
       y -= 20
       paddle2.sety(y)
        
def paddle1_down():
    if paddle1.ycor()-50 > -222.2222:
      y = paddle1.ycor()
      y -= 20
      paddle1.sety(y)
    
#keyboard bindings
wind.listen()  #tell the window to expect keyboard inputs  
wind.onkeypress(paddle1_up , "z") #when z is pressed the function paddle1_up gets executed
wind.onkeypress(paddle1_down , "s")
wind.onkeypress(paddle2_up , "Up")
wind.onkeypress(paddle2_down , "Down")


#main game loop
while True:
    wind.update() #updates the game everytime the loop runs
    ball.setx(ball.xcor()+ball.dx) #ball starts at 0.0 and moves by 0.1 px
    ball.sety(ball.ycor()+ball.dy) 
    
    #border check
    if ball.ycor()>220 : #if the ball reaches the top border we reverse it's direction 
        ball.sety(220)
        ball.dy *= -1
        
    if ball.ycor()<-220 : #if the ball reaches the bottom we reverse it's direction
        ball.sety(-220)
        ball.dy *= -1
        
    if ball.xcor()>390 : #if 1p scores we return the ball back to 0.0 and restart the game by reversing it's direction
        ball.goto(0,0) 
        ball.dx *= -1
        score1 += 1 
        score.clear()
        score.write("player1 : {}   Player2 : {}".format(score1,score2) , align="center", font = ("Ariel",22,"normal") )
        
    if ball.xcor()<-390 : #if 2p scores we return the ball back to 0.0 and restart the game by reversing it's direction
        ball.goto(0,0) 
        ball.dx *= -1  
        score2 += 1
        score.clear()
        score.write("player1 : {}   Player2 : {}".format(score1,score2) , align="center", font = ("Ariel",22,"normal") )
    #collision between the paddles and the ball
    if ball.xcor() < -360 and ball.xcor() > -370 and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() -40) :
        ball.setx(-360)     
        ball.dx *= -1  
     
    if ball.xcor() > 360 and ball.xcor() < 370  and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() -40) :   
        ball.setx(360)
        ball.dx *= -1