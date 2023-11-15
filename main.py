import pygame
from pygame.locals import *

import random

pygame.init()

# import music
from pygame import mixer

# initialize pygame
pygame.init()

# initalize the music
mixer.init()

# load audio files
mixer.music.load('asteroid-defender/audio/bg_music.mp3')

# set volume
mixer.music.set_volume(1)
    
# play the music
mixer.music.play()

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
asteroids_list = []

# load images
bg = pygame.image.load('asteroid-defender/img/stars.png')
asteroid_img = pygame.image.load('asteroid-defender/img/asteroid.png').convert_alpha()
ship = pygame.image.load('asteroid-defender/img/ship.png')
title = pygame.image.load('asteroid-defender/img/title.png')
start = pygame.image.load('asteroid-defender/img/start.png')
gameover = pygame.image.load('asteroid-defender/img/gameover.png')
ammo = pygame.image.load('asteroid-defender/img/ammo.png')
playagain = pygame.image.load('asteroid-defender/img/play_again.png')

# set the ships initial position
shipX = (screen_width / 2) - 37.5
shipY = 440

# asteroid size
asteroidX = random.randint(50, 100)
asteroidY = random.randint(50, 100)

# resize images
bg = pygame.transform.scale(bg, (770, 530))
asteroid_img = pygame.transform.scale(asteroid_img, (asteroidX, asteroidY))
ship = pygame.transform.scale(ship, (75, 100))
title = pygame.transform.scale(title, (700, 100))
gameover = pygame.transform.scale(gameover, (700, 100))
ammo = pygame.transform.scale(ammo, (50, 100))

# the ship
class Ship():
    def __init__(self, x, y):
        self.image = ship
        self.width = 75
        self.height = 100
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = x    # x-coordinate of sprite's top left corner
        self.rect.y = y    # y-coordinate of sprite's top left corner

    def draw(self):
        
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
# the asteroids
class Asteroid():

    def __init__(self, x, y):
        self.image = asteroid_img
        self.width = 80
        self.height = 50
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = x    # x-coordinate of sprite's top left corner
        self.rect.y = y    # y-coordinate of sprite's top left corner

    def draw(self):
            
        screen.blit(self.image, (self.rect.x, self.rect.y))    # HELP WHAT
            
player = Ship(shipX, shipY)
asteroid = Asteroid(random.randint(0, 300), 0)

# hide mouse cursor
pygame.mouse.set_visible(False)

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

        if player.rect.colliderect(asteroid.rect):
            game_over = True

        asteroid.rect.y += 1
        if asteroid.rect.y == screen_height:
            game_over = True

        # draw asteroids
        for i in range(0, 10):

            asteroid.draw()


        # draw ship
        player.draw()

        # screen.blit(asteroid_img, (random.randint(0, screen_width), 0))

        # moving the ship
        pressed = pygame.key.get_pressed()
        
        if (pressed[K_RIGHT] or pressed[K_d]):    # if user pressed right arrow OR d key
            player.rect.x += 4
            if player.rect.x > 700:    # stop player if goes too far right
                player.rect.x = 700
        if (pressed[K_LEFT] or pressed[K_a]):    # if user pressed left arrow OR a key
            player.rect.x -= 4
            if player.rect.x < 0:    # stop player if goes too far left
                player.rect.x = 0

        if game_over == True:

            asteroid.rect.x = -100
            player.rect.y = -100
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
