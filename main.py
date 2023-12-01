# importing libraries
import pygame
from pygame.locals import *
import random
from pygame import mixer

# initialize pygame and music
pygame.init()
mixer.init()

font = pygame.font.SysFont('', 50)

# the audio
def bg_audio():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio/bg_music.mp3'))
bg_audio()
def game_over_audio():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('audio/game_over_audio.mp3'))
def boom_audio():
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('audio/boom.mp3'))


# set the screen dimensions
SCREEN_WIDTH = 770
SCREEN_HEIGHT = 530

# create the window, name it, and set icon
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Asteroid Defender')
icon = pygame.image.load('./img/ship.png')
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
hi_score = 0
clicked = False

# load images
bg = pygame.image.load('./img/stars.png')
asteroid_img = pygame.image.load('./img/asteroid.png')
ship = pygame.image.load('./img/ship.png')
title = pygame.image.load('./img/title.png')
start = pygame.image.load('./img/start.png')
gameover = pygame.image.load('./img/gameover.png')
playagain = pygame.image.load('./img/play_again.png')

# resize images
bg = pygame.transform.scale(bg, (770, 530))
# random sizes for asteroids
asteroidX = random.randint(50, 100)     
asteroidY = random.randint(50, 100)
asteroid_img = pygame.transform.scale(asteroid_img, (asteroidX, asteroidY))
ship = pygame.transform.scale(ship, (75, 100))
title = pygame.transform.scale(title, (700, 100))
gameover = pygame.transform.scale(gameover, (700, 100))

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
        self.speed = 1.5

    def move(self):
        # moving asteroids down the screen
        self.rect.y += self.speed

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Bullet():

    def __init__(self, x, y):
        self.width = 7.5
        self.height = 15
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.speed = 1

    def move(self):
        # Move the bullet up the screen
        self.rect.y -= self.speed

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

# the ammo 
class Ammo():

    def __init__(self, x, y):
        self.width = 7.5
        self.height = 15
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.speed = 1

    def move(self):
        # shooting the ammo up
        self.rect.y -= self.speed

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
        
    def create_new_bullet(self):
        return Bullet(self.rect.x + 32.5, self.rect.y - 20)
    
class Button():

    def __init__(self, x, y):
        self.width = 225
        self.height = 60
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
    
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)


# set the ships initial position
shipX = (SCREEN_WIDTH / 2) - 37.5
shipY = (SCREEN_HEIGHT - 50)

# creating instances
# the ship
player = Ship(shipX + 37.5, shipY)
# the asteroids
asteroid1 = Asteroid(random.randint(0, 200), random.randint(-200, 0))
asteroid2 = Asteroid(random.randint(250, 400), random.randint(-200, 0))
asteroid3 = Asteroid(random.randint(450, 750), random.randint(-200, 0))
# the ammo
# ammo = Ammo(player.rect.x + 32.5, shipY - 20)
bullet = Bullet(player.rect.x + 32.5, shipY - 10)
bullets = []

button = Button(SCREEN_WIDTH/ 2 + 5, SCREEN_HEIGHT / 2 - 20)

# the start menu !
def start_menu():
    # show mouse cursor
    pygame.mouse.set_visible(True)
    # draw background with no scrolling
    screen.blit(bg, (0, 0))
    # draw title
    screen.blit(title, ((SCREEN_WIDTH / 2) - 350, 40))
    # draw start
    screen.blit(start, (SCREEN_WIDTH/ 2 - 60, SCREEN_HEIGHT / 2 - 40))
    # draw ship with no movement allowed yet
    player.draw()

    button.draw()

