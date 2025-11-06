import pygame
import math


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 10
    mode = 'brush'
    color = (0, 0, 255)
    start_pos = None
    drawing = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_b:
                    color = (0, 0, 255)
                    mode = "brush"
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                    mode = "brush"
                elif event.key == pygame.K_r:
                    color = (255, 0, 0)
                    mode = "brush"
                elif event.key == pygame.K_c:
                    mode = "circle"
                elif event.key == pygame.K_t:
                    mode = "rect"
                elif event.key == pygame.K_e:
                    mode = "eraser"

            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos
                drawing = True

            if event.type == pygame.MOUSEBUTTONUP:
                end_pos = event.pos
                drawing = False
                if mode == "rect":
                    pygame.draw.rect(screen, color,
                                     pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])), 2)
                elif mode == "circle":
                    radius_shape = int(math.dist(start_pos, end_pos))
                    pygame.draw.circle(screen, color, start_pos, radius_shape, 2)

            if event.type == pygame.MOUSEMOTION and drawing:
                if mode == "brush":
                    pygame.draw.circle(screen, color, event.pos, radius)
                elif mode == "eraser":
                    pygame.draw.circle(screen, (255, 255, 255), event.pos, radius)

        pygame.display.flip()
        clock.tick(60)


main()