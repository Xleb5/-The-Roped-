import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
LEVEL = None
SKIN1 = 'data/skins/idle.png'
SKIN2 = 'data/skins/idle.png'
bg = pygame.transform.scale(pygame.image.load('bg.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT))


class Player(pygame.sprite.Sprite):
    right = True

    def __init__(self, image):
        super().__init__()
        self.image = image
        self.coins = 0
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.calc_grav()
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right
        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            self.change_y = 0
        if pygame.sprite.spritecollide(self, self.level.coins_list, True):
            self.coins += 1
        if pygame.sprite.spritecollide(self, self.level.flag, True):
            end_game()

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .95
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        # Обработка прыжка
        self.rect.y += 10
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 10

        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -16

    # Передвижение игрока
    def go_left(self):
        self.change_x = -9
        if self.right:
            self.flip()
            self.right = False

    def go_right(self):
        self.change_x = 9
        if not self.right:
            self.flip()
            self.right = True

    def stop(self):
        self.change_x = 0

    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)


player1 = Player(pygame.image.load(SKIN))
player2 = Player(pygame.image.load(SKIN))


# Класс платформы
class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('platform.png')
        self.rect = self.image.get_rect()


class Flag(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('flag.png'), (63, 74))
        self.rect = self.image.get_rect()


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('coin.png'), (38, 38))
        self.rect = self.image.get_rect()


class Level(object):
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.coins_list = pygame.sprite.Group()
        self.flag = pygame.sprite.Group()
        self.player = player

    def update(self):
        self.platform_list.update()
        self.coins_list.update()

    def draw(self, screen):
        screen.blit(bg, (0, 0))
        self.platform_list.draw(screen)
        self.coins_list.draw(screen)
        self.flag.draw(screen)


class Level_1(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        # Платформы
        platforms = [
            [520, 170],
            [200, 300],
            [400, 300],
            [520, 350],
            [600, 400],
            [660, 470],
        ]
        for platform in platforms:
            block = Platform()
            block.rect.x = platform[0]
            block.rect.y = platform[1]
            block.player = self.player
            self.platform_list.add(block)

        # Finish
        block = Flag()
        block.rect.x = 75
        block.rect.y = 75
        block.player = self.player
        self.flag.add(block)

        # Монеты
        coins = [
            [520, 250],
            [420, 250],
            [320, 250],
            [650, 125],
        ]
        for coin in coins:
            block = Coin()
            block.rect.x = coin[0]
            block.rect.y = coin[1]
            self.coins_list.add(block)


class Level_2(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        level = [
            [520, 470],
            [200, 600],
            [400, 600],
            [520, 650],
            [600, 700],
            [660, 770],
        ]

        for platform in level:
            block = Platform()
            block.rect.x = platform[0]
            block.rect.y = platform[1]
            block.player = self.player
            self.platform_list.add(block)


class Level_3(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        level = [
            [520, 470],
            [200, 600],
            [400, 600],
            [520, 650],
            [600, 700],
            [660, 770],
        ]

        for platform in level:
            block = Platform()
            block.rect.x = platform[0]
            block.rect.y = platform[1]
            block.player = self.player
            self.platform_list.add(block)


class Level_4(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        level = [
            [520, 470],
            [200, 600],
            [400, 600],
            [520, 650],
            [600, 700],
            [660, 770],
        ]

        for platform in level:
            block = Platform()
            block.rect.x = platform[0]
            block.rect.y = platform[1]
            block.player = self.player
            self.platform_list.add(block)


def end_game():
    global done, screen
    done = False
    screen.fill((100, 100, 100))
    font = pygame.font.Font(None, 60)
    text1 = font.render('Нажмите любую клавишу для выхода', True, (100, 255, 100))
    text2 = font.render(f'+{player1.coins + player2.coins}', True, (100, 255, 100))
    screen.blit(text1, (110, 200))
    screen.blit(text2, (450, 275))
    pygame.display.flip()
    f = True
    while f:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = False
            if event.type == pygame.KEYDOWN:
                f = False


def startt(ind):
    global done, screen, player1, player2
    pygame.init()
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("The Roped")

    level_list = []
    level_list.append(LEVELS[ind](player1))

    current_level_num = 0
    current_level = level_list[current_level_num]

    active_sprite_list = pygame.sprite.Group()
    player1.level = current_level
    player2.level = current_level

    player1.rect.x = 340
    player1.rect.y = SCREEN_HEIGHT - player1.rect.height
    player2.rect.x = 340
    player2.rect.y = SCREEN_HEIGHT - player2.rect.height
    active_sprite_list.add(player1)
    active_sprite_list.add(player2)
    done = True
    clock = pygame.time.Clock()

    while done:
        dif = int(((player1.rect.x - player2.rect.x) ** 2 + (player1.rect.y - player2.rect.y) ** 2) ** 0.5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player1.go_left()
                if event.key == pygame.K_RIGHT:
                    player1.go_right()
                if event.key == pygame.K_UP:
                    player1.jump()
                if event.key == pygame.K_a:
                    player2.go_left()
                if event.key == pygame.K_d:
                    player2.go_right()
                if event.key == pygame.K_w:
                    player2.jump()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player1.change_x < 0:
                    player1.stop()
                if event.key == pygame.K_RIGHT and player1.change_x > 0:
                    player1.stop()
                if event.key == pygame.K_a and player2.change_x < 0:
                    player2.stop()
                if event.key == pygame.K_d and player2.change_x > 0:
                    player2.stop()

        active_sprite_list.update()
        current_level.update()
        if player1.rect.right > SCREEN_WIDTH:
            player1.rect.right = SCREEN_WIDTH
        if player1.rect.left < 0:
            player1.rect.left = 0
        if player2.rect.right > SCREEN_WIDTH:
            player2.rect.right = SCREEN_WIDTH
        if player2.rect.left < 0:
            player2.rect.left = 0
        x1, x2 = player1.rect.x, player2.rect.x
        y1, y2 = player1.rect.y, player2.rect.y
        if dif >= 400:
            go_x, go_y = x1 - x2, y1 - y2
            player1.rect.x += go_x // -40
            player2.rect.x += go_x // 40
            player1.rect.y += go_y // -40
            player2.rect.y += go_y // 40
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        clock.tick(60)
        font = pygame.font.Font(None, 75)
        text = font.render(str(player1.coins + player2.coins), True, (100, 255, 100))
        screen.blit(text, (900, 10))
        pygame.draw.line(screen, (int(254 * dif / 405) % 256, 255 - int(254 * dif / 405) % 256,
                                  255 - int(254 * dif / 405) % 256),
                         (x1 + 30, y1 + 50), (x2 + 30, y2 + 50), 7)
        pygame.display.flip()
    pygame.display.flip()


LEVELS = [Level_1, Level_2, Level_3, Level_4]
