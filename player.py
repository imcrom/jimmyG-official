import pygame


class Player:
    jimmy = None

    def __init__(self, x, y, screen):
        self.jimmy = pygame.image.load("character\\charac.png")
        self.jimmy_x = x
        self.jimmy_y = y
        self.screen = screen
        screen.blit(self.jimmy, (x, y))

    def update_player(self, x, y):
        self.screen.blit(self.jimmy, (x, y))