# the text 
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# the actual game running 
def game_playing():
    # hide mouse cursor
    pygame.mouse.set_visible(False)

    global score
    # draw background with scrolling
    screen.blit(bg, (0, scroll))
    screen.blit(bg, (0, scroll - 530))

    

     # draw and move all existing bullets
    for bullet in bullets:
        bullet.draw()
        bullet.move()

        # check for collision with asteroids
        if bullet.rect.colliderect(asteroid1.rect):
            # increase score
            score += 1
            boom_audio()
            # reset asteroid position
            asteroid1.rect.x = random.randint(0, 200)
            asteroid1.rect.y = random.randint(-200, 0)
            # remove the bullet
            bullets.remove(bullet)

        if bullet.rect.colliderect(asteroid2.rect):
            score += 1
            boom_audio()
            asteroid2.rect.x = random.randint(250, 400)
            asteroid2.rect.y = random.randint(-200, 0)
            bullets.remove(bullet)

        if bullet.rect.colliderect(asteroid3.rect):
            score += 1
            boom_audio()
            asteroid3.rect.x = random.randint(450, 750)
            asteroid3.rect.y = random.randint(-200, 0)
            bullets.remove(bullet)

        # remove bullets that are off-screen
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

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

    # draw score in top left corner
    draw_text(str(score), font, (255, 0, 0), 20, 20)

# game over screen
def game_over():
    # show mouse cursor
    pygame.mouse.set_visible(True)
    # draw background with no scrolling anymore
    screen.blit(bg, (0, 0))
    # print GAME OVER screen
    screen.blit(gameover, ((SCREEN_WIDTH / 2) - 350, 80))
    # ask user if they wish to play again
    screen.blit(playagain, (SCREEN_WIDTH/ 2 - 90, SCREEN_HEIGHT / 2 - 40))
    # draw ship in initial position with no movement allowed anymore
    player.rect.x = shipX
    player.draw()
    # set asteroids back to initial position 
    asteroid1.rect.x = random.randint(20, 200)
    asteroid1.rect.y = random.randint(-200, 0)
    asteroid2.rect.x = random.randint(250, 400)
    asteroid2.rect.y = random.randint(-200, 0)
    asteroid3.rect.x = random.randint(450, 720)
    asteroid3.rect.y = random.randint(-200, 0)
    # set ammo back to initial position
    # ammo.rect.x = player.rect.x + 32.5
    # ammo.rect.y = shipY - 20

    
    button.draw()

# main game loop 
while run:

    # if user clicks exit window, game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(fps)
    time = pygame.time.get_ticks()

    pressed = pygame.key.get_pressed()   

   
    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check if the mouse is over the button
    if button.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] == 1:
        # Do something
        start_game = True

        if game_end:
            start_game = True
            game_end = False
        
    # if pygame.mouse.get_pos() and :
    
    # if game has not begun yet
    if not start_game:
        start_menu()

    # if user has pressed space bar to start:
    else:
        # game plays until game over
        if not game_end:
            game_playing()
            pygame.mixer.Channel(0).unpause()

            #pressed = pygame.key.get_pressed()   

            # draw and move all existing bullets
            for bullet in bullets:
                bullet.draw()
                bullet.move()

            # remove bullets that are off-screen
            bullets = [bullet for bullet in bullets if bullet.rect.y > 0]

            # shoot when user clicks mouse
            if pygame.mouse.get_pressed()[0] == 1 and clicked == False:    # if left mouse bar clicked
                clicked = True
                ammo = Ammo(player.rect.x + 35, shipY - 40)
                bullets.append(ammo)
    
            if pygame.mouse.get_pressed()[0] == 0:    # if left mouse bar not clicked
                clicked = False


    # check for player collision with asteroids OR asteroids pass the player
    if player.rect.colliderect(asteroid1.rect)\
        or player.rect.colliderect(asteroid2.rect)\
        or player.rect.colliderect(asteroid3.rect)\
        or asteroid1.rect.top > SCREEN_HEIGHT\
        or asteroid2.rect.top > SCREEN_HEIGHT\
        or asteroid3.rect.top > SCREEN_HEIGHT:
        # if there is collision or asteroid passes, call game over
        game_over()
        game_over_audio()
        pygame.mixer.Channel(0).pause()

        # change game end to True
        game_end = True
        # empty the list of bullets for new game 
        bullets = []

        if score > hi_score:
            hi_score = score

            score = 0

        # draw hi score here 
        draw_text(str("Hi-Score: "), font, (255, 0, 0), 20, 20)
        draw_text(str(hi_score), font, (255, 0, 0), 200, 20)

            
    # press space to restart
    

    # scroll the game
    scroll += scroll_speed
    if abs(scroll) > 530:
        scroll = 0

    pygame.display.update()

pygame.quit()
