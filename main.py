import pygame
from pygame import *
from general import *
from utils import *

# Объявляем переменные
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"
PLATFORM_COLOR = "#FF6262"


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

    levels = load_levels()
    lvl_c = 0  # номер текущего уровня

    entities, platforms, tr = level_loader(levels[lvl_c], hero)
    lvl_c += 1

    while 1:  # Основной цикл программы
        timer.tick(60)
        if pygame.sprite.collide_rect(hero, tr):
            if lvl_c >= len(levels):
                exit(0)
            entities, platforms, tr = level_loader(levels[lvl_c], hero)
            lvl_c += 1

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

