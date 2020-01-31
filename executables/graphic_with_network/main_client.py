import random
import time
import pygame

from GameClient import GameClient


pygame.init()
pygame.display.set_caption("Snake")
random.seed(time.time())
game = GameClient()
game.play()
pygame.quit()
