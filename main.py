import sys
import pygame
from buttons import Button
from functions import load_image, music


WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 500


class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption('The Roped')
        self.clock = pygame.time.Clock()
        gui_font = pygame.font.SysFont("Arial", 25)
        self.buttons = []
        Button(self.buttons, 'старт', 200, 40, (300, 200), 4, gui_font)
        Button(self.buttons, 'магазин', 200, 40, (300, 260), 4, gui_font)
        Button(self.buttons, 'выход', 200, 40, (300, 320), 4, gui_font, function=lambda: sys.exit())
        Button(self.buttons, 'профиль', 90, 30, (705, 10), 4, pygame.font.SysFont("Arial", 20),
               function=self.pprriinntt)
        self.image = load_image("fon.jpg")

    def buttons_draw(self):
        for b in self.buttons:
            b.update(self.screen)

    def pprriinntt(self):
        print('pprriinntt')

    def run(self):
        m_running = True
        while m_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    m_running = False
            self.screen.blit(self.image, (0, 0))
            font = pygame.font.SysFont('Arial', 100)
            text = font.render('The Roped', True, (100, 100, 120))
            self.screen.blit(text, (200, 50))
            font = pygame.font.SysFont('Arial', 18)
            text = font.render('Version: 0.0.2 (alpha)', True, (0, 0, 0))
            self.screen.blit(text, (4, 477))
            self.buttons_draw()
            pygame.display.update()
            self.clock.tick(60)


pygame.init()
music()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    cd = Menu()
    cd.run()
    pygame.quit()
    break
pygame.quit()
sys.exit()