from math import *
from enum import Enum


class Direction(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class Snake:
    def __init__(self, nb_tile_x, nb_tile_y, tile_width):
        self._length = 1
        self._window_width_tile = nb_tile_x
        self._window_height_tile = nb_tile_y
        self._head_x = floor(nb_tile_x / 2)
        self._head_y = floor(nb_tile_y / 2)
        # the first element is the last part of the queue
        # the last element is the first part of the queue
        self._body_coordinates = []
        self._head_coordinate_before_move = []
        self._direction_current = ""
        self._direction_forbidden = ""

    @property
    def head_x(self):
        return self._head_x

    @property
    def head_y(self):
        return self._head_y

    def get_head_coordinate(self):
        return [self._head_x, self._head_y]

    @property
    def body_coordinates(self):
        return self._body_coordinates

    @property
    def direction_current(self):
        return self._direction_current

    @direction_current.setter
    def direction_current(self, value):
        if value in Direction:
            self._direction_current = value

    def growth(self):
        self._length += 1
        self._body_coordinates.append(self._head_coordinate_before_move)

    def move_head(self):
        if self.direction_current == Direction.UP:
            self.move_up()
        elif self.direction_current == Direction.DOWN:
            self.move_down()
        elif self.direction_current == Direction.LEFT:
            self.move_left()
        elif self.direction_current == Direction.RIGHT:
            self.move_right()

    def move_body(self):
        if len(self._body_coordinates) > 0:
            # remove the first element (the last part)
            self._body_coordinates.pop(0)
            # add the new part
            self._body_coordinates.append(self._head_coordinate_before_move)

    def set_head_coordinate_before_move(self):
        self._head_coordinate_before_move = [self._head_x, self._head_y]

    def move_up(self):
        if self._direction_forbidden != Direction.UP:
            self.set_head_coordinate_before_move()
            self._head_y -= 1
            if self._head_y < 0:
                self._head_y = self._window_height_tile - 1
            self._direction_forbidden = Direction.DOWN
        else:
            self.move_down()

    def move_down(self):
        if self._direction_forbidden != Direction.DOWN:
            self.set_head_coordinate_before_move()
            self._head_y += 1
            if self._head_y >= self._window_height_tile:
                self._head_y = 0
            self._direction_forbidden = Direction.UP
        else:
            self.move_up()

    def move_left(self):
        if self._direction_forbidden != Direction.LEFT:
            self.set_head_coordinate_before_move()
            self._head_x -= 1
            if self._head_x < 0:
                self._head_x = self._window_width_tile - 1
            self._direction_forbidden = Direction.RIGHT
        else:
            self.move_right()

    def move_right(self):
        if self._direction_forbidden != Direction.RIGHT:
            self.set_head_coordinate_before_move()
            self._head_x += 1
            if self._head_x >= self._window_width_tile:
                self._head_x = 0
            self._direction_forbidden = Direction.LEFT
        else:
            self.move_left()

    def has_lost(self):
        return [self._head_x, self._head_y] in self._body_coordinates
