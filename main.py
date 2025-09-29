import pygame
import sys
from constants import *
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    Shot.containers = (updatable_group, drawable_group, shot_group)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable_group.update(dt)

        for obj in asteroids_group:
            if CircleShape.collisions(player, obj):
                sys.exit("GAME OVER!")
            else:
                pass

        for obj in asteroids_group:
            for bullet in shot_group:
                if CircleShape.collisions(bullet, obj):
                    print("HIT!")
                    obj.kill()
                    bullet.kill()
                else:
                    pass

        screen.fill("black")

        for drawable in drawable_group:
            drawable.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
