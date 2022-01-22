import sys
import pygame
from buttons import Button
from functions import load_image, music
from roped import *
pygame.init()

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 500
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.SysFont('Arial', 27)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def clean(self):
        self.text += '123231'

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.clean()
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if self.txt_surface.get_width() <= 150:
                        self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = 167
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y - 3))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


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
        Button(self.buttons, 'Старт', 200, 60, (300, 220), 4, self.gui_font, function=self.start)
        Button(self.buttons, '<', 40, 40, (20, 240), 4, self.gui_font, function=self.left)
        Button(self.buttons, 'Buy', 170, 40, (60, 390), 4, self.gui_font)
        Button(self.buttons, '>', 40, 40, (230, 240), 4, self.gui_font, function=self.right)
        Button(self.buttons, 'Выход', 200, 60, (300, 300), 4, self.gui_font, function=lambda: sys.exit())
        Button(self.buttons, 'Log in', 168, 30, (620, 150), 4, pygame.font.SysFont("Arial", 20),
               function=self.log_in)
        self.input_box1 = InputBox(620, 60, 60, 26)
        self.input_box2 = InputBox(620, 110, 60, 26)
        self.input_boxes = [self.input_box1, self.input_box2]

    def left(self):
        pass

    def right(self):
        pass

    def update(self):
        self.screen.blit(self.image, (0, 0))
        font = pygame.font.SysFont('Arial', 100)
        text = font.render('The Roped', True, (100, 100, 120))
        self.screen.blit(text, (200, 50))
        font = pygame.font.SysFont('Arial', 18)
        text = font.render('Version: 0.2.1 (beta)', True, (0, 0, 0))
        self.screen.blit(text, (4, 477))
        font = pygame.font.SysFont('Arial', 18)
        text = font.render('''Войти в профиль, или создать новый''', True, (0, 0, 0))
        self.screen.blit(text, (530, 9))
        text = font.render('Login:', True, (0, 0, 0))
        self.screen.blit(text, (620, 35))
        text = font.render('Password', True, (0, 0, 0))
        self.screen.blit(text, (620, 87))
        for box in self.input_boxes:
            box.update()
        for box in self.input_boxes:
            box.draw(self.screen)

    def buttons_update(self):
        for b in self.buttons:
            b.update(self.screen)

    def log_in(self):
        self.input_box1.clean()
        self.input_box2.clean()

    def run(self):
        self.m_running = True
        while self.m_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if self.input_boxes:
                    for box in self.input_boxes:
                        box.handle_event(event)

            self.update()
            self.buttons_update()
            pygame.display.update()
            self.clock.tick(60)

    def start(self):
        lev_menu = LevelMenu()
        lev_menu.run()


class LevelMenu(Menu):
     def button_draw(self):
         Button(self.buttons, 'Назад', 770, 30, (20, 460), 4, pygame.font.SysFont("Arial", 20),
                function=self.close)
         Button(self.buttons, '1', 150, 150, (40, 175), 4, pygame.font.SysFont("Arial", 40), function=self.start_level_1)
         Button(self.buttons, '2', 150, 150, (230, 175), 4, pygame.font.SysFont("Arial", 40), function=self.start_level_2)
         Button(self.buttons, '3', 150, 150, (420, 175), 4, pygame.font.SysFont("Arial", 40), function=self.start_level_3)
         Button(self.buttons, '4', 150, 150, (610, 175), 4, pygame.font.SysFont("Arial", 40), function=self.start_level_4)
         self.input_boxes = False

     def update(self):
         self.screen.blit(self.image, (0, 0))

     def close(self):
         self.m_running = False

     def start_level_1(self):
         startt(0)
         self.screen = pygame.display.set_mode(WINDOW_SIZE)
         pygame.display.flip()

     def start_level_2(self):
         startt(1)
         self.screen = pygame.display.set_mode(WINDOW_SIZE)
         pygame.display.flip()

     def start_level_3(self):
         startt(2)
         self.screen = pygame.display.set_mode(WINDOW_SIZE)
         pygame.display.flip()

     def start_level_4(self):
         startt(3)
         self.screen = pygame.display.set_mode(WINDOW_SIZE)
         pygame.display.flip()


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