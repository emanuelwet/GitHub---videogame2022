#pong game 
#need two sides that can bounce a ball either vertically or horizontally

#import libraries and modules
#from platform import platform

import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint

# game settings 
WIDTH = 850
HEIGHT = 800
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
  

