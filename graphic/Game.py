import numpy as np
from math import *
import time
import pygame

from graphic.Snake import Snake
from graphic.Snake import Direction
from graphic.Apple import Apple

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# images
# image_apple = pygame.image.load('assets/apple.png')


class Game:
    def __init__(self, window_width, window_height):
        # tiles and pixels
        self._nb_tile_x = 60
        self._tile_width = floor(window_width / self._nb_tile_x)
        self._width_px = self._tile_width * self._nb_tile_x
        self._nb_tile_y = floor(window_height / self._tile_width)
        self._height_px = self._tile_width * self._nb_tile_y

        # elements
        # screen
        self._screen = pygame.display.set_mode((self._width_px, self._height_px))
        self._background = pygame.image.load('assets/grass.jpg')
        self._background = pygame.transform.scale(self._background, (self._width_px, self._height_px))
        # objects
        self._snake = Snake(self._nb_tile_x, self._nb_tile_y, self._tile_width)
        self._apple = Apple(self._nb_tile_x - 1, self._nb_tile_y - 1, self._tile_width)

        # other
        self._running = True

    def play(self):
        self.create_new_apple()
        while not self.has_lost() and self._running:

            self.manage_event()
            self._snake.move()
            self.draw_screen()
            if self.is_catching_the_apple():
                self.create_new_apple()
                self._snake.growth()
            else:
                self._snake.move_body()
            pygame.display.flip()
            time.sleep(0.05)

    def manage_event(self):
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
                    self._snake.direction_current = Direction.RIGHT

    """def move_snake_head(self):
        key = input()
        if key == 'z':
            self._snake.move_up()
        elif key == 'q':
            self._snake.move_left()
        elif key == 's':
            self._snake.move_down()
        elif key == 'd':
            self._snake.move_right()
        else:
            print('key not valid')"""

    def is_catching_the_apple(self):
        return self._apple.x == self._snake.head_x and self._apple.y == self._snake.head_y

    def has_lost(self):
        return self._snake.has_lost()

    def create_new_apple(self):
        apple_coord = self._apple.get_coordinate()
        while apple_coord in self._snake.body_coordinates or apple_coord == self._snake.get_head_coordinate():
            self._apple.set_new_coordinates(self._nb_tile_x - 1, self._nb_tile_y - 1)
            apple_coord = self._apple.get_coordinate()

    def draw_screen(self):
        self._screen.blit(self._background, (0, 0))

        # draw apple
        # pygame.draw.rect(self._screen, RED, self._apple.rect)

        self._screen.blit(self._apple.image, self._apple.rect_i)

        # self._screen.blit(image_apple, (100, -100))

        # draw snake
        # head
        head_coordinate = self._snake.get_head_coordinate()
        rect = pygame.Rect(head_coordinate[0] * self._tile_width, head_coordinate[1] * self._tile_width,
                           self._tile_width, self._tile_width)
        pygame.draw.rect(self._screen, GREEN, rect)
        # body
        for part in self._snake.body_coordinates:
            rect = pygame.Rect(part[0] * self._tile_width, part[1] * self._tile_width, self._tile_width, self._tile_width)
            pygame.draw.rect(self._screen, RED, rect)
