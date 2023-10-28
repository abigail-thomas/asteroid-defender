import pygame
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Asteroid Defender')

# load images
bg = pygame.image.load('img/bg.png')
asteroid = pygame.image.load('img/asteroid.png')

game_over = False

while not game_over:

    # draw background
    screen.blit(bg, (0, 0))

    # if user clicks exit window, game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True
    

    pygame.display.update()

pygame.quit()