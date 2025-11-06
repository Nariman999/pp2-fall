import pygame, sys
from pygame.locals import *
import random, time

def start_game():
    pygame.init()
    pygame.mixer.init()

    engine_sound = pygame.mixer.Sound("ferari.engine.wav")
    engine_sound.set_volume(0.4)
    engine_sound.play(-1)

    coin_sound = pygame.mixer.Sound("coin_s.wav")
    coin_sound.set_volume(0.6)

    FPS = 60
    FramePerSec = pygame.time.Clock()

    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 600
    SPEED = 5
    SCORE = 0
    CS = 0

    font_small = pygame.font.SysFont("Verdana", 20)
    big_font = pygame.font.SysFont("Verdana", 60)
    game_over_text = big_font.render("Game Over", True, BLACK)

    background = pygame.image.load("AnimatedStreet.png")
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Game")

    class Coins(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.original_image = pygame.image.load("coin.png").convert_alpha()
            self.image = pygame.transform.scale(self.original_image, (32, 32))
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        def move(self):
            self.rect.move_ip(0, SPEED)
            if self.rect.top > SCREEN_HEIGHT:
                self.rect.top = 0
                self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("Enemy.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        def move(self):
            nonlocal SCORE
            self.rect.move_ip(0, SPEED)
            if self.rect.top > SCREEN_HEIGHT:
                SCORE += 1
                self.rect.top = 0
                self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("Player.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.center = (160, 520)
        def move(self):
            pressed_keys = pygame.key.get_pressed()
            if self.rect.left > 0 and pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
            if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    P1 = Player()
    E1 = Enemy()
    C1 = Coins()

    enemies = pygame.sprite.Group()
    enemies.add(E1)

    coins = pygame.sprite.Group()
    coins.add(C1)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1, E1, C1)

    INC_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INC_SPEED, 1000)

    while True:
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                SPEED += 0.3
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        DISPLAYSURF.blit(background, (0, 0))
        DISPLAYSURF.blit(font_small.render("Score: " + str(SCORE), True, BLACK), (10, 10))
        DISPLAYSURF.blit(font_small.render("Coins: " + str(CS), True, BLACK), (300, 10))

        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()

        hit_coins = pygame.sprite.spritecollide(P1, coins, True, pygame.sprite.collide_mask)
        if hit_coins:
            coin_sound.play()
            CS += 1
            new_coin = Coins()
            coins.add(new_coin)
            all_sprites.add(new_coin)

        for enemy in enemies:
            if pygame.sprite.collide_mask(P1, enemy):
                engine_sound.stop()
                pygame.mixer.Sound("crash.wav").play()
                DISPLAYSURF.fill(RED)
                DISPLAYSURF.blit(game_over_text, (30, 250))
                DISPLAYSURF.blit(font_small.render("Press R to Restart", True, BLACK), (110, 330))
                pygame.display.update()

                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == KEYDOWN and event.key == K_r:
                            return start_game()
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()

        pygame.display.update()
        FramePerSec.tick(FPS)

start_game()