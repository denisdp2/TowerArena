import pygame as pg

from BaseCharacter import BaseCharacter
from animated_sprite import AnimatedSprite


class Bullet:
    def __init__(self, x, y):
        self.sprite = AnimatedSprite("FireAttackSpriteSheet.png", 2, 1, x, y)
        self.sprite.rect = self.sprite.image.get_rect()
        self.x = x
        self.y = y
        self.sprite.rect.y = self.y
        self.sprite.rect.x = self.x

    def get_sprite(self):
        return self.sprite

    def set_player_coords(self, player):
        self.character_x, self.character_y = player.get_coords()

    def attack_target(self, player):
        self.sprite.rect.x = self.character_x
        self.sprite.rect.y = self.character_y
        self.update(player)

    def update(self, player):
        if self.sprite.rect.y == self.character_y and \
                self.sprite.rect.x == self.character_x:
            player.take_damage(7)


class EnemyMelee(BaseCharacter):
    def __init__(self, x, y):
        super().__init__("GoblinSpriteSheet.png", "GoblinSpriteWalkSheet.png", "GoblinSpriteAttackSheet.png", 6, 7, 10)

        tile_width, tile_height = 128, 128
        self.sprite.rect.x = x * tile_width
        self.sprite.rect.y = y * tile_height
        self.enemy_x = self.sprite.rect.x
        self.enemy_y = self.sprite.rect.y
        self.summ = 199
        self.hp_enemy_melee = 100
        self.name = "melee"

    def get_hp(self):
        hp = self.hp_enemy_melee * 0.01
        return hp

    def set_player_coords(self, player):
        self.character_x, self.character_y = player.get_coords()

    def get_damage(self, player):
        if abs(self.character_x - self.enemy_x) <= 100 and \
                abs(self.character_y - self.enemy_y) <= 100:
            self.hp_enemy_melee -= player.weapon_now.damage
            if self.hp_enemy_melee <= 0:
                self.sprite.kill()
                self.sprite.rect.x = 100000

    def range_attack(self, group, player):
        self.set_walking(False)
        self.enemy_x = self.sprite.rect.x
        self.enemy_y = self.sprite.rect.y
        self.summ += 2
        if self.summ >= 200:
            self.summ = 399
        if abs(self.character_x - self.enemy_x) <= 400 and \
                abs(self.character_y - self.enemy_y) <= 400:
            self.attack_target(group, player)
            self.attack_target(group, player)
            self.attack_target(group, player)
            self.attack_target(group, player)
            self.attack_target(group, player)

    def attack_target(self, group, player):
        if abs(self.character_x - self.enemy_x) >= 83 or \
                abs(self.character_y - self.enemy_y) >= 83:
            if self.character_x < self.enemy_x \
                    and self.can_walk("W", group):
                self.sprite.direction = False
                self.set_walking(True)
                self.sprite.rect.x -= 1
            if self.character_x > self.enemy_x \
                    and self.can_walk("E", group):
                self.sprite.direction = True
                self.set_walking(True)
                self.sprite.rect.x += 1
            if self.character_y < self.enemy_y\
                    and self.can_walk("N", group):
                self.set_walking(True)
                self.sprite.rect.y -= 1
            if self.character_y > self.enemy_y\
                    and self.can_walk("S", group):
                self.set_walking(True)
                self.sprite.rect.y += 1
        else:
            self.summ += 1
            if self.summ % 400 == 0:
                self.set_attacking(True)
                player.take_damage(8)
                self.summ = 0
        self.enemy_x = self.sprite.rect.x
        self.enemy_y = self.sprite.rect.y


class EnemyRange(BaseCharacter):
    def __init__(self, x, y):
        super().__init__("MageSpriteSheet.png", "MageSpriteWalkSheet.png", "MageSpriteFireAttackSheet.png", 5, 7, 10)

        tile_width, tile_height = 128, 128
        self.sprite.rect.x = x * tile_width
        self.sprite.rect.y = y * tile_height
        self.enemy_x = self.sprite.rect.x
        self.enemy_y = self.sprite.rect.y
        self.flag = False
        self.summ = 199
        self.hp = 85
        self.name = "range"

    def get_hp(self):
        hp = self.hp * 0.01
        return hp

    def create_bullet(self, *args):
        self.bullet = Bullet(self.enemy_x, self.enemy_y)
        return self.bullet

    def set_player_coords(self, player):
        self.character_x, self.character_y = player.get_coords()

    def get_damage(self, player):
        if abs(self.character_x - self.enemy_x) <= 100 and \
                abs(self.character_y - self.enemy_y) <= 100:
            self.hp -= player.weapon_now.damage
            if self.hp <= 0:
                self.sprite.kill()
                self.sprite.rect.x = 100000

    def range_attack(self, group, player):
        self.set_walking(False)
        self.enemy_x = self.sprite.rect.x
        self.enemy_y = self.sprite.rect.y
        self.summ += 2
        if self.summ >= 200:
            self.summ = 399
        if abs(self.character_x - self.enemy_x) <= 450 and \
                abs(self.character_y - self.enemy_y) <= 450:
            self.attack_target(group, player)
            self.attack_target(group, player)

    def attack_target(self, group, player):
        if abs(self.character_x - self.enemy_x) >= 300 or \
                abs(self.character_y - self.enemy_y) >= 300:
            if self.character_x < self.enemy_x \
                    and self.can_walk("W", group):
                self.sprite.direction = False
                self.set_walking(True)
                self.sprite.rect.x -= 1
            if self.character_x > self.enemy_x \
                    and self.can_walk("E", group):
                self.sprite.direction = True
                self.set_walking(True)
                self.sprite.rect.x += 1
            if self.character_y < self.enemy_y \
                    and self.can_walk("N", group):
                self.set_walking(True)
                self.sprite.rect.y -= 1
            if self.character_y > self.enemy_y \
                    and self.can_walk("S", group):
                self.set_walking(True)
                self.sprite.rect.y += 1
        else:
            self.summ += 1
            if self.summ % 400 == 0:
                self.set_attacking(True)
                self.flag = True
                self.summ = 0
        self.enemy_x = self.sprite.rect.x
        self.enemy_y = self.sprite.rect.y
