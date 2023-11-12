# AED 2 DOGO
# Johnatas Philipe Rodrigues da Silva
# Pedro Henrique Souza dos Santos

from informed_search import *
from heapTools import *
import pygame

def main():
    # colours
    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (0, 0, 255)

    # screen setup
    width = 1280
    height = 736
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("The Dogo game")

    # square size and Dogo's initial position
    square_size = 32
    x_dogo = 0
    y_dogo = 0

    # pygame init
    pygame.init()
    clock = pygame.time.Clock()
    

    # initial loop
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple")

        # ------------------------------------------ DOGO GAME INIT ------------------------------------------
        # draw the game tray
        for line in range(height // square_size):
            for column in range(width // square_size):
                colour = white if (line + column) % 2 == 0 else black
                pygame.draw.rect(
                    screen,
                    colour,
                    (
                        column * square_size, 
                        line * square_size,
                        square_size,
                        square_size
                    )
                )
        
        pygame.draw.circle(
            screen,
            blue,
            (
                x_dogo + square_size // 2,
                y_dogo + square_size // 2
            ),
            square_size // 2
        )

        pygame.display.flip()

        # To verify Dogo's moviment
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x_dogo -= square_size
        if keys[pygame.K_RIGHT]:
            x_dogo += square_size
        if keys[pygame.K_UP]:
            y_dogo -= square_size
        if keys[pygame.K_DOWN]:
            y_dogo += square_size


        # ------------------------------------------ DOGO GAME END ------------------------------------------
        pygame.display.flip()

        clock.tick(60) # limits FPS to 60
    
    # pygame end
    pygame.quit()

if __name__ == '__main__':
    main()