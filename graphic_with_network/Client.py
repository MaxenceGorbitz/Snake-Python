import numpy as np
from math import *
import random
import time
import pygame
import pickle

import graphic_with_network.ConstantVariables
from graphic_with_network.ConstantVariables import ConstantVariables
from graphic_with_network.Network import Network
from graphic_with_network.Game import Game
from graphic_with_network.Snake import Snake
from graphic_with_network.Snake import Direction
from graphic_with_network.Apple import Apple


# init pygame
pygame.init()
pygame.display.set_caption("Snake")

# init random
random.seed(time.time())

# init Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# init images
# image_apple = pygame.image.load('assets/apple.png')


class Client:
    def __init__(self):
        # tiles and pixels
        self._tile_width = ConstantVariables.TILE_WIDTH
        self._nb_tile_x = ConstantVariables.NB_COLUMN
        self._nb_tile_y = ConstantVariables.NB_ROW
        self._width_px = ConstantVariables.WINDOW_WIDTH
        self._height_px = ConstantVariables.WINDOW_HEIGHT

        # elements
        # screen
        self._screen = pygame.display.set_mode((self._width_px, self._height_px))
        self._background = pygame.image.load('../assets/grass.jpg')
        self._background = pygame.transform.scale(self._background, (self._width_px, self._height_px))

        # objects
        # self._snake = Snake(self._nb_tile_x, self._nb_tile_y, self._tile_width)
        # self._apple = Apple(self._nb_tile_x - 1, self._nb_tile_y - 1, self._tile_width)

        # other
        self._running = True

    def main(self):
        run = True
        n = Network()
        player_id = int(n.p)
        print("You are player: ", player_id)

        while run:
            try:
                game = n.send(ConstantVariables.NETWORK_GET)
            except:
                run = False
                print("Couldn't get game")
                break

            self.draw_screen(game)
            """self.manage_event()
            self._snake.move()
            self.draw_screen()
            if self.is_catching_the_apple():
                self.create_new_apple()
                self._snake.growth()
            else:
                self._snake.move_body()
            pygame.display.flip()
            time.sleep(0.05)"""

    # TODO
    """def manage_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self._snake.direction_current = Direction.UP
                elif event.key == pygame.K_a:
                    self._snake.direction_current = Direction.LEFT
                elif event.key == pygame.K_s:
                    self._snake.direction_current = Direction.DOWN
                elif event.key == pygame.K_d:
                    self._snake.direction_current = Direction.RIGHT"""

    """def is_catching_the_apple(self):
        return self._apple.x == self._snake.head_x and self._apple.y == self._snake.head_y"""

    """def has_lost(self):
        return self._snake.has_lost()"""

    def draw_screen(self, game):
        self._screen.blit(self._background, (0, 0))

        # draw apple
        self._screen.blit(game.apple.image, game.apple.rect_i)

        # draw snake
        # head
        """head_coordinate = self._snake.get_head_coordinate()
        rect = pygame.Rect(head_coordinate[0] * self._tile_width, head_coordinate[1] * self._tile_width,
                           self._tile_width, self._tile_width)
        pygame.draw.rect(self._screen, GREEN, rect)"""
        # body
        """for part in self._snake.body_coordinates:
            rect = pygame.Rect(part[0] * self._tile_width, part[1] * self._tile_width, self._tile_width,
                               self._tile_width)
            pygame.draw.rect(self._screen, RED, rect)"""


client = Client()
client.main()