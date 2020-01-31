from math import *
from enum import Enum


class Direction(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class Snake:
    def __init__(self, window_width, window_height):
        self._length = 1
        self._window_width = window_width
        self._window_height = window_height
        self._head_x = floor(window_width / 2)
        self._head_y = floor(window_height / 2)
        # the first element is the last part of the queue
        # the last element is the first part of the queue
        self._body_coordinates = []
        self._head_coordinate_before_move = []
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

    def growth(self):
        self._length += 1
        self._body_coordinates.append(self._head_coordinate_before_move)

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
                self._head_y = self._window_height - 1
            self._direction_forbidden = Direction.DOWN
        else:
            self.move_down()

    def move_down(self):
        if self._direction_forbidden != Direction.DOWN:
            self.set_head_coordinate_before_move()
            self._head_y += 1
            if self._head_y >= self._window_height:
                self._head_y = 0
            self._direction_forbidden = Direction.UP
        else:
            self.move_up()

    def move_left(self):
        if self._direction_forbidden != Direction.LEFT:
            self.set_head_coordinate_before_move()
            self._head_x -= 1
            if self._head_x < 0:
                self._head_x = self._window_width - 1
            self._direction_forbidden = Direction.RIGHT
        else:
            self.move_right()

    def move_right(self):
        if self._direction_forbidden != Direction.RIGHT:
            self.set_head_coordinate_before_move()
            self._head_x += 1
            if self._head_x >= self._window_width:
                self._head_x = 0
            self._direction_forbidden = Direction.LEFT
        else:
            self.move_left()

    def has_lost(self):
        return [self._head_x, self._head_y] in self._body_coordinates
