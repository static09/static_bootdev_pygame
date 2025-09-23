import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()
    dt = 0
    while pygame.get_init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.flip()
    pygame.time.Clock.tick(60)
    dt = pygame.time.Clock.tick()/1000


if __name__ == "__main__":
    main()
