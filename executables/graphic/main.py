import random
import time
import pygame

from Game import Game


pygame.init()
pygame.display.set_caption("Snake")
random.seed(time.time())
game = Game(1080, 720)
game.play()
pygame.quit()