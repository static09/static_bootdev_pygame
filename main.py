import pygame
from constants import *
from circleshape import *
from player import Player

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    while pygame.get_init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        player.draw(screen)
        pygame.display.flip()
    pygame.time.Clock.tick(60)
    dt = pygame.time.Clock.tick(60) / 1000


if __name__ == "__main__":
    main()
