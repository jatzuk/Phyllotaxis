import pygame
from pygame import Surface, Vector2
import math

WIDTH = 800
HEIGHT = 600

points = []


def main():
    pygame.init()
    pygame.display.set_caption("Phyllotaxis")
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    surface = pygame.Surface([WIDTH, HEIGHT], pygame.SRCALPHA)
    surface.fill((255, 255, 255))

    is_running = True

    n = 1
    c = 1

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        screen.blit(surface, (0, 0))

        for i in range(n):
            a = i * math.radians(137.5)
            r = c * math.sqrt(i)
            x = r * math.cos(a) + (WIDTH - surface.get_width() / 2)
            y = r * math.sin(a) + (HEIGHT - surface.get_height() / 2)
            rgb = (clamp(a % 256, 0, 255), clamp(r, 0, 255), clamp(n, 0, 255))
            pygame.draw.circle(surface, rgb, (x, y), 2)

        pygame.display.flip()

        n += 5

    pygame.quit()


def clamp(x, min, max):
    return x if x > min and x < max else (min if x < min else max)


if __name__ == "__main__":
    main()
