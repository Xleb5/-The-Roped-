import sys
import pygame
from buttons import Button
from functions import load_image, music, profiles, update_csv_cell
from roped import *

pygame.init()

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 500
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.SysFont('Arial', 27)
SKINS_LIST = ('bunny', 'guy', 'idle', 'mario')
PROFILE = False


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def clean(self):
        self.text = ''
        self.txt_surface = FONT.render(self.text, True, self.color)

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
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y - 3))
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
        self.buy = Button(self.buttons, 'Bought', 170, 40, (60, 390), 4, self.gui_font, function=self.buy_scin)
        Button(self.buttons, '>', 40, 40, (230, 240), 4, self.gui_font, function=self.right)
        Button(self.buttons, 'Выход', 200, 60, (300, 300), 4, self.gui_font, function=lambda: sys.exit())
        Button(self.buttons, 'Log in', 168, 30, (620, 150), 4, pygame.font.SysFont("Arial", 20),
               function=self.log_in)
        self.input_box1 = InputBox(620, 60, 60, 26)
        self.input_box2 = InputBox(620, 110, 60, 26)
        self.input_boxes = [self.input_box1, self.input_box2]
        self.skin_ind = 2

    def buy_scin(self):
        if PROFILE:
            if not (SKIN in PROFILE[3]):
                if int(PROFILE[2]) >= 10:

                    PROFILE[2] = str(int(PROFILE[2]) - 10)
                    PROFILE[3] = PROFILE[3] + f' {SKIN}'
                    self.buy.text = 'bought'

                    print(PROFILE)

    def left(self):
        if PROFILE:
            self.skin_ind -= 1
            global SKIN
            SKIN = SKINS_LIST[self.skin_ind % 4]
            if SKIN in PROFILE[3]:
                self.buy.text = 'bought'
            else:
                self.buy.text = 'Buy for 10'

    def right(self):
        if PROFILE:
            self.skin_ind += 1
            global SKIN
            SKIN = SKINS_LIST[self.skin_ind % 4]
            if SKIN in PROFILE[3]:
                self.buy.text = 'Bought'
            else:
                self.buy.text = 'Buy for 10'

    def update(self):
        self.screen.blit(self.image, (0, 0))
        font = pygame.font.SysFont('Arial', 80)
        text = font.render('The Roped', True, (100, 100, 120))
        self.screen.blit(text, (200, 50))
        font = pygame.font.SysFont('Arial', 18)
        text = font.render('Version: 0.2.1 (beta)', True, (0, 0, 0))
        self.screen.blit(text, (4, 477))
        font = pygame.font.SysFont('Arial', 18)
        text = font.render('''Войти в профиль, или создать новый''', True, (0, 0, 0))
        self.screen.blit(text, (480, 9))
        text = font.render('Key 1:', True, (0, 0, 0))
        self.screen.blit(text, (620, 35))
        text = font.render('Key 2:', True, (0, 0, 0))
        self.screen.blit(text, (620, 87))
        self.c_image = pygame.transform.scale(pygame.image.load('data/coin.png'), (60, 60))
        self.screen.blit(self.c_image, (20, 20))
        if PROFILE:
            font = pygame.font.SysFont('Arial', 45)
            text = font.render(PROFILE[2], True, (100, 100, 120))
            self.screen.blit(text, (87, 24))

        for box in self.input_boxes:
            box.update()
        for box in self.input_boxes:
            box.draw(self.screen)
        self.skin = pygame.transform.scale(pygame.image.load(f'data/skins/{SKINS_LIST[self.skin_ind % 4]}.png'),
                                           (60, 75))
        self.screen.blit(self.skin, (120, 220))
        self.buy.change_text(self.buy.text)

    def buttons_update(self):
        for b in self.buttons:
            b.update(self.screen)

    def log_in(self):
        a = profiles(self.input_box1.text, self.input_box2.text)
        print(a)
        self.input_box1.clean()
        self.input_box2.clean()
        global PROFILE
        PROFILE = a

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
        global SKIN
        if PROFILE and not (SKIN in PROFILE[3]):
            SKIN = 'idle'
        lev_menu = LevelMenu()
        lev_menu.run()


class LevelMenu(Menu):
    def button_draw(self):
        Button(self.buttons, 'Назад', 770, 30, (20, 460), 4, pygame.font.SysFont("Arial", 20),
               function=self.close)
        Button(self.buttons, '1', 150, 150, (40, 175), 4, pygame.font.SysFont("Arial", 40), function=self.start_level_1)
        Button(self.buttons, '2', 150, 150, (230, 175), 4, pygame.font.SysFont("Arial", 40),
               function=self.start_level_2)
        Button(self.buttons, '3', 150, 150, (420, 175), 4, pygame.font.SysFont("Arial", 40),
               function=self.start_level_3)
        Button(self.buttons, '4', 150, 150, (610, 175), 4, pygame.font.SysFont("Arial", 40),
               function=self.start_level_4)
        self.input_boxes = False

    def update(self):
        self.screen.blit(self.image, (0, 0))

    def close(self):
        self.m_running = False

    def mn_f(self):
        if PROFILE:
            from roped import MONEY
            PROFILE[2] = str(int(PROFILE[2]) + MONEY)

    def start_level_1(self):

        a = startt(SKIN, 0)
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.mn_f()
        pygame.display.flip()

    def start_level_2(self):
        startt(SKIN, 1)
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.mn_f()
        pygame.display.flip()

    def start_level_3(self):
        startt(SKIN, 2)
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.mn_f()
        pygame.display.flip()

    def start_level_4(self):
        startt(SKIN, 3)
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.mn_f()
        pygame.display.flip()


music('data/melody/menu.mp3')
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
