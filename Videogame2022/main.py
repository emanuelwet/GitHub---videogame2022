# content from kids can code: http://kidscancode.org/blog/

# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random


# game settings
WIDTH = 500
HEIGHT = 650
FPS = 30


vec = pg.math.Vector2

# game settings 
WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128, 255)

def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)

# Returns a random integer in range (includes both end points)
def colorbyte():
    return random.randint(0,255)

# sprites...
class Player(Sprite):
        def __init__(self):
                Sprite.__init__(self)
                self.image = pg.Surface((50, 50))
                self.image.fill(WHITE)
                self.rect = self.image.get_rect()
                self.rect.center = (WIDTH/2, HEIGHT/2)
                self.pos = vec(WIDTH/2, HEIGHT/2)
                self.vel = vec(0,0)
                self.acc = vec(0,0)
        def jump(self):
                self.rect.x += 1
                hits = pg.sprite.spritecollide(self, all_plats, True)    
                self.rect.x += -1
                if hits:
                        self.vel.y = -20
        def update(self):
                self.rect.x += 5
                self.rect.y += 5 
                if self.rect.x > WIDTH:
                        self.rect.x = 0
                if self.rect.y > HEIGHT: 
                        self.rect.y = 0
        
        def update(self):
                self.acc = vec(0,1)
                self.rect.x += 5
                self.rect.y += 5 
                if self.rect.x > WIDTH:
                        self.rect.x = 0
                if self.rect.y > HEIGHT: 
                        self.rect.y = 0   



# platforms
class Platform(Sprite):
        def __init__(self, x, y, w, h):
                Sprite.__init__(self)
                self.image = pg.Surface((w, h))
                self.image.fill(BLACK)
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
        def controls(self):
                keys = pg.key.get_pressed()
                # if keys[pg.K_w]:
                #     self.acc.y = -5
                if keys[pg.K_a]:
                        self.acc.x = -1
                # use "a" to move left/ backwards
                #     self.acc.y = 5
                if keys[pg.K_d]:
                #use "d" to move right/ forward
                        self.acc.x = 1


# initiate pygame and window is created
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Manny's Pong Game...")
clock = pg.time.Clock()
  
# plateforms are created (size + position)
player = Player()

# groups are created
all_sprites = pg.sprite.Group()
all_plats = pg.sprite.Group()
mobs = pg.sprite.Group()



# The Game loop
running = True
while running:
    clock.tick(FPS)
    dt = clock.tick(FPS)
    hits = pg.sprite.spritecollide(player, all_plats, False)

# -----here are Updates-----

# all sprites are updated
all_sprites.update()

# -----here are drawing instructions-----
# background is drawn
screen.fill(GRAY)
# draws/ creates all sprites
all_sprites.draw(screen)
# creates an FPS counter (shows FPS)
draw_text("FPS: " + str(dt), 22, RED, WIDTH / 2, HEIGHT / 24)
# buffer - after drawing everything, flip display
pg.display.flip()

# ends pygame
pg.quit()