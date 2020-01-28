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


class Game:
    def __init__(self, window_width, window_height):
        self._snake = Snake(window_width, window_height)
        self._height = window_height
        self._width = window_width
        self._apple = Apple(self._width - 1, self._height - 1)
        self._screen = pygame.display.set_mode((window_width, window_height))
        self._running = True
        # self._board = np.chararray(window_height * window_width).reshape(window_height, window_width)

    def reset_screen(self):
        self._screen.fill(WHITE)

    def play(self):
        self.create_new_apple()
        while not self.has_lost() and self._running:
            self.manage_event()
            self._snake.move()
            self.reset_screen()
            self.draw_screen()
            if self.is_catching_the_apple():
                self.create_new_apple()
                self._snake.growth()
            else:
                self._snake.move_body()
            pygame.display.update()
            time.sleep(0.1)

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
        rect_head = self._snake.rect_head
        rect_apple = self._apple.rect
        return rect_head.colliderect(rect_apple)
        # return self._apple.x == self._snake.head_x and self._apple.y == self._snake.head_y

    def has_lost(self):
        # if else for debug
        if self._snake.has_lost():
            return True
        else:
            return False

    def create_new_apple(self):
        while self._apple.rect.colliderect(self._snake.rect_head):
            self._apple.set_new_coordinates(self._width - 1, self._height - 1)

            """ apple_coord = self._apple.get_coordinate()
             while apple_coord in self._snake.body_coordinates or apple_coord == self._snake.get_head_coordinate():
                 self._apple.new_coordinates(self._width - 1, self._height - 1)
                 apple_coord = self._apple.get_coordinate()"""

    def draw_screen(self):
        # draw snake
        pygame.draw.rect(self._screen, GREEN, self._snake.rect_head)
        # draw apple
        pygame.draw.rect(self._screen, RED, self._apple.rect)

    """def draw_board(self):
        self.draw_snake()
        # draw apple
        self._board[self._apple.y][self._apple.x] = 'a'
        s = ''
        for r in self._board:
            row = ''
            for c in r:
                row = row + c.decode() + " "
            s = s + row + '\n'
        return s

    def draw_snake(self):
        # draw head
        self._board[self._snake.head_y][self._snake.head_x] = 's'
        # draw body
        for c in self._snake.body_coordinates:
            self._board[c[1]][c[0]] = "b"""
