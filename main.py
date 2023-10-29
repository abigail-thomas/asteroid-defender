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
# asteroid_gap = 50
ship_move = 0
ship_speed = 0

# load images
bg = pygame.image.load('asteroid-defender/img/stars.png')
asteroid = pygame.image.load('asteroid-defender/img/asteroid.png').convert_alpha()
ship = pygame.image.load('asteroid-defender/img/ship.png')
title = pygame.image.load('asteroid-defender/img/title.png')
start = pygame.image.load('asteroid-defender/img/start.png')
gameover = pygame.image.load('asteroid-defender/img/gameover.png')
ammo = pygame.image.load('asteroid-defender/img/ammo.png')

asteroid_sizeX = random.randint(50, 100)
asteroid_sizeY = random.randint(50, 100)

# set the ships initial position
shipX = (screen_width / 2) - 75
shipY = 400


# resize images
bg = pygame.transform.scale(bg, (770, 530))
asteroid = pygame.transform.scale(asteroid, (asteroid_sizeX, asteroid_sizeY))
ship = pygame.transform.scale(ship, (150, 150))
title = pygame.transform.scale(title, (700, 100))
ammo = pygame.transform.scale(ammo, (50, 100))

# start button 
# class Button():
# draw start button
# screen.blit(start, ((screen_width / 2) - 75, 250))

# the ship
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init()
        self.image = ship
        self.rect = self.image.get_rect()
        self.rect.x = x    # x-coordinate of sprite's top left corner
        self.rect.y = y    # y-coordinate of sprite's top left corner

# the asteroids 
class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = asteroid
        self.rect = self.image.get_rect()
        self.rect.x = x    # x-coordinate of sprite's top left corner
        self.rect.y = y    # y-coordinate of sprite's top left corner
        
            

    def update(self):
        self.rect.y += scroll_speed
        # if self.rect.y > 530:
            # self.rect.y = 0 # put asteroid back at top of screen
            # self.rect.x = random.randint(40, 730)

class Ammo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = ammo
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= scroll_speed
    # if self.rect.y > 530:
        # self.rect.y = 0 # put asteroid back at top of screen
        # self.rect.x = random.randint(40, 730)



asteroid_group = pygame.sprite.Group()
roids = Asteroid(random.randint(40, 730), 0)
ship_group = pygame.sprite.Group()
ammo_group = pygame.sprite.Group()
ammos = Ammo(300, 530)


# adding asteroids
asteroid_group.add(roids)

# main loop
while not game_over:

    # if user clicks exit window, game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    '''clock.tick(fps)
    time = pygame.time.get_ticks()    # in milliseconds
'''
    # draw background (two so theres seamless scrolling)
    screen.blit(bg, (0, scroll))
    screen.blit(bg, (0, scroll - 530))

    # draw asteroids
    # asteroid_group.draw(pygame.display.get_surface())
    # screen.blit(asteroid, (0, scroll))
    asteroid_group.draw(screen)
    asteroid_group.update()

    # draw ship
    screen.blit(ship, ((shipX, shipY)))


    # moving the ship
    pressed = pygame.key.get_pressed()
    
    if (pressed[K_RIGHT] or pressed[K_d]):    # if user pressed right arrow OR d key
        shipX = shipX + 3
        if shipX > 660:    # stop player if goes too far right
            shipX = 660
    if (pressed[K_LEFT] or pressed[K_a]):    # if user pressed left arrow OR a key
        shipX = shipX - 3
        if shipX < -45:    # stop player if goes too far left
            shipX = -45

    # draw ammo
    ammo_group.draw(screen)
    ammo_group.update()
    

    

    # check for ship/ asteroid collision
    

    # if asteroid passes ship, stop game
    if roids.rect.y > 530:
        scroll_speed = 0


    # draw title
    # screen.blit(title, ((screen_width / 2) - 350, 40))

    # scroll the game
    scroll += scroll_speed
    if abs(scroll) > 530:
        scroll = 0

    pygame.display.update()

pygame.quit()
