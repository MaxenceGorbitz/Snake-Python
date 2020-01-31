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
GREY = (200, 200, 200)


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

        # game
        self._game = GameServer()

        # socket
        self._socket = ClientSocket()

        # other
        self._running = True
        self._my_direction = "not_set"

    def play(self):
        # create connection
        self._socket.connect()

        while self._running:

            self.manage_event()

            # ask to the server for receive game data
            # if the client has lost : this method return None
            self._game = self._socket.send_direction_and_get_data(self._my_direction)

            if self._game is None:
                self._running = False
                break

            self.draw_screen()

            # update display
            pygame.display.flip()
            time.sleep(0.05)

    def manage_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self._my_direction = Direction.UP.value
                elif event.key == pygame.K_a:
                    self._my_direction = Direction.LEFT.value
                elif event.key == pygame.K_s:
                    self._my_direction = Direction.DOWN.value
                elif event.key == pygame.K_d:
                    self._my_direction = Direction.RIGHT.value

    def draw_screen(self):
        # background
        self._screen.blit(self._background, (0, 0))

        # draw apple
        rect_apple = self._apple_image.get_rect()
        rect_apple.x = self._game.apple.get_coordinate()[0] * ConstantVariables.TILE_WIDTH
        rect_apple.y = self._game.apple.get_coordinate()[1] * ConstantVariables.TILE_WIDTH
        self._screen.blit(self._apple_image, rect_apple)

        # draw snakes
        for snake in self._game.snakes:
            # head
            head_coordinate = snake.get_head_coordinate()
            rect = pygame.Rect(head_coordinate[0] * self._tile_width, head_coordinate[1] * self._tile_width,
                               self._tile_width, self._tile_width)
            if snake.id_client == self._socket.id:
                pygame.draw.rect(self._screen, GREEN, rect)
            else:
                pygame.draw.rect(self._screen, RED, rect)
            # body
            for part in snake.body_coordinates:
                rect = pygame.Rect(part[0] * self._tile_width, part[1] * self._tile_width, self._tile_width,
                                   self._tile_width)
                pygame.draw.rect(self._screen, GREY, rect)
