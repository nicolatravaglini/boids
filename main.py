import pygame
from Boids import Boids


def update(win, boids):
    win.fill((0, 0, 0))

    boids.update()
    boids.draw()

    pygame.display.update()


def main():
    pygame.init()
    width, height = 1200, 800
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("tua madre è un boid")

    boids = Boids(window, width, height, 50)
    boids.generate()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        update(window, boids)


if __name__ == '__main__':
    main()
