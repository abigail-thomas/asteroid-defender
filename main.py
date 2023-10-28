import pygame
from pygame.locals import *

import random

pygame.init()

screen_width = 770
screen_height = 530

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Asteroid Defender')

clock = pygame.time.Clock()
fps = 60

# variables
game_over = False
scroll = 0
scroll_speed = .5
score = 0

# load images
bg = pygame.image.load('asteroid-defender/img/stars.png')
ship = pygame.image.load('asteroid-defender/img/ship.png')
title = pygame.image.load('asteroid-defender/img/title.png')
start = pygame.image.load('asteroid-defender/img/start.png')

# resize images
bg = pygame.transform.scale(bg, (770, 530))
ship = pygame.transform.scale(ship, (150, 150))
title = pygame.transform.scale(title, (700, 100))

# start button 
# class Button():
# draw start button
# screen.blit(start, ((screen_width / 2) - 75, 250))

# the ship


# the asteroids
class Asteroid(pygame.sprite.Sprite):

    def __init__(self, x, y, position):
        self.image = pygame.image.load('asteroid-defender/img/asteroid.png')
        self.rect = self.image.get_ret()

        if position == 1:
            self.rect.topleft = [x, y]

    def update(self):
        self.rect.y += scroll_speed    # move asteroids down
        if self.rect.top > 770:
            self.kill()    # delete astroid if off screen


# main loop
while not game_over:

    # draw background (two so theres seamless scrolling)
    screen.blit(bg, (0, scroll))
    screen.blit(bg, (0, scroll - 530))

    # draw ship
    screen.blit(ship, ((screen_width / 2) - 75, 400))

    # draw title
    # screen.blit(title, ((screen_width / 2) - 350, 40))

    # scroll the game
    scroll += scroll_speed
    if abs(scroll) > 530:
        scroll = 0

    # if user clicks exit window, game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()

pygame.quit()