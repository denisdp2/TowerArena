import pygame as pg
from load_image import load_image


class HealingSalve(pg.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)

        self.image = load_image("healing_salve.png")
        tile_width, tile_height = 128, 128
        self.rect = self.image.get_rect().move(x * tile_width, y * tile_height)
