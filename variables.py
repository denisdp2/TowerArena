import pygame as pg
from load_image import load_image

first_lvl_sprites = pg.sprite.Group()
characters_sprites = pg.sprite.Group()
FPS = 30
WIDTH, HEIGHT = 1080, 720
size = WIDTH, HEIGHT
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
cursor_pos = (0, 0)
cursor_image = load_image('Cursor.png')
