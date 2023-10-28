import pygame
from pygame.locals import *

import random

pygame.init()

screen_width = 770
screen_height = 530

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Asteroid Defender')

# load images
bg = pygame.image.load('asteroid-defender/img/bg.png')
asteroid = pygame.image.load('asteroid-defender/img/asteroid.png')
ship = pygame.image.load('asteroid-defender/img/ship.png')
title = pygame.image.load('asteroid-defender/img/title.png')
start = pygame.image.load('asteroid-defender/img/start.png')

# resize images
ship = pygame.transform.scale(ship, (150, 150))
title = pygame.transform.scale(title, (700, 100))

# start button 
# class Button():
# draw start button
screen.blit(start, ((screen_width / 2) - 75, 250))
    

game_over = False

# main loop
while not game_over:

    # draw background
    screen.blit(bg, (0, 0))

    # draw ship
    screen.blit(ship, ((screen_width / 2) - 75, 400))

    # draw title
    screen.blit(title, ((screen_width / 2) - 350, 40))

    # if user clicks exit window, game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()

pygame.quit()