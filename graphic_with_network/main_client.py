import random
import time
import pygame

from graphic_with_network.GameClient import GameClient


pygame.init()
pygame.display.set_caption("Snake")
random.seed(time.time())
game = GameClient()
game.play()
pygame.quit()
