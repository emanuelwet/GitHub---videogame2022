# EMANUEL WETSCHNIG


##### SOURCES #####
# help + basecode from https://www.youtube.com/watch?v=NIfkaOF3Hjs&list=PLjcN1EyupaQlbAyHLsuFIp0n6i_p8XWaO&ab_channel=CodingWithRuss    
# content from kids can code: http://kidscancode.org/blog/
# help from geeks for geeks: https://www.geeksforgeeks.org/
# help from https://www.youtube.com/watch?v=C6jJg9Zan7w&ab_channel=freeCodeCamp.org       
   
 


import pygame
from pygame.locals import *

pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Breakout')

#define font
font = pygame.font.SysFont('Constantia', 30)

#define colours
bg = (234, 218, 184)
#block colours
block_red = (242, 85, 96)
block_green = (86, 174, 87)
block_blue = (69, 177, 232)
#plat1 colours
plat_col = (142, 135, 123)
plat_outline = (100, 100, 100)
#text colour
text_col = (78, 81, 139)



#define game variables
cols = 6
rows = 6
clock = pygame.time.Clock()
fps = 60
live_ball = False
game_over = 0


#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))








#plat1 class
class plat1():
    def __init__(self):
        self.reset()


    def move(self):
        #reset movement direction
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1
        if key[pygame.K_d] and self.rect.right < screen_width:
            self.rect.x += self.speed
            self.direction = 1

    def draw(self):
        pygame.draw.rect(screen, plat_col, self.rect)
        pygame.draw.rect(screen, plat_outline, self.rect, 3)


    def reset(self):
        #define plat1 variables
        self.height = 20
        self.width = int(screen_width / cols)
        self.x = int((screen_width / 2) - (self.width / 2))
        self.y = screen_height - (self.height * 2)
        self.speed = 10
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0


#ball class
class game_ball():
    def __init__(self, x, y):
        self.reset(x, y)


    def move(self):

        #collision threshold
        collision_thresh = 5


        #check for collision with walls
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1

        #check for collision with top and bottom of the screen
        if self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.bottom > screen_height:
            self.game_over = -1


        #look for collission with plat1
        if self.rect.colliderect(player_plat1):
            #check if colliding from the top
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
        pygame.draw.circle(screen, plat_col, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)
        pygame.draw.circle(screen, plat_outline, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad, 3)



    def reset(self, x, y):
        self.ball_rad = 10
        self.x = x - self.ball_rad
        self.y = y
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = 4
        self.speed_y = -4
        self.speed_max = 5
        self.game_over = 0





#create plat1
player_plat1 = plat1()


#create ball
ball = game_ball(player_plat1.x + (player_plat1.width // 2), player_plat1.y - player_plat1.height)

run = True
while run:

    clock.tick(fps)
    
    screen.fill(bg)

    #draw all objects

    player_plat1.draw()
    ball.draw()

    if live_ball:
        #draw plat1
        player_plat1.move()
        #draw ball
        game_over = ball.move()
        if game_over != 0:
            live_ball = False


    #print player instructions
    if not live_ball:
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
        if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False:
            live_ball = True
            ball.reset(player_plat1.x + (player_plat1.width // 2), player_plat1.y - player_plat1.height)
            player_plat1.reset()




    pygame.display.update()

pygame.quit()