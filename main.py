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
        self.gui_font = pygame.font.SysFont("Arial", 30)
        self.buttons = []
        self.image = load_image("fon.jpg")
        self.button_draw()

    def button_draw(self):
        Button(self.buttons, 'старт', 200, 40, (300, 200), 4, self.gui_font, function=self.start)
        Button(self.buttons, 'магазин', 200, 40, (300, 260), 4, self.gui_font)
        Button(self.buttons, 'выход', 200, 40, (300, 320), 4, self.gui_font, function=lambda: sys.exit())
        Button(self.buttons, 'профиль', 90, 30, (705, 10), 4, pygame.font.SysFont("Arial", 20),
               function=self.pprriinntt)

    def update(self):
        self.screen.blit(self.image, (0, 0))
        font = pygame.font.SysFont('Arial', 100)
        text = font.render('The Roped', True, (100, 100, 120))
        self.screen.blit(text, (200, 50))
        font = pygame.font.SysFont('Arial', 18)
        text = font.render('Version: 0.0.3 (alpha)', True, (0, 0, 0))
        self.screen.blit(text, (4, 477))

    def buttons_update(self):
        for b in self.buttons:
            b.update(self.screen)

    def pprriinntt(self):
        print('pprriinntt')

    def run(self):
        self.m_running = True
        while self.m_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.update()
            self.buttons_update()
            pygame.display.update()
            self.clock.tick(60)

    def start(self):
        lev_menu = LevelMenu()
        lev_menu.run()


class LevelMenu(Menu):
     def button_draw(self):
         Button(self.buttons, 'назад', 770, 30, (20, 460), 4, pygame.font.SysFont("Arial", 20),
                function=self.close)
         Button(self.buttons, '1', 70, 70, (10, 10), 4, pygame.font.SysFont("Arial", 40))
         Button(self.buttons, '2', 70, 70, (90, 10), 4, pygame.font.SysFont("Arial", 40))
         Button(self.buttons, '3', 70, 70, (170, 10), 4, pygame.font.SysFont("Arial", 40))
         Button(self.buttons, '4', 70, 70, (250, 10), 4, pygame.font.SysFont("Arial", 40))
         Button(self.buttons, '5', 70, 70, (330, 10), 4, pygame.font.SysFont("Arial", 40))
         Button(self.buttons, '6', 70, 70, (410, 10), 4, pygame.font.SysFont("Arial", 40))
         Button(self.buttons, '7', 70, 70, (490, 10), 4, pygame.font.SysFont("Arial", 40))
         Button(self.buttons, '8', 70, 70, (570, 10), 4, pygame.font.SysFont("Arial", 40))
         Button(self.buttons, '9', 70, 70, (650, 10), 4, pygame.font.SysFont("Arial", 40))
         Button(self.buttons, '10', 70, 70, (730, 10), 4, pygame.font.SysFont("Arial", 40))

     def update(self):
         self.screen.blit(self.image, (0, 0))

     def close(self):
         self.m_running = False


pygame.init()
#music()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    cd = Menu()
    cd.run()
    pygame.quit()
    break
sys.exit()