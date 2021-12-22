import os
import sys
import pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 500
FPS = 60


class Button(pygame.sprite.Sprite):
    def __init__(self, position, text, size,
                 colors="white on blue",
                 hover_colors="red on green",
                 style=2, borderc=(255, 255, 255),
                 command=lambda: print("No command activated for this button")):
        super().__init__()
        self.text = text
        self.command = command
        self.colors = colors
        self.original_colors = colors
        self.fg, self.bg = self.colors.split(" on ")
        if hover_colors == "red on green":
            self.hover_colors = f"{self.bg} on {self.fg}"
        else:
            self.hover_colors = hover_colors
        self.style = style
        self.borderc = borderc
        self.font = pygame.font.SysFont("Arial", size)
        self.render()
        self.x, self.y, self.w, self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect((self.x, self.y), (self.w, self.h))
        self.position = position
        self.pressed = 1
        buttons.add(self)

    def render(self):
        self.text_render = self.font.render(self.text, True, self.fg)
        self.image = self.text_render

    def update(self):
        self.fg, self.bg = self.colors.split(" on ")
        if self.style == 1:
            self.draw_button()
        elif self.style == 2:
            self.draw_button_fone()
        self.hover()
        self.click()

    def draw_button(self):
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y), (self.x + self.w, self.y), 5)
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y - 2), (self.x, self.y + self.h), 5)
        pygame.draw.line(screen, (50, 50, 50), (self.x, self.y + self.h), (self.x + self.w, self.y + self.h), 5)
        pygame.draw.line(screen, (50, 50, 50), (self.x + self.w, self.y + self.h), [self.x + self.w, self.y], 5)
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w, self.h))

    def draw_button_fone(self):
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w, self.h), 0, 13)

    def hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.colors = self.hover_colors
        else:
            self.colors = self.original_colors
        self.render()

    def click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                print("Execunting code for button '" + self.text + "'")
                self.command()
                self.pressed = 0
            if pygame.mouse.get_pressed() == (0, 0, 0):
                self.pressed = 1


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


def on_play():
    print("Сейчас должно было открыться меню уровней")


def on_exit():
    sys.exit()


def on_shop():
    print("А тут магазин")


def on_version():
    print('Версии')


def on_profiles():
    print('Профили')


def buttons_def():
    Button((315, 200), " Играть    ", 36, "red on yellow",
           hover_colors="blue on orange", style=2, borderc=(255, 255, 0),
           command=on_play)
    Button((315, 265), " Магазин ", 36, "red on yellow",
           hover_colors="blue on orange", style=2, borderc=(255, 255, 0),
           command=on_shop)
    Button((315, 330), " Выход    ", 36, "red on yellow",
           hover_colors="blue on orange", style=2, borderc=(255, 255, 0),
           command=on_exit)
    Button((0, 465), " Версии    ", 36, "red on green",
           hover_colors="blue on green", style=2, borderc=(255, 255, 0),
           command=on_version)
    Button((605, 5), " Профиль    ", 36, "red on green",
           hover_colors="blue on green", style=2, borderc=(255, 255, 0),
           command=on_profiles)


def draw_nik(nik):
    font = pygame.font.Font(None, 25)
    text = font.render(nik, True, (0, 200, 0))
    screen.blit(text, (800 - len(nik) * 12, 50))


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE))
    pygame.display.set_caption('The Roped')
    clock = pygame.time.Clock()
    buttons = pygame.sprite.Group()
    buttons_def()
    image = load_image("fon.jpg")
    running = True
    screen.blit(image, (0, 0))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            # Текстовые данные на экране
            # Название
            font = pygame.font.Font(None, 100)
            text = font.render('The Roped', True, (0, 200, 0))
            screen.blit(text, (225, 100))

            # Версия
            font = pygame.font.Font(None, 25)
            text = font.render('Version: 0.0.1 (alpha)', True, (0, 200, 0))
            screen.blit(text, (5, 440))

            # Вывод ника
            draw_nik('Ник профиля')
        buttons.update()
        buttons.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()
pygame.quit()
