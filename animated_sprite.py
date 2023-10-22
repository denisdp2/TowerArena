import pygame as pg
from variables import first_lvl_sprites, characters_sprites, FPS
from load_image import load_image


class AnimatedSprite(pg.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(characters_sprites)
        self.frames_breathing = []
        self.frames_walking = []
        self.frames_hitting = []
        self.frames_shooting = []
        self.frames_damaged = []
        self.cut_sheet(load_image(sheet), columns, rows, self.frames_breathing)
        self.cur_frame = 0
        self.image = self.frames_breathing[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.count = 0
        # Направление взгляда персонажа: тру - право, фолс - лево
        self.direction = True

    def set_moving_sprite(self, sheet, columns, rows):
        self.cut_sheet(load_image(sheet), columns, rows, self.frames_walking)

    def set_attacking_sprite(self, sheet, columns, rows):
        self.cut_sheet(load_image(sheet), columns, rows, self.frames_hitting)
        self.cut_sheet(load_image(sheet), columns, rows, self.frames_shooting)

    def set_damaged_sprite(self, sheet, columns, rows):
        self.cut_sheet(load_image(sheet), columns, rows, self.frames_damaged)

    def cut_sheet(self, sheet, columns, rows, frames):
        self.rect = pg.Rect(0, 0, sheet.get_width() // columns,
                            sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                frames.append(sheet.subsurface(pg.Rect(
                    frame_location, self.rect.size)))

    def update_breath(self):
        self.count += 1
        if self.count % 6 == 0:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames_breathing)
            if self.direction:
                self.image = self.frames_breathing[self.cur_frame]
            else:
                invert_image = pg.transform.flip(self.frames_breathing[self.cur_frame], True, False)
                self.image = invert_image
            self.count = 0

    def update_move(self):
        self.count += 1
        if self.count % 3 == 0:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames_walking)
            if self.direction:
                self.image = self.frames_walking[self.cur_frame]
            else:
                invert_image = pg.transform.flip(self.frames_walking[self.cur_frame], True, False)
                self.image = invert_image
            self.count = 0

    def update_hit(self):
        self.count += 1
        if self.count % 2 == 0:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames_hitting)
            if self.direction:
                self.image = self.frames_hitting[self.cur_frame]
            else:
                invert_image = pg.transform.flip(self.frames_hitting[self.cur_frame], True, False)
                self.image = invert_image

    def update_damaged(self):
        if self.count % 2 == 0:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames_damaged)
            if self.direction:
                self.image = self.frames_damaged[self.cur_frame]
            else:
                invert_image = pg.transform.flip(self.frames_damaged[self.cur_frame], True, False)
                self.image = invert_image
