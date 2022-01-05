import sys
import pygame
from buttons import Button


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Gui Menu')
clock = pygame.time.Clock()
gui_font = pygame.font.SysFont("Arial", 30)
buttons = []
button1 = Button(buttons, 'старт', 200, 40, (100, 200), 4, gui_font)
button2 = Button(buttons, 'магазин', 200, 40, (100, 250), 4, gui_font)
button3 = Button(buttons, 'выход', 200, 40, (100, 300), 4, gui_font, function=lambda: print('hello'))


def buttons_draw():
    for b in buttons:
        b.update(screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('#DCDDD8')
    buttons_draw()

    pygame.display.update()
    clock.tick(60)