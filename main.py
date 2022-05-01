# Импортируем библиотеку pygame
import pygame
from pygame import *
from player import Player, Treasure
from platfrom import Platform

# Объявляем переменные
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

level_1 = [
    "-------------------------",
    "-                       -",
    "-                       -",
    "-                   *   -",
    "-               ---------",
    "-                       -",
    "-    -      --          -",
    "-                       -",
    "--                      -",
    "-   --                  -",
    "-                   --- -",
    "-                       -",
    "-                       -",
    "-      ---              -",
    "-                       -",
    "-   -----------         -",
    "-                       -",
    "- --                --  -",
    "-                       -",
    "-------------------------"]

level_2 = [
    "-------------------------",
    "-                       -",
    "-                       -",
    "--              ---------",
    "-                       -",
    "-                      *-",
    "-      --       ------ --",
    "-                       -",
    "-                       -",
    "-   --     -            -",
    "-                   --- -",
    "-                       -",
    "-                       -",
    "-    --   --     --     -",
    "-                       -",
    "-      -----------      -",
    "-                       -",
    "-                   --  -",
    "-                       -",
    "-------------------------"]


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
            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля
    return entities, platforms, tr


timer = pygame.time.Clock()


def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("My First Game")  # Пишем в шапку
    bg = Surface(DISPLAY)  # Создание видимой поверхности background

    # будем использовать как бекграунд
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом

    hero = Player(55, 55)  # создаем героя по (x,y) координатам
    left = right = up = False  # по умолчанию — стоим

    entities, platforms, tr = level_loader(level_1, hero)

    while 1:  # Основной цикл программы
        timer.tick(60)
        if pygame.sprite.collide_rect(hero, tr):
            entities, platforms, tr = level_loader(level_2, hero)
        # _____________EVENTS_____________
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                exit(0)

            if e.type == KEYDOWN:
                if e.key == K_LEFT:
                    left = True
                if e.key == K_RIGHT:
                    right = True
                if e.key == K_UP:
                    up = True

            if e.type == KEYUP:
                if e.key == K_RIGHT:
                    right = False
                if e.key == K_LEFT:
                    left = False
                if e.key == K_UP:
                    up = False

        # _____________DRAWING_____________

        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        hero.update(left, right, up, platforms)

        entities.draw(screen)

        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()

