import pygame as pg

from TowerArena.load_image import load_image


class Tile(pg.sprite.Sprite):
    def __init__(self, low_group, main_group, tile_type, pos_x, pos_y):
        super().__init__(low_group, main_group)

        tile_images = {
            "floor": load_image("Пол.png"),
            "wall_up": load_image("Верхняя_стена.png"),
            "wall_down": load_image("Нижняя_стена.png"),
            "wall_left": load_image("Левая_стена.png"),
            "wall_right": load_image("Правая_стена.png"),
            "corner_left-up": load_image("Угол_верх-лево.png"),
            "corner_left-down": load_image("Угол_низ-лево.png"),
            "corner_right-up": load_image("Угол_верх-право.png"),
            "corner_right-down": load_image("Угол_низ-право.png"),
            "vertical_wall": load_image("Продолжение_вертикальной_стены.png"),
            "street": load_image("улица_с_травой_верх.png"),
            "street2": load_image("Улица2.png"),
            "vertical_wall_end": load_image("Конец_вертикальной_стены.png")
        }

        tile_width, tile_height = 128, 128

        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
