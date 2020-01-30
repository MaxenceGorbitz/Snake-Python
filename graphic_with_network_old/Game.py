import numpy as np
from math import *
import time

import graphic_with_network_old.ConstantVariables
from graphic_with_network_old.ConstantVariables import ConstantVariables
from graphic_with_network_old.Snake import Snake
from graphic_with_network_old.Snake import Direction
from graphic_with_network_old.Apple import Apple

# images
# image_apple = pygame.image.load('assets/apple.png')


class Game:
    def __init__(self):
        # tiles and pixels
        self._nb_tile_x = ConstantVariables.NB_COLUMN
        self._nb_tile_y = ConstantVariables.NB_ROW

        # elements
        # objects
        self._snakes = []
        self._apple = Apple(self._nb_tile_x - 1, self._nb_tile_y - 1)

        # other
        self._running = True

    @property
    def apple(self):
        return self._apple

    def add_snake(self, id_client):
        self._snakes.append(Snake(id_client, self._nb_tile_x, self._nb_tile_y))

    # move snakes
    def move_snakes(self):
        for snake in self._snakes:
            snake.move_head()
    """def play(self):
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
            time.sleep(0.05)"""

    # change direction
    def change_direction(self, id_client, direction):
        for snake in self._snakes:
            if snake.id_client == id_client:
                snake.direction_current = direction
                break

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

    def apple_catching(self):
        for snake in self._snakes:
            if self._apple.x == snake.head_x and self._apple.y == snake.head_y:
                return True
        return False

    """def has_lost(self):
        return self._snake.has_lost()"""

    def create_new_apple(self):
        apple_coord = self._apple.get_coordinate()
        all_coord_snake = []
        for snake in self._snakes:
            all_coord_snake.append(snake.get_head_coordinate())
            all_coord_snake.append(snake.body_coordinates)
        while apple_coord in all_coord_snake:
            self._apple.set_new_coordinates(self._nb_tile_x - 1, self._nb_tile_y - 1)
            apple_coord = self._apple.get_coordinate()

    """def draw_screen(self):
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
            rect = pygame.Rect(part[0] * self._tile_width, part[1] * self._tile_width, self._tile_width,
                               self._tile_width)
            pygame.draw.rect(self._screen, RED, rect)"""
