import pygame
from player import Player

pygame.init()

pygame.display.set_caption("JimmyG Adventures")
screen = pygame.display.set_mode((1000, 563))

# Load Player
playerX, playerY = 99, 468
player = Player(playerX, playerY, screen)

# Set Background Image
bg = pygame.image.load("bg\\2_game_background.png")
# Set and Load Player Variables
# Load background and Player

screen.blit(bg, (0, 0))

clock = pygame.time.Clock()
pressed_right = False
pressed_left = False

# Game loop
while 1:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            playerX -= 10
        if keys[pygame.K_d]:
            playerX += 10

        screen.blit(bg, (0, 0))
        player.update_player(playerX, playerY)
        pygame.display.update()
        clock.tick(120)
