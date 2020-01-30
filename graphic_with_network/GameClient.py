import numpy as np
from math import *
import time
import pygame

from graphic_with_network.Snake import Direction
from graphic_with_network.GameServer import GameServer
from graphic_with_network.ClientSocket import ClientSocket
from graphic_with_network.ConstantVariables import ConstantVariables


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class GameClient:
    def __init__(self):
        # tiles and pixels
        self._tile_width = ConstantVariables.TILE_WIDTH
        self._nb_tile_x = ConstantVariables.NB_COLUMN
        self._nb_tile_y = ConstantVariables.NB_ROW
        self._width_px = ConstantVariables.WINDOW_WIDTH
        self._height_px = ConstantVariables.WINDOW_HEIGHT

        # elements
        # screen - textures
        self._screen = pygame.display.set_mode((self._width_px, self._height_px))
        self._background = pygame.image.load('../assets/grass.jpg')
        self._background = pygame.transform.scale(self._background, (self._width_px, self._height_px))
        self._apple_image = pygame.image.load('../assets/apple.png')
        self._apple_image = pygame.transform.scale(self._apple_image, (self._tile_width, self._tile_width))
        # objects
        self._game = GameServer()

        # socket
        self._socket = ClientSocket()

        # other
        self._running = True
        self._my_direction = ""

    def play(self):
        self._socket.connect()
        # self.create_my_snake()
        while not self.has_lost() and self._running:
            self.manage_event()
            # self._socket.send_a_message()
            self._game = self._socket.send_and_get_data(self._my_direction)

            self.draw_screen()

            pygame.display.flip()
            time.sleep(0.05)

    def manage_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self._my_direction = Direction.UP
                elif event.key == pygame.K_a:
                    self._my_direction = Direction.LEFT
                elif event.key == pygame.K_s:
                    self._my_direction = Direction.DOWN
                elif event.key == pygame.K_d:
                    self._my_direction = Direction.RIGHT

    # TODO
    def has_lost(self):
        return False

    def draw_screen(self):
        # background
        self._screen.blit(self._background, (0, 0))

        # draw apple
        rect_apple = self._apple_image.get_rect()
        rect_apple.x = self._game.apple.get_coordinate()[0] * ConstantVariables.TILE_WIDTH
        rect_apple.y = self._game.apple.get_coordinate()[1] * ConstantVariables.TILE_WIDTH
        self._screen.blit(self._apple_image, rect_apple)

        # draw snake
        for snake in self._game.snakes:
            # head
            head_coordinate = snake.get_head_coordinate()
            rect = pygame.Rect(head_coordinate[0] * self._tile_width, head_coordinate[1] * self._tile_width,
                               self._tile_width, self._tile_width)
            pygame.draw.rect(self._screen, GREEN, rect)
            # body
            for part in snake.body_coordinates:
                rect = pygame.Rect(part[0] * self._tile_width, part[1] * self._tile_width, self._tile_width,
                                   self._tile_width)
                pygame.draw.rect(self._screen, RED, rect)

    # TODO
    def create_my_snake(self):
        pass
