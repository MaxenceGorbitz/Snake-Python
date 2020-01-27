from math import *
import numpy as np
import random
import time

from Snake import Snake

class Game:
    def __init__(self, heigth, width):
        self._snake = Snake(width / 2, heigth / 2)
        self._heigth = heigth
        self._width = width
        self._is_apple = False
        self._board = np.chararray(heigth * width).reshape(heigth, width)
        self.init_board()

    def init_board(self):
        self._board[:] = '.'
        self._board[floor(self._heigth / 2)][floor(self._width / 2)] = 's'


    def play(self):
        #self.enter_key()
        while not self.is_lost():
            if not self._is_apple:
                self.create_appel()
            print(self.__repr__())
            self.move()
            time.sleep(0.4)

    """def enter_key(self):
        while True:
            time.sleep(1)
            print('test')"""

    def move(self):
        key = input()
        if key == 'z':
            print('up')
        elif key == 'q':
            print('left')
        elif key == 's':
            print('down')
        elif key == 'd':
            print('right')
        else:
            print('key not valid')

    def is_lost(self):
        return False

    def create_appel(self):
        x = random.randint(0, self._width - 1)
        y = random.randint(0, self._heigth - 1)
        self._board[x][y] = 'a'
        self._is_apple = True

    def __repr__(self):
        s = ''
        for r in self._board:
            row = ''
            for c in r:
                row = row + c.decode() + " "
            s = s + row + '\n'
        return s

