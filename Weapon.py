import pygame as pg
from load_image import load_image


class Weapon(pg.sprite.Sprite):
    def __init__(self, filename_stand, x, y, damage):
        super().__init__()

        self.image = load_image(filename_stand)
        tile_width, tile_height = 128, 128
        self.rect = self.image.get_rect().move(x * tile_width, y * tile_height)
        self.damage = damage

    def is_taken(self, player):
        player_x, player_y = player.get_coords()
        if abs(self.rect.x - player_x) <= 50 or \
                abs(self.rect.y - player_y) <= 50:
            return True
        else:
            return False

    def update_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
