import pygame


# not use for the moment
class TileRectangle:
    def __init__(self, tile_width, nb_tile_on_x, nb_tile_on_y, x_tile, y_tile):
        self._tile_width = tile_width
        self._nb_tile_on_x = nb_tile_on_x
        self._nb_tile_on_y = nb_tile_on_y
        self._x_tile = x_tile
        self._y_tile = y_tile
        self._x_px = x_tile * tile_width
        self._y_px = y_tile * tile_width
        self._rect = pygame.Rect(self._x_px, self._y_px, self._tile_width, self._tile_width)

