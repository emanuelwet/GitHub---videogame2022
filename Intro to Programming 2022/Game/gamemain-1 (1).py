# create a video game 
# include all elements from the class works

#-----SOURCES----
    # Mr. Cozort's tutorial videos
    # content from kids can code: http://kidscancode.org/blog/
    
# import libraries and modules
# from platform import platform
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint

vec = pg.math.Vector2

# game settings 
WIDTH = 850
HEIGHT = 800
FPS = 30

# player settings
PLAYER_GRAV = 2
PLAYER_FRIC = 0.1
SCORE = 0

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
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
        self.image = pg.Surface((35,35))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(150, 1)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
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
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, all_plats, True)    
        self.rect.x += -1
        if hits:
            self.vel.y = -20
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        self.rect.x += 5
        self.rect.y += 5 
        if self.rect.x > WIDTH:
            self.rect.x = 0
        if self.rect.y > HEIGHT: 
            self.rect.y = 0
        # friction
        self.acc.x += self.vel.x * -0.1
        # self.acc.y += self.vel.y * -0.1
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # self.rect.x += self.xvel
        # self.rect.y += self.yvel
        self.rect.midbottom = self.pos

# platforms
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#snowflakes 
class Mob(Sprite):
    def __init__(self, x, y, w, h, color):
        Sprite.__init__(self)
        self.image = pg.Surface((5, 5))
        self.color = color
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.rect.x += -1
        self.rect.y += 1
        if (self.rect.x < 0):
            self.kill
        

# initiate pygame and window is created
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Manny's Game...")
clock = pg.time.Clock()
  
# groups are created
all_sprites = pg.sprite.Group()
all_plats = pg.sprite.Group()
mobs = pg.sprite.Group()

# plateforms are created (size + position)
player = Player()
plat = Platform(100, 500, 150, 35)
plat2 = Platform(550, 450, 70, 15)
plat3 = Platform(500, 350, 70, 15)
plat4 = Platform(0, 790, 600, 15)
plat5 = Platform(450, 250, 70, 15)
plat11 = Platform(350, 250, 70, 15)
plat6 = Platform(550, 750, 70, 15)
plat7 = Platform(600, 650, 70, 15)
plat8 = Platform(650, 550, 70, 15)
plat9 = Platform(700, 450, 70, 15)
plat10 = Platform(700, 250, 70, 15)
plat12 = Platform(250, 250, 70, 15)
plat13 = Platform(20, 250, 70, 15)
plat14 = Platform(20, 150, 70, 15)
plat15 = Platform(20, 50, 70, 15)
plat16 = Platform(220, 80, 70, 15)
plat17 = Platform(300, 90, 70, 15)
plat18 = Platform(380, 100, 70, 15)
plat19 = Platform(550, 100, 70, 15)

# finish base
plat20 = Platform(750, 250, 70, 15)
plat21 = Platform(810, 200, 10, 50)
plat22 = Platform(810, 180, 10, 20)
plat23 = Platform(750, 180, 70, 10)

\
# instructions for snowflakes (size, # of snowflakes to create)
for i in range(1000):
    m = Mob(randint(0,WIDTH), randint(0,HEIGHT), 10, 10, (colorbyte(),colorbyte(),colorbyte()))
    all_sprites.add(m)
    mobs.add(m)
   

# all sprite groups are having player added
all_sprites.add(player)
all_plats.add(plat, plat2, plat3, plat4, plat5, plat6,
    plat7, plat8, plat9, plat10, plat11, plat12, plat13, 
    plat14, plat15, plat16, plat17, plat18, plat19, plat20, 
    plat21, plat22, plat23)

# platforms are added to to all sprite groups
all_sprites.add(plat)
all_sprites.add(plat2)
all_sprites.add(plat3)
all_sprites.add(plat4)
all_sprites.add(plat5)
all_sprites.add(plat6)
all_sprites.add(plat7)
all_sprites.add(plat8)
all_sprites.add(plat9)
all_sprites.add(plat10)
all_sprites.add(plat11)
all_sprites.add(plat12)
all_sprites.add(plat13)
all_sprites.add(plat14)
all_sprites.add(plat15)
all_sprites.add(plat16)
all_sprites.add(plat17)
all_sprites.add(plat18)
all_sprites.add(plat19)

# the goal platforms are painted green 
plat23.image.fill(GREEN) 
plat20.image.fill(GREEN)
plat21.image.fill(GREEN)
plat22.image.fill(GREEN)
plat10.image.fill(GREEN)

all_sprites.add(plat20)
all_sprites.add(plat21)
all_sprites.add(plat22)
all_sprites.add(plat23)


# The Game loop
running = True
while running:
    clock.tick(FPS)
    dt = clock.tick(FPS)
    hits = pg.sprite.spritecollide(player, all_plats, False)
    if hits:
        player.pos.y = hits[0].rect.top
        player.vel.y = 0
    mobhits = pg.sprite.spritecollide(player, mobs, True)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.jump()
        
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
print("CONGRATULATIONS, you won!")