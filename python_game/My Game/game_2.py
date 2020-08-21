import pygame
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        y=randint(240,350)
        position=[1000,y]
        enemy1=pygame.image.load('enemy.png')
        self.img=pygame.transform.flip(enemy1,True,False)
        #self.img = pygame.image.load('enemy2')
        self.rect = self.img.get_rect()
        self.rect.center = position
        self.image = self.img

        speed=[-4,0]
        self.speed=speed
    def move(self):
        self.rect=self.rect.move(self.speed)