#EMANUEL WETSCHNIG


##### SOURCES #####
# content from kids can code: http://kidscancode.org/blog/
# help from geeks for geeks: https://www.geeksforgeeks.org/
# help from https://www.youtube.com/watch?v=C6jJg9Zan7w&ab_channel=freeCodeCamp.org


# turtle will allow me to create graphic illustrations
import turtle

#create background
screen = turtle.Screen()
screen.title("Manny's Pong Game...")
screen.bgcolor("Purple")
screen.setup(width=800, height=650)
screen.tracer(0) #stops the window from updating, calls for manual update (allows to speedup games)


#create platform
#platform  
plat1 = turtle.Turtle() #automatically creates a background screen
plat1.speed(5) #anywhere between 0-10
#using this command I can simply type in the shape I want (given that it exists in the Turtle Screen's shape dictionary)
plat1.shape("square")
#allows me to simply write the name of the color of the platform (I could also use the color code)
plat1.color("black")
#numbers have to be positive (width, length,)
plat1.shapesize(stretch_wid=0.5, stretch_len=6)
#"Pen-Up" simply means the created object does not draw anything on the sreen when moving
plat1.penup()
#allows me to set the position of the object 
plat1.goto(0,-250)

#create the gameball (gb)
gb = turtle.Turtle()
gb.speed(0)
gb.shape("circle")
gb.color("Yellow")
gb.penup()
gb.goto(0, 0) #starting point = center of screen
#moving the ball

gb.xspeed = 0.05 #everytime the ball moves it moves by 0.05 pixels
gb.yspeed = 0.05
        
# Game score
player = 0

# Show the gamescore on the display (gamescore = gs)
gs = turtle.Turtle()
gs.speed(0)
gs.color("white")
gs.penup()
gs.hideturtle() #makes the curser/ drawing pen invisible and only shows the writing
gs.goto(0, 260)
gs.write("Player score : 0", align = "center", font = ("Times New Roman", 15, "normal"))


    # create functions to move objects #

# Platform moves to the left
def plat1_left():
    x = plat1.xcor()
#x coordinate decreases as object moves left, increases as it moves right
    x -= 10
    plat1.setx(x)

#allows me to move the platform to the right 
def plat1_right():
    x = plat1.xcor()
    x += 10
    plat1.setx(x)


#keyboard binding
screen.listen() #focuses on screen and acts on keyboard clicks
screen.onkeypress(plat1_left, "a") #when a/d keys are pressed the written action takes place
screen.onkeypress(plat1_right, "d")

# Moving the gameball 






# Main game loop

while True:
    screen.update()

    # Move the gameball
    gb.setx(gb.xcor() + gb.xspeed) #everytime it goes through the loop it moves by 0.05 pixels
    gb.sety(gb.ycor() + gb.yspeed)

    # Top and Bottom Borders
    if gb.ycor() > 300:
        gb.sety(300)
        gb.yspeed *= - 1 

    if gb.ycor() < -300:
        gb.sety(-300)
        gb.yspeed *= - 1
    
    #Left and Right Borders
    if gb.xcor() > 380:
        gb.setx(380)
        gb.xspeed *= -1
    
    if gb.xcor() < -390:
        gb.setx(-390)
        gb.xspeed *= -1

        