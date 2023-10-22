from TowerArena import DeathScreen
from TowerArena.BaseCharacter import BaseCharacter
from Weapon import Weapon


class MainCharacter(BaseCharacter):
    def __init__(self, x, y):
        super().__init__("MainCharacterSpriteSheet.png", "MainCharacterSpriteWalkSheet.png",
                         "MainCharacterSpriteAttackSheet.png", 6, 7, 10)

        self.weapon_now = Weapon("started_weapon.png", -20, -20, 2)
        self.health = 100
        tile_width, tile_height = 128, 128
        self.sprite.rect.x = x * tile_width
        self.sprite.rect.y = y * tile_height

    def move(self, direction, group):
        if direction == 'N':
            if self.can_walk(direction, group):
                self.sprite.rect.y -= 15
        if direction == 'W':
            if self.can_walk(direction, group):
                self.sprite.rect.x -= 15
        if direction == 'S':
            if self.can_walk(direction, group):
                self.sprite.rect.y += 15
        if direction == 'E':
            if self.can_walk(direction, group):
                self.sprite.rect.x += 15

    def get_coords(self):
        return self.sprite.rect.x, self.sprite.rect.y

    def get_hp(self):
        hp = self.health * 0.01
        return hp

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            DeathScreen.start_screen()

    def take_weapon(self, weapon):
        self.weapon_now = weapon


