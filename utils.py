import os
import pygame
from general import *
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32


def load_level(path_to_level: str):
    with open(path_to_level, "r") as f:
        return list(map(str.strip, f.readlines()))


def load_levels():
    level_paths = os.listdir("levels")
    levels = []
    for path in level_paths:
        levels.append(load_level("levels/" + path))
    return levels


def level_loader(level, hero):
    tr = None
    entities = pygame.sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться
    entities.add(hero)
    x = 0
    y = 0
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            elif col == '*':
                tr = Treasure(x, y)
                entities.add(tr)
            elif col == "p":
                hero.change_pos(x, y)
            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля
    return entities, platforms, tr


# if __name__ == '__main__':
#     print(*load_levels(), sep="\n")