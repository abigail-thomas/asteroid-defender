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
run = True
game_over = False
start_game = False
scroll = 0
scroll_speed = .5
score = 0
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
playagain = pygame.image.load('asteroid-defender/img/play_again.png')

# set the ships initial position
shipX = (screen_width / 2) - 37.5
shipY = 440

# resize images
bg = pygame.transform.scale(bg, (770, 530))
asteroid_sizeX = random.randint(50, 100)
asteroid_sizeY = random.randint(50, 100)
asteroid = pygame.transform.scale(asteroid, (asteroid_sizeX, asteroid_sizeY))
ship = pygame.transform.scale(ship, (75, 100))
title = pygame.transform.scale(title, (700, 100))
gameover = pygame.transform.scale(gameover, (700, 100))
ammo = pygame.transform.scale(ammo, (50, 100))

ship_sprite = pygame.sprite.Sprite()
asteroid_sprite = pygame.sprite.Sprite()

ship_sprite.rect.x = 100
ship_sprite.rect.y = 100

asteroid_sprite.rect.x = 200
asteroid_sprite.rect.y = 200

if ship_sprite.collide_rect(asteroid_sprite):
    print("collision")
#########################
    ### MAIN LOOP ###
#########################
while run:

    # if user clicks exit window, game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(fps)
    time = pygame.time.get_ticks()    # in milliseconds
    
    # draw background (two so theres seamless scrolling)
    screen.blit(bg, (0, scroll))
    screen.blit(bg, (0, scroll - 530))

    # user hasn't pressed Start yet:
    # start button
    pressed = pygame.key.get_pressed()
    
    if (pressed[K_SPACE]):    # if user pressed space bar
        start_game = True

    if start_game == False:
        # draw title
        screen.blit(title, ((screen_width / 2) - 350, 40))

        # draw start
        screen.blit(start, (screen_width/ 2 - 280, screen_height / 2 - 40))

    # if user has pressed Start:
    else:
    
        # draw asteroids
        # asteroid_group.draw(pygame.display.get_surface())
        # screen.blit(asteroid, (0, scroll))
        
        # if time / 1000 > 3:
            # trying to generate more roids

        # draw ship
        screen.blit(ship, ((shipX, shipY)))

        # moving the ship
        pressed = pygame.key.get_pressed()
        
        if (pressed[K_RIGHT] or pressed[K_d]):    # if user pressed right arrow OR d key
            shipX = shipX + 4
            if shipX > 700:    # stop player if goes too far right
                shipX = 700
        if (pressed[K_LEFT] or pressed[K_a]):    # if user pressed left arrow OR a key
            shipX = shipX - 4
            if shipX < 0:    # stop player if goes too far left
                shipX = 0

        # check for ship/ asteroid collision
        
        # if asteroid passes ship, game over

        if game_over == True:

            scroll_speed = 0

            # stop player movement and set back to initial position
            shipX = shipX = (screen_width / 2) - 37.5
                
            # print GAME OVER
            screen.blit(gameover, ((screen_width / 2) - 350, 40))

            screen.blit(playagain, (screen_width/ 2 - 330, screen_height / 2 - 40))

            if (pressed[K_SPACE]):
                start_game == True
                game_over = False


        # scroll the game
        scroll += scroll_speed
        if abs(scroll) > 530:
            scroll = 0

    pygame.display.update()

pygame.quit()