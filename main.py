from pygame import *
from pygame.sprite import *

class Ambulance(Sprite):
    def __init__(self, screen):
        Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/ambulance_animation/1.png")
        self.image = pygame.transform.scale(self.image, (128,128))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 50
        self.screen = screen
        self.move_speed = 6

    def moveleft(self):
        self.image = pygame.image.load("Sprites/ambulance_animation/2.png")
        self.rect.x -= self.move_speed
        display.flip()

    def moveright(self):
        self.image = pygame.image.load("Sprites/ambulance_animation/3.png")
        self.rect.x += self.move_speed
        display.flip()

    def moveup(self):
        self.image = pygame.image.load("Sprites/ambulance_animation/3.png")
        self.rect.y -= self.move_speed
        display.flip()

    def movedown(self):
        self.image = pygame.image.load("Sprites/ambulance_animation/2.png")
        self.rect.y += self.move_speed
        display.flip()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, screen, width, height, speedY, startX, startY):
        pygame.sprite.Sprite.__init__(self)
        self.startx = startX
        self.starty = startY

        self.speedY = speedY

        self.image = pygame.image.load("Sprites/Fake_Taxi.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect = startX
        self.rect.top = startY
        self.screen = screen

    def movement(self):
        #to make the Obstacle move
        self.rect.top += self.speedY
