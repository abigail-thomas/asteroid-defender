# importing libraries
import pygame
from pygame.locals import *
import random
from pygame import mixer

# initialize pygame
pygame.init()
# initalize the music
mixer.init()

# hide mouse cursor
pygame.mouse.set_visible(False)

# load audio files
mixer.music.load('asteroid-defender./audio/bg_music.mp3')
# set volume
mixer.music.set_volume(1)
# play the music
mixer.music.play()

# set the screen dimensions
SCREEN_WIDTH = 770
SCREEN_HEIGHT = 530

# create the window, name it, and set icon
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Asteroid Defender')
icon = pygame.image.load('asteroid-defender./img/ship.png')
pygame.display.set_icon(icon)

# frame rate
clock = pygame.time.Clock()
fps = 60

# variables
run = True
game_end = False
start_game = False
scroll = 0
scroll_speed = .5
score = 0
ship_move = 0
ship_speed = 0

# load images
bg = pygame.image.load('asteroid-defender./img/stars.png')
asteroid_img = pygame.image.load('asteroid-defender./img/asteroid.png')
ship = pygame.image.load('asteroid-defender./img/ship.png')
title = pygame.image.load('asteroid-defender./img/title.png')
start = pygame.image.load('asteroid-defender./img/start.png')
gameover = pygame.image.load('asteroid-defender./img/gameover.png')
bullet = pygame.image.load('asteroid-defender./img/ammo.png')
playagain = pygame.image.load('asteroid-defender./img/play_again.png')

# resize images
bg = pygame.transform.scale(bg, (770, 530))
# random sizes for asteroids
asteroidX = random.randint(50, 100)     
asteroidY = random.randint(50, 100)
asteroid_img = pygame.transform.scale(asteroid_img, (asteroidX, asteroidY))
ship = pygame.transform.scale(ship, (75, 100))
title = pygame.transform.scale(title, (700, 100))
gameover = pygame.transform.scale(gameover, (700, 100))
bullet = pygame.transform.scale(bullet, (100, 100))

# spaceship 
class Ship():
    def __init__(self, x, y):
        self.image = ship
        self.width = 75
        self.height = 100
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.speed = 5

    def move(self):

        # moving the ship with left arrow, right arrow, a, or d
        pressed = pygame.key.get_pressed()
        # if user pressed right arrow OR d key
        if (pressed[K_RIGHT] or pressed[K_d]):    
            self.rect.x += self.speed
            # stop player if goes too far right
            if self.rect.x > 700:    
                self.rect.x = 700
        # if user pressed left arrow OR a key
        if (pressed[K_LEFT] or pressed[K_a]):    
            self.rect.x -= self.speed
             # stop player if goes too far left
            if self.rect.x < 0:   
                self.rect.x = 0

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
# asteroids
class Asteroid():

    def __init__(self, x, y):
        self.image = asteroid_img
        self.width = asteroidX
        self.height = asteroidY
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.speed = 2

    def move(self):
        # moving asteroids down the screen
        self.rect.y += self.speed

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

# the ammo 
class Ammo():

    def __init__(self, x, y):
        # self.image = bullet
        self.width = 7.5
        self.height = 15
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.speed = 5

    def move(self):
        # shooting the ammo up
        self.rect.y -= self.speed

    def draw(self):

        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
        # figure out how to have endless ammo shooting 


# set the ships initial position
shipX = (SCREEN_WIDTH / 2) - 37.5
shipY = (SCREEN_HEIGHT - 50)

# creating instances
# the ship
player = Ship(shipX, shipY)
# the asteroids
asteroid1 = Asteroid(random.randint(0, 200), random.randint(-200, 0))
asteroid2 = Asteroid(random.randint(250, 400), random.randint(-200, 0))
asteroid3 = Asteroid(random.randint(450, 750), random.randint(-200, 0))
# the ammo
ammo = Ammo(player.rect.x + 32.5, shipY - 20)

# the start menu !
def start_menu():
    # draw background with no scrolling
    screen.blit(bg, (0, 0))
    # draw title
    screen.blit(title, ((SCREEN_WIDTH / 2) - 350, 40))
    # draw start
    screen.blit(start, (SCREEN_WIDTH/ 2 - 280, SCREEN_HEIGHT / 2 - 40))
    # draw ship with no movement allowed yet
    player.draw()

