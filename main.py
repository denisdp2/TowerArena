import sys

import pygame as pg
from Camera import Camera
from variables import *
from StartScreen import start_screen

from level_loading import generate_level, load_level

pg.init()

screen = pg.display.set_mode(size)
clock = pg.time.Clock()
camera = Camera()

pg.key.set_repeat(int(1000 / FPS))

# Создание групп спрайтов
bullets = pg.sprite.Group()
second_lvl_sprites = pg.sprite.Group()
third_lvl_sprites = pg.sprite.Group()
walls_group = pg.sprite.Group()
tiles_group = pg.sprite.Group()
pg.display.set_caption("TowerArena")

player, weapons, salves, enemies = generate_level(load_level("lvl1"), tiles_group,
                                                  first_lvl_sprites, walls_group)
# Добавление спрайтов в группы
for i in weapons:
    first_lvl_sprites.add(i)
for salve in salves:
    first_lvl_sprites.add(salve)
for enemy in enemies:
    first_lvl_sprites.add(enemy.get_sprite())
    characters_sprites.add(enemy.get_sprite())
first_lvl_sprites.add(player.get_sprite())
characters_sprites.add(player.get_sprite())


# Поток отрисовки
def draw():
    screen.fill("black")
    first_lvl_sprites.draw(screen)
    pg.draw.rect(screen, "white", (5, HEIGHT - 25, 300, 20), 1)
    pg.draw.rect(screen, "red", (6, HEIGHT - 24, 298 * player.get_hp(), 18))
    camera.update(player, size[0], size[1])
    if pg.mouse.get_focused():
        screen.blit(cursor_image, cursor_pos)

    for enemy in enemies:
        camera.apply_player(enemy)
        if enemy.name == "OneManApocalypse":
            pg.draw.rect(screen, "white", (enemy.enemy_x - 74, enemy.enemy_y, 451, 20), 1)
            pg.draw.rect(screen, "red", (enemy.enemy_x - 72, enemy.enemy_y + 1,
                                         149 * enemy.get_hp(), 18))
        elif enemy.name == "melee":
            pg.draw.rect(screen, "white", (enemy.enemy_x + 3, enemy.enemy_y, 80, 10), 1)
            pg.draw.rect(screen, "red", (enemy.enemy_x + 4, enemy.enemy_y + 1,
                                     78 * enemy.get_hp(), 8))
        elif enemy.name == "range":
            pg.draw.rect(screen, "white", (enemy.enemy_x + 3, enemy.enemy_y, 68, 10), 1)
            pg.draw.rect(screen, "red", (enemy.enemy_x + 4, enemy.enemy_y + 1,
                                         78 * enemy.get_hp(), 8))
        enemy.set_player_coords(player)
        enemy.range_attack(walls_group, player)
        if enemy.name == "range" and enemy.flag is True:
            bullet = enemy.create_bullet(bullets, first_lvl_sprites)
            bullets.add(bullet.get_sprite())
            bullet.set_player_coords(player)
            bullet.attack_target(player)
            enemy.flag = False
        bullets.draw(screen)

    for salve in salves:
        camera.apply_field(salve)

    for weapon in weapons:
        camera.apply_field(weapon)

    camera.apply_player(player)

    for i in bullets:
        camera.apply_field(i)
    for i in walls_group:
        camera.apply_field(i)
    for i in tiles_group:
        camera.apply_field(i)


running = True
hit = False
hit_quit = 0
repeat = 1
cursor_pos = (0, 0)

start_screen()

while running:
    walking = False
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            walking = True
            player.move("N", walls_group)
        if keys[pg.K_a]:
            walking = True
            player.move("W", walls_group)
            player.change_direction('W')
        if keys[pg.K_d]:
            walking = True
            player.move("E", walls_group)
            player.change_direction('E')
        if keys[pg.K_s]:
            walking = True
            player.move("S", walls_group)
        if keys[pg.K_e]:
            if repeat % 2 == 0:
                for index_weapon in range(1, len(weapons)):
                    weapon = weapons[index_weapon]
                    if weapon.is_taken(player):
                        x, y = player.get_coords()
                        weapons[index_weapon] = player.weapon_now
                        player.weapon_now.update_position(x + 30, y)
                        weapon.update_position(x - 100000, y)
                        player.take_weapon(weapon)
                        weapons[0] = weapon
            repeat += 1
        if event.type == pg.MOUSEBUTTONDOWN and event.button == pg.BUTTON_LEFT:
            hit = True
        if event.type == pg.MOUSEMOTION:
            cursor_pos = event.pos

    for salve in salves:
        if pg.sprite.collide_mask(salve, player.get_sprite()):
            if player.health + 50 > 100 and player.health != 100:
                player.health = 100
                salve.rect.x = 100000
                salve.kill()
            elif player.health + 50 < 100:
                player.health += 50
                salve.rect.x = 100000
                salve.kill()

    draw()
    clock.tick(FPS)
    if hit:
        for enemy in enemies:
            enemy.get_damage(player)
        player.get_sprite().update_hit()
        hit_quit += 1
    else:
        if walking:
            player.get_sprite().update_move()
        else:
            player.get_sprite().update_breath()
    for enemy in enemies:
        if enemy.get_walking():
            enemy.get_sprite().update_move()
            enemy.set_attacking(False)
        elif enemy.get_attacking():
            enemy.get_sprite().update_hit()
        else:
            enemy.get_sprite().update_breath()
    for i in bullets:
        i.update_breath()
        if pg.time.get_ticks() % 100 == 0:
            i.kill()

    pg.display.flip()
    if hit_quit % 10 == 0:
        hit = False
pg.quit()
sys.exit()
