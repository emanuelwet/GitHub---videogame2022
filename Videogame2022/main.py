#pong game 
#need two sides that can bounce a ball either vertically or horizontally

#import libraries and modules
#from platform import platform
import turtle



#game settings 
WIDTH = 850
HEIGHT = 800
FPS = 30

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128, 255)

#create background screen (bg)
bg = turtle.Screen()
bg.title("Manny's Pong Game")
bg.bgcolor(WHITE)
bg.setup(WIDTH, HEIGHT)
