from math import *
import time

from ConstantVariables import ConstantVariables
from Snake import Snake
from Snake import Direction
from Apple import Apple


class GameServer:
    def __init__(self):
        # tiles and pixels
        self._nb_tile_x = ConstantVariables.NB_COLUMN
        self._nb_tile_y = ConstantVariables.NB_ROW

        # elements
        self._snakes = []
        self._apple = Apple(self._nb_tile_x - 1, self._nb_tile_y - 1)

        # other
        self._running = True

    @property
    def snakes(self):
        return self._snakes

    @property
    def apple(self):
        return self._apple

    def create_snake(self, id_client):
        coordinate_not_free = []
        for snake in self._snakes:
            coordinate_not_free.append(snake.get_head_coordinate())
            for part_snake in snake.body_coordinates:
                coordinate_not_free.append(part_snake)
        coordinate_not_free.append(self.apple.get_coordinate())
        self._snakes.append(Snake(id_client, self._nb_tile_x, self._nb_tile_y, coordinate_not_free))

    def start(self):
        self.create_new_apple()

    def is_apple_caught(self, snake):
        return self._apple.x == snake.head_x and self._apple.y == snake.head_y

    def create_new_apple(self):
        apple_coord = self._apple.get_coordinate()
        all_coord_snake = []
        for snake in self._snakes:
            all_coord_snake.append(snake.get_head_coordinate())
            all_coord_snake.append(snake.body_coordinates)
        while apple_coord in all_coord_snake:
            self._apple.set_new_coordinates(self._nb_tile_x - 1, self._nb_tile_y - 1)
            apple_coord = self._apple.get_coordinate()
