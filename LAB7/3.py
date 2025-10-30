import pygame
import sys

pygame.init()

W, H = 800, 600
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Moving Ball")
fps = pygame.time.Clock()

radius = 25
move = 20
bx, by = W // 2, H // 2
go = True

while go:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            go = False
        if ev.type == pygame.KEYDOWN:
            new_x, new_y = bx, by
            if ev.key == pygame.K_a or ev.key == pygame.K_LEFT:
                new_x -= move
            elif ev.key == pygame.K_d or ev.key == pygame.K_RIGHT:
                new_x += move
            elif ev.key == pygame.K_w or ev.key == pygame.K_UP:
                new_y -= move
            elif ev.key == pygame.K_s or ev.key == pygame.K_DOWN:
                new_y += move
            if radius <= new_x <= W - radius and radius <= new_y <= H - radius:
                bx, by = new_x, new_y

    win.fill((210, 230, 255))   # светло-голубой фон
    pygame.draw.circle(win, (255, 70, 120), (bx, by), radius)  # розово-красный мяч
    pygame.display.update()
    fps.tick(60)

pygame.quit()
sys.exit()