# the actual game running 
def game_playing():
    global score
    # draw background with scrolling
    screen.blit(bg, (0, scroll))
    screen.blit(bg, (0, scroll - 530))
    # draw ammo
    # ammo.draw()
    for i in range(10):
        ammo.draw()
    # move ammo
    ammo.move()
    # draw player
    player.draw()
    # allow left and right movement for the player
    player.move()
    # draw asteroids
    asteroid1.draw()
    asteroid2.draw()
    asteroid3.draw()
    # move asteroids
    asteroid1.move()
    asteroid2.move()
    asteroid3.move()

    '''if ammo.rect.y < (SCREEN_HEIGHT // 2):
        ammo.rect.y = player.rect.y + 20
        ammo.rect.x = player.rect.x + 32.5'''



    

    # after asteroid is hit, put it back at the top of the screen
    # increase score
    if ammo.rect.colliderect(asteroid1) or ammo.rect.colliderect(asteroid2) or ammo.rect.colliderect(asteroid3) or ammo.rect.y < 0:
        ammo.rect.y = player.rect.y + 20
        ammo.rect.x = player.rect.x + 32.5
    if ammo.rect.colliderect(asteroid1):
        score += 1
        asteroid1.rect.x = random.randint(0, 200)
        asteroid1.rect.y = random.randint(-200, 0)
    if ammo.rect.colliderect(asteroid2):
        score += 1
        asteroid2.rect.x = random.randint(250, 400)
        asteroid2.rect.y = random.randint(-200, 0)
    if ammo.rect.colliderect(asteroid3):
        score += 1
        asteroid3.rect.x = random.randint(450, 750)
        asteroid3.rect.y = random.randint(-200, 0)


# game over screen
def game_over():
    # draw background with no scrolling anymore
    screen.blit(bg, (0, 0))
    # print GAME OVER screen
    screen.blit(gameover, ((SCREEN_WIDTH / 2) - 350, 40))
    # ask user if they wish to play again
    screen.blit(playagain, (SCREEN_WIDTH/ 2 - 330, SCREEN_HEIGHT / 2 - 40))
    # draw ship in initial position with no movement allowed anymore
    player.rect.x = shipX
    player.draw()
    # set asteroids back to initial position 
    asteroid1.rect.x = random.randint(0, 200)
    asteroid1.rect.y = random.randint(-200, 0)
    asteroid2.rect.x = random.randint(250, 400)
    asteroid2.rect.y = random.randint(-200, 0)
    asteroid3.rect.x = random.randint(450, 750)
    asteroid3.rect.y = random.randint(-200, 0)
    # set ammo back to initial position
    ammo.rect.x = player.rect.x + 32.5
    ammo.rect.y = shipY - 20


#########################
    ### MAIN LOOP ###
#########################
while run:

    # if user clicks exit window, game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    clock.tick(fps)
    time = pygame.time.get_ticks()


    pressed = pygame.key.get_pressed()
    
    # if user presses space bar, begin playing game
    if (pressed[K_SPACE]):  
        start_game = True
    
    # if game has not begun yet
    if not start_game:
        start_menu()

    # if user has pressed space bar to start:
    else:
        # game plays until game over
        if not game_end:
            game_playing()

        

        # check for player collision with asteroids OR asteroids pass the player
        if player.rect.colliderect(asteroid1.rect) or player.rect.colliderect(asteroid2.rect) or player.rect.colliderect(asteroid3.rect) or asteroid1.rect.top > SCREEN_HEIGHT or asteroid2.rect.top > SCREEN_HEIGHT or asteroid3.rect.top > SCREEN_HEIGHT:
            # if there is collision or asteroid passes, call game over
            game_over()
            # change game end to True
            print("here")
            game_end = True
            
                
        # press space to restart
        if (pressed[K_SPACE]):
            # restart game
            start_game = True
            # set game over back to false
            game_end = False


        # scroll the game
        scroll += scroll_speed
        if abs(scroll) > 530:
            scroll = 0

    pygame.display.update()

pygame.quit()
