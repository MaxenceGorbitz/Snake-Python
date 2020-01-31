import numpy as np

from console.Snake import Snake
from console.Apple import Apple


class Game:
    def __init__(self, window_width, window_height):
        self._snake = Snake(window_width, window_height)
        self._height = window_height
        self._width = window_width
        self._apple = Apple(self._width - 1, self._height - 1)
        self._board = np.chararray(window_height * window_width).reshape(window_height, window_width)

    def reset_board(self):
        self._board[:] = '.'

    def play(self):
        self.create_new_apple()
        while not self.has_lost():
            self.reset_board()
            print(self.draw_board())
            self.move_snake_head()
            if self.is_catching_the_apple():
                self._snake.growth()
                self.create_new_apple()
            else:
                self._snake.move_body()
        print('GAME OVER')

    def move_snake_head(self):
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
            print('key not valid')

    def is_catching_the_apple(self):
        return self._apple.x == self._snake.head_x and self._apple.y == self._snake.head_y

    def has_lost(self):
        return self._snake.has_lost()

    def create_new_apple(self):
        apple_coord = self._apple.get_coordinate()
        while apple_coord in self._snake.body_coordinates or apple_coord == self._snake.get_head_coordinate():
            self._apple.new_coordinates(self._width - 1, self._height - 1)
            apple_coord = self._apple.get_coordinate()

    def draw_board(self):
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
            self._board[c[1]][c[0]] = "b"
