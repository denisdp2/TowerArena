import pygame as pg
import sys
from load_image import load_image
from variables import *


def start_screen():
    global cursor_pos
    fon = pg.transform.scale(load_image('MainMenu.png'), size)
    screen.blit(fon, (0, 0))
    image = load_image("TA.png")
    image1 = pg.transform.scale(image, (300, 150))
    start_image = load_image("StartGame.png")
    start_image1 = pg.transform.scale(start_image, (120, 40))
    pg.mouse.set_visible(False)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEMOTION:
                cursor_pos = event.pos
            screen.blit(fon, (0, 0))
            screen.blit(image1, (size[0] // 2 - 150, 10))
            screen.blit(start_image1, (size[0] // 2 - 60, size[1] // 2 + 50))
            if pg.mouse.get_focused():
                screen.blit(cursor_image, cursor_pos)
            if event.type == pg.MOUSEBUTTONDOWN and (event.pos[0] in range(size[0] // 2 - 60, size[0] // 2 + 60) and
                                                     event.pos[1] in range(size[1] // 2 + 50, size[1] // 2 + 100)):
                return
        pg.display.flip()
        clock.tick(FPS)
