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
screen.tracer(0) #stops the window from updating, calls for manual update (allows to speedup games) )


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

#create the game ball (gb)
gb = turtle.Turtle()
gb.speed(0)
gb.shape("circle")
gb.color("Yellow")
gb.pendown()
gb.goto(0, 0) #center of screen







while True:
    screen.update()