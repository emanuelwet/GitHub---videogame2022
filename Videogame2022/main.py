# EMANUEL WETSCHNIG

# content from kids can code: http://kidscancode.org/blog/
# help from geeks for geeks: https://www.geeksforgeeks.org/


import os
# turtle will allow me to create graphic illustrations
import turtle


import os
import turtle

#create background
screen = turtle.Screen()
screen.title("Manny's Pong Game...")
screen.bgcolor("White")
screen.setup(width=1050, height=650)


#create vertical moving platform
#platform 

plat1 = turtle.Turtle() #automatically creates a background screen
plat1.speed(5) #anywhere between 0-10
#using this command I can simply type in the shape I want (given that it exists in the Turtle Screen's shape dictionary)
plat1.shape("square")
#allows me to simply write the name of the color of the platform (I could also use the color code)
plat1.color("black")
#numbers have to be positive (width, length,)
plat1.shapesize(stretch_wid=6, stretch_len=2)
#"Pen-Up" simply means the created object does not draw anything on the sreen when moving
plat1.penup()
#allows me to set the position of the object 
plat1.goto(10,10)

