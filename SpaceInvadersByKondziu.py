# !/usr/bin/env python
from pygame import *
import sys
from random import shuffle, randrange, choice

#           R    G    B
WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)

SCREEN = display.set_mode((800, 600))
FONT = "fonts/space_invaders.ttf"
IMG_NAMES = ["ship", "ship", "mystery", "enemy1_1", "enemy1_2", "enemy2_1", "enemy2_2",
             "enemy3_1", "enemy3_2", "explosionblue", "explosiongreen", "explosionpurple", "laser", "enemylaser"]
IMAGES = {name: image.load("images/{}.png".format(name)).convert_alpha()
          for name in IMG_NAMES}

class SpaceInvaders(object):
    def __init__(self):
        mixer.pre_init(44100, -16, 1, 512)
        init()
        self.caption = display.set_caption('Space Invaders by Kondziu')
        self.screen = SCREEN
        self.background = image.load('images/background.jpg').convert()
        self.startGame = False
        self.mainScreen = True
        self.gameOver = False
        self.enemyposition = 65

def create_text(self):
    self.titleText = Text(FONT, 50, "Space Invaders", WHITE, 164, 155)
    self.titleText2 = Text(FONT, 25, "Wcisnij dowolny klawisz", WHITE, 201, 225)
    self.gameOverText = Text(FONT, 50, "Koniec Gry", WHITE, 250, 270)
    self.nextRoundText = Text(FONT, 50, "Nastepna runda", WHITE, 240, 270)
    self.enemy1Text = Text(FONT, 25, "   =   10 punktow", GREEN, 368, 270)
    self.enemy2Text = Text(FONT, 25, "   =  20 punktow", BLUE, 368, 320)
    self.enemy3Text = Text(FONT, 25, "   =  30 punktow", PURPLE, 368, 370)
    self.enemy4Text = Text(FONT, 25, "   =  ?????", RED, 368, 420)
    self.scoreText = Text(FONT, 20, "PTK", WHITE, 5, 5)
    self.livesText = Text(FONT, 20, "Zycia ", WHITE, 640, 5)