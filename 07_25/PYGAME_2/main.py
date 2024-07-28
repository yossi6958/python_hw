import pygame
from game import Game


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Plane Traffic Game")

    game = Game(screen)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.update()
        game.draw()
        pygame.display.flip()

        clock.tick(10)  # Slow down the updates for better visibility

    pygame.quit()


if __name__ == "__main__":
    main()
