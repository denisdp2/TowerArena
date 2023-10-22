import pygame as pg
from animated_sprite import AnimatedSprite
from TowerArena.load_image import load_image


class BaseCharacter:
    def __init__(self, filename_stand, filename_walk, filename_attack_m, frames_b=None, frames_w=None, frames_a=None):
        self.sprite = AnimatedSprite(filename_stand, frames_b, 1, 50, 50)
        self.sprite.set_moving_sprite(filename_walk, frames_w, 1)
        self.sprite.set_attacking_sprite(filename_attack_m, frames_a, 1)
        self.sprite.rect = self.sprite.image.get_rect()
        self.walking = False
        self.attacking = False
        self.hurting = False

    def get_sprite(self):
        return self.sprite

    def can_walk(self, direction, group):
        if direction == 'N':
            self.sprite.rect.y -= 15
            if pg.sprite.spritecollideany(self.sprite, group):
                self.sprite.rect.y += 15
                return False
            self.sprite.rect.y += 15
            return True
        if direction == 'W':
            self.sprite.rect.x -= 15
            if pg.sprite.spritecollideany(self.sprite, group):
                self.sprite.rect.x += 15
                return False
            self.sprite.rect.x += 15
            return True
        if direction == 'S':
            self.sprite.rect.y += 15
            if pg.sprite.spritecollideany(self.sprite, group):
                self.sprite.rect.y -= 15
                return False
            self.sprite.rect.y -= 15
            return True
        if direction == 'E':
            self.sprite.rect.x += 15
            if pg.sprite.spritecollideany(self.sprite, group):
                self.sprite.rect.x -= 15
                return False
            self.sprite.rect.x -= 15
            return True

    def change_direction(self, direction):
        if direction == 'E':
            self.sprite.direction = True
        if direction == 'W':
            self.sprite.direction = False

    def get_walking(self):
        return self.walking

    def set_walking(self, walking):
        self.walking = walking

    def get_attacking(self):
        return self.attacking

    def set_attacking(self, attacking):
        self.attacking = attacking

    def get_hurting(self):
        return self.hurting

    def set_hurting(self, hurting):
        self.hurting = hurting
