from BaseCharacter import BaseCharacter
import EndScene


class Boss(BaseCharacter):
    def __init__(self, x, y):
        super().__init__("BossSpriteSheet.png", "BossSpriteWalkSheet.png", "BossSpriteAttackSheet.png", 4, 6, 8)
        self.hp = 550
        tile_width, tile_height = 128, 128
        self.sprite.rect.x = x * tile_width
        self.sprite.rect.y = y * tile_height
        self.enemy_x = self.sprite.rect.x
        self.enemy_y = self.sprite.rect.y
        self.summ = 199
        self.name = "OneManApocalypse"

    def get_hp(self):
        hp = self.hp * 0.0055
        return hp

    def set_player_coords(self, player):
        self.character_x, self.character_y = player.get_coords()

    def get_damage(self, player):
        if abs(self.character_x - self.enemy_x) <= 100 and \
                abs(self.character_y - self.enemy_y) <= 100:
            self.hp -= player.weapon_now.damage
            if self.hp <= 0:
                self.sprite.kill()
                self.sprite.rect.x = 10000
                self.sprite.rect.y = 10000
                EndScene.start_screen()

    def range_attack(self, group, player):
        self.set_walking(False)
        self.enemy_x = self.sprite.rect.x
        self.enemy_y = self.sprite.rect.y
        self.summ += 2
        if self.summ >= 300:
            self.summ = 599
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
            if self.summ % 600 == 0:
                self.set_attacking(True)
                player.take_damage(30)
                self.summ = 0
        self.enemy_x = self.sprite.rect.x
        self.enemy_y = self.sprite.rect.y
