# EMANUEL WETSCHNIG


##### SOURCES #####
# help + basecode from https://www.youtube.com/watch?v=NIfkaOF3Hjs&list=PLjcN1EyupaQlbAyHLsuFIp0n6i_p8XWaO&ab_channel=CodingWithRuss    
# content from kids can code: http://kidscancode.org/blog/
# help from geeks for geeks: https://www.geeksforgeeks.org/
# help from https://www.youtube.com/watch?v=C6jJg9Zan7w&ab_channel=freeCodeCamp.org  
# help from https://www.youtube.com/watch?v=dGwmmBBMlKs&ab_channel=buildwithpython

import pygame
from pygame.locals import *
import os


#setup asset folders here
#game_folder = os.path.dirname(__file__)
#img_folder = os.path.join(game_folder, "images")




pygame.init()


#Screen settings
screen_width = 800
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Manny's Keep-Up Game")

#text font (for all text)
font = pygame.font.SysFont('Algerian', 30)

#define colors
#gb.color = (234, 218, 184)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PURPLE = (238,130,238)
GRAY = (128, 128, 128, 255)

#platform and gameball colors
plat1_col = (WHITE)
plat1_outline = (GRAY)

#text color
text_col = (BLACK)


#define game settings
cols = 6
rows = 6
clock = pygame.time.Clock()
fps = 60
live_gb = False
game_over = 0

#getting text on the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#platform class
class plat1():
    def __init__(self):
        self.reset()

    def move(self):
        #moevement direction gets reset
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1
        if key[pygame.K_d] and self.rect.right < screen_width:
            self.rect.x += self.speed
            self.direction = 1

    def draw(self):
        pygame.draw.rect(screen, plat1_col, self.rect)
        pygame.draw.rect(screen, plat1_outline, self.rect, 3)


    def reset(self):
        #define platform variables
        self.height = 20
        self.width = int(screen_width / cols)
        self.x = int((screen_width / 2) - (self.width / 2))
        self.y = screen_height - (self.height * 2)
        self.speed = 10
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0


#game ball class
class game_gb():
    def __init__(self, x, y):
        self.reset(x, y)

    def move(self):
        #collision threshold
        collision_thresh = 5
        #wall collision
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1
        #collisions w/ top + bottom of screen
        if self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.bottom > screen_height:
            self.game_over = -1


        #collission w/ the platform
        if self.rect.colliderect(player_plat1):
            #the game ball is making contact from the top
            if abs(self.rect.bottom - player_plat1.rect.top) < collision_thresh and self.speed_y > 0:
                self.speed_y *= -1
                self.speed_x += player_plat1.direction
                if self.speed_x > self.speed_max:
                    self.speed_x = self.speed_max
                elif self.speed_x < 0 and self.speed_x < -self.speed_max:
                    self.speed_x = -self.speed_max
            else:
                self.speed_x *= -1

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.game_over


    def draw(self):
        pygame.draw.circle(screen, plat1_col, (self.rect.x + self.gb_rad, self.rect.y + self.gb_rad), self.gb_rad)
        pygame.draw.circle(screen, plat1_outline, (self.rect.x + self.gb_rad, self.rect.y + self.gb_rad), self.gb_rad, 3)



    def reset(self, x, y):
        self.gb_rad = 10
        self.x = x - self.gb_rad
        self.y = y
        self.rect = Rect(self.x, self.y, self.gb_rad * 2, self.gb_rad * 2)
        self.speed_x = 10
        self.speed_y = -4
        self.speed_max = 5
        self.game_over = 0



#platform is created
player_plat1 = plat1()



#adding background image
#background image from files
#bgImg = pygame.image.load('heavencity.png')


#gameball is created
gb = game_gb(player_plat1.x + (player_plat1.width // 2), player_plat1.y - player_plat1.height)

run = True
while run:

    clock.tick(fps)
    
    screen.fill(PURPLE)

    #draw all objects

    player_plat1.draw()
    gb.draw()

    if live_gb:
        #draw plat1
        player_plat1.move()
        #draw ball
        game_over = gb.move()
        if game_over != 0:
            live_gb = False


    #print player instructions
    if not live_gb:
        if game_over == 0:
            draw_text('CLICK ANYWHERE TO START', font, text_col, 100, screen_height // 2 + 100)
        elif game_over == 1:
            draw_text('YOU WON!', font, text_col, 240, screen_height // 2 + 50)
            draw_text('CLICK ANYWHERE TO START', font, text_col, 100, screen_height // 2 + 100)
        elif game_over == -1:
            draw_text('YOU LOST!', font, text_col, 240, screen_height // 2 + 50)
            draw_text('CLICK ANYWHERE TO START', font, text_col, 100, screen_height // 2 + 100)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and live_gb == False:
            live_ball = True
            gb.reset(player_plat1.x + (player_plat1.width // 2), player_plat1.y - player_plat1.height)
            player_plat1.reset()




    pygame.display.update()

pygame.quit()