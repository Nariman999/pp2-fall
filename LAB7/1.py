import pygame
import sys
import datetime as dt

pygame.init()

W, H = 1440, 1000
window = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mickey Mouse Clock")

fps = pygame.time.Clock()

bg = pygame.image.load("mickey.jpg").convert_alpha()
hand_min = pygame.image.load("right_hand.png").convert_alpha()
hand_sec = pygame.image.load("left_hand.png").convert_alpha()
center_pos = (W // 2, H // 2)

def spin(img, ang):
    new_img = pygame.transform.rotate(img, ang)
    new_rect = new_img.get_rect(center=center_pos)
    return new_img, new_rect

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    t = dt.datetime.now()
    s = t.second
    m = t.minute

    ang_s = -(s * 6)
    ang_m = -(m * 6 + s * 0.1)

    window.fill((140, 230, 245))
    bg_rect = bg.get_rect(center=center_pos)
    window.blit(bg, bg_rect)

    img_s, rect_s = spin(hand_sec, ang_s)
    img_m, rect_m = spin(hand_min, ang_m)

    window.blit(img_s, rect_s)
    window.blit(img_m, rect_m)

    pygame.display.update()
    fps.tick(60)
