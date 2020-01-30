import random
import time
import pygame

from graphic.Game import Game


pygame.init()
pygame.display.set_caption("Snake")
random.seed(time.time())
game = Game(1080, 720)
game.play()
pygame.quit()

"""import pygame
import time


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# init game
pygame.init()
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((1080, 720))

running = True
head = pygame.Rect(0, 0, 50, 50)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, head)
    pygame.display.update()

pygame.quit()
"""