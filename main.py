import pygame 
from pygame.locals import *
import constants
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    on = True

    while on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
        log_state()
        screen.fill("black")
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()
