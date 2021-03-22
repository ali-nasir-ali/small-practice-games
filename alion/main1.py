
import pygame
import random

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load('player.png')
playerx = 370
playery = 480
playerx_change= 0
playery_change= 0

# enemy
enemyimg = pygame.image.load('enemy.png')
enemyx = random.randint(0, 800)
enemyy = random.randint(50, 150)
enemyx_change= 10
enemyy_change= 5

# bullet
bulletimg = pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bulletx_change= 0
bullety_change= 10
bullet_state = "ready"

def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy(x, y):
    screen.blit(enemyimg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x+16, y+10))


# Game Loop
running = True
while running:
    # RBG
    screen.fill((0, 0, 0))
    # Background
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              running = False

    # keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                   playerx_change = -8
            if event.key == pygame.K_RIGHT:
                   playerx_change = 8
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                   bulletx = playerx
                   fire_bullet(bulletx, bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
    enemyx += enemyx_change
    if enemyx <= 0:
        enemyx_change = 8
        enemyy += enemyy_change
    elif enemyx >= 736:
        enemyx_change = -8
        enemyy += enemyy_change
    if bullety <=0:
        bullety = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletx,bullety)
        bullety -= bullety_change

    player(playerx, playery)
    enemy(enemyx, enemyy)
    pygame.display.update()