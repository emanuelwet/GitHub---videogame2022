
import pygame as pg
from pygame.sprite import Sprite
import turtle


# game settings 
WIDTH = 450
HEIGHT = 500
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
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

# platforms
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#create vertical moving platform
#platform 
plat = turtle.Turtle()
plat.speed(5)
plat.shape("square")
plat.color("black")
plat.shapesize(stretch_wid=6, stretch_len=2)
plat.penup()
plat.goto(100,50)



#create the groups
all_plats = pg.sprite.Group()


# plateforms are created (size + position)
player = Platform(10, 50, 50, 35)
plat1 = Platform(20, 40, 50, 35)
plat1.image.fill(BLACK)





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