# content from kids can code: http://kidscancode.org/blog/
# help from geeks for geeks: https://www.geeksforgeeks.org/


import pygame as pg
# turtle will allow me to create graphic illustrations
import turtle


# game settings 
WIDTH = 350
HEIGHT = 300
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128, 255)


# initiate pygame and window is created
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Manny's Game...")
clock = pg.time.Clock()
  

def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)


#create vertical moving platform
#platform 

plat = turtle.Turtle() #automatically creates a background screen
plat.speed(5)
#using this command I can simply type in the shape I want (given that it exists in the Turtle Screen's shape dictionary)
plat.shape("square")
#alows me to simply write the name of the color (I could also use the color code)
plat.color("black")
#numbers have to be positive (width, length,)
plat.shapesize(stretch_wid=6, stretch_len=2)
#"Pen-Up" simply means the created object does not draw anything on the sreen when moving
plat.penup()
#allows me to set the position of the object 
plat.goto(10,10)



# The Game loop
running = True
while running:
    clock.tick(FPS)
    dt = clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


# -----here are drawing instructions-----
        # background is drawn
        screen.fill(WHITE)
        # buffer - after drawing everything, flip display
        pg.display.flip()