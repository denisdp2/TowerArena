from MainCharacter import MainCharacter
from Tile import Tile
from Weapon import Weapon
from HealingSalve import HealingSalve
from Enemies import EnemyMelee, EnemyRange
from Boss import Boss


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line for line in mapFile]

    return level_map


def generate_level(*args):
    level, tile_group, main_group, walls_group = args
    weapons = []
    salves = []
    enemies = []
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile(tile_group, main_group, 'floor', x, y)
            elif level[y][x] == 'u':
                Tile(tile_group, main_group, 'wall_up', x, y)
            elif level[y][x] == 'z':
                Tile(walls_group, main_group, 'corner_right-up', x, y)
            elif level[y][x] == 'r':
                Tile(walls_group, main_group, 'wall_right', x, y)
            elif level[y][x] == 'e':
                Tile(tile_group, main_group, 'corner_right-down', x, y)
            elif level[y][x] == 'd':
                Tile(walls_group, main_group, 'wall_down', x, y)
            elif level[y][x] == 'l':
                Tile(walls_group, main_group, 'wall_left', x, y)
            elif level[y][x] == 'g':
                Tile(walls_group, main_group, 'corner_right-down', x, y)
            elif level[y][x] == 's':
                Tile(walls_group, main_group, 'street', x, y)
            elif level[y][x] == 'c':
                Tile(walls_group, main_group, 'corner_left-down', x, y)
            elif level[y][x] == 'x':
                Tile(walls_group, main_group, 'corner_left-up', x, y)
            elif level[y][x] == '@':
                Tile(tile_group, main_group, 'floor', x, y)
                player = MainCharacter(x, y)
                weapons.append(player.weapon_now)
            elif level[y][x] == 'i':
                Tile(walls_group, main_group, 'vertical_wall', x, y)
            elif level[y][x] == '_':
                Tile(walls_group, main_group, 'vertical_wall_end', x, y)
            elif level[y][x] == 'm':
                Tile(tile_group, main_group, 'floor', x, y)
                enemies.append(EnemyMelee(x, y))
            elif level[y][x] == 'R':
                Tile(tile_group, main_group, 'floor', x, y)
                enemies.append(EnemyRange(x, y))
            elif level[y][x] == 'B':
                Tile(tile_group, main_group, 'floor', x, y)
                enemies.append(Boss(x, y))
            elif level[y][x] == '+':
                Tile(tile_group, main_group, 'floor', x, y)
                salves.append(HealingSalve(x, y))
            elif level[y][x] == '7':
                Tile(tile_group, main_group, 'floor', x, y)
                weapons.append(Weapon("weapon_example.png", x, y, 5))
            elif level[y][x] == '6':
                Tile(tile_group, main_group, 'floor', x, y)
                weapons.append(Weapon("weapon_example4.png", x, y, 3.3))
            elif level[y][x] == '5':
                Tile(tile_group, main_group, 'floor', x, y)
                weapons.append(Weapon("weapon_example2.png", x, y, 3.7))
            elif level[y][x] == '4':
                Tile(tile_group, main_group, 'floor', x, y)
                weapons.append(Weapon("weapon_example3.png", x, y, 4.1))

    return player, weapons, salves, enemies
