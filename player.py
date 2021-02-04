import pygame

class Player():
    def __init__(self, start):
        self.r = 20
        self.cords = start
        self.delta = 1
    
    def render(self, screen):
        pygame.draw.circle(screen, pygame.Color("black"), self.cords, self.r)
    
    def move(self, key):
        if key == 26:
            self.cords = (self.cords[0], self.cords[1] - self.delta)
        if key == 4:
            self.cords = (self.cords[0] - self.delta, self.cords[1])
        if key == 22:
            self.cords = (self.cords[0], self.cords[1] + self.delta)
        if key == 7:
            self.cords = (self.cords[0] + self.delta, self.cords[1])
        