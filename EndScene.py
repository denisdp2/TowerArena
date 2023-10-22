import pygame as pg
import sys
from load_image import load_image
from variables import *


def start_screen():
    global cursor_pos
    fon = pg.transform.scale(load_image('GrayFon.png'), size)
    screen.blit(fon, (0, 0))
    image = load_image("Creators.png")
    image1 = pg.transform.scale(image, (1080, 600))
    pg.mouse.set_visible(False)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEMOTION:
                cursor_pos = event.pos
            screen.blit(fon, (0, 0))
            screen.blit(image1, (0, 120))
            if pg.mouse.get_focused():
                screen.blit(cursor_image, cursor_pos)
        pg.display.flip()
        clock.tick(FPS)
