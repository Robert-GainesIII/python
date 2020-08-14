import pygame

image = pygame.image.load('images/rpgGuy.png')

class player(object):

    def __init__(self, name, path, surface):

        self.name = name
        self.path = path
        self.image = image
        self.surface = surface
        self.x = 50
        self.y = 50


    def draw(self):

        self.surface.blit(self.image, (self.x,self.y))

    def moveX(self, dx):
        self.x += dx

    def moveY(self, dy):
        self.y += dy
        
