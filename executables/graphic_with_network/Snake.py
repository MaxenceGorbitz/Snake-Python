import random
from enum import Enum

from ConstantVariables import ConstantVariables


class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class Snake:
    def __init__(self, id_client, nb_tile_x, nb_tile_y, coordinate_not_free):
        self._length = 1
        self._id_client = id_client
        self._nb_tile_x = ConstantVariables.NB_COLUMN
        self._nb_tile_y = ConstantVariables.NB_ROW
        self.create_head(nb_tile_x, nb_tile_y, coordinate_not_free)
        # the first element is the last part of the queue
        # the last element is the first part of the queue
        self._body_coordinates = []
        self._head_coordinate_before_move = []
        self._direction_current = ""
        self._direction_forbidden = ""

    def create_head(self, max_x, max_y, coordinate_not_free):
        self._head_x = random.randint(0, max_x)
        self._head_y = random.randint(0, max_y)
        while self.get_head_coordinate() in coordinate_not_free:
            self._head_x = random.randint(0, max_x)
            self._head_y = random.randint(0, max_y)

    @property
    def id_client(self):
        return self._id_client

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
        if value in [Direction.UP.value, Direction.DOWN.value, Direction.LEFT.value, Direction.RIGHT.value]:
            self._direction_current = value

    def growth(self):
        self._length += 1
        self._body_coordinates.append(self._head_coordinate_before_move)

    def move_head(self):
        if self.direction_current == Direction.UP.value:
            self.move_up()
        elif self.direction_current == Direction.DOWN.value:
            self.move_down()
        elif self.direction_current == Direction.LEFT.value:
            self.move_left()
        elif self.direction_current == Direction.RIGHT.value:
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
        if self._direction_forbidden != Direction.UP.value:
            self.set_head_coordinate_before_move()
            self._head_y -= 1
            if self._head_y < 0:
                self._head_y = self._nb_tile_y - 1
            self._direction_forbidden = Direction.DOWN.value
        else:
            self.move_down()

    def move_down(self):
        if self._direction_forbidden != Direction.DOWN.value:
            self.set_head_coordinate_before_move()
            self._head_y += 1
            if self._head_y >= self._nb_tile_y:
                self._head_y = 0
            self._direction_forbidden = Direction.UP.value
        else:
            self.move_up()

    def move_left(self):
        if self._direction_forbidden != Direction.LEFT.value:
            self.set_head_coordinate_before_move()
            self._head_x -= 1
            if self._head_x < 0:
                self._head_x = self._nb_tile_x - 1
            self._direction_forbidden = Direction.RIGHT.value
        else:
            self.move_right()

    def move_right(self):
        if self._direction_forbidden != Direction.RIGHT.value:
            self.set_head_coordinate_before_move()
            self._head_x += 1
            if self._head_x >= self._nb_tile_x:
                self._head_x = 0
            self._direction_forbidden = Direction.LEFT.value
        else:
            self.move_left()
