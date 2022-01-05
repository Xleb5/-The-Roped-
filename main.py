import os
import sys
import pygame
import pygame_gui

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 500
FPS = 60
main_menu = True
mm_running = True
p_running = False
NIK = 'Без профиля'


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE))
    pygame.display.set_caption('The Roped')
    clock = pygame.time.Clock()
    buttons = pygame.sprite.Group()
    image = load_image("fon.jpg")
    mm_running = True
    screen.blit(image, (0, 0))
    manager = pygame_gui.UIManager(WINDOW_SIZE)
    start = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30, 30), (70, 20)),
                                         text='start',
                                         manager=manager)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(start)
    all_sprites.draw(screen)
    while mm_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mm_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mm_running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start:
                    print('start')
        if main_menu:
            # Текстовые данные на экране
            # Название
            font = pygame.font.Font(None, 100)
            text = font.render('The Roped', True, (0, 200, 0))
            screen.blit(text, (225, 100))
            # Версия
            font = pygame.font.Font(None, 25)
            text = font.render('Version: 0.0.2 (alpha)', True, (0, 200, 0))
            screen.blit(text, (5, 440))

            # Вывод ника
            buttons.update()
            buttons.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()


main_menu()
pygame.quit()
