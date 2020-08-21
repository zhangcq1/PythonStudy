import pygame,sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        position= 50,250
        self.img=pygame.image.load('player.png')
        self.rect=self.img.get_rect()
        self.rect.center=position
        self.image=self.img
    def move_left(self):
        self.speed=[-5,0]
        if self.rect.left<=-80:
            self.rect.left=-80
        else:
            self.rect=self.rect.move(self.speed)

    def move_right(self):
        self.speed=[5,0]
        if self.rect.right>=1000:
            self.rect.right=1000
        else:
            self.rect=self.rect.move(self.speed)


    def move_up(self):
        self.speed=[0,-5]
        if self.rect.top<=150:
            self.rect.top=150
        else:
            self.rect=self.rect.move(self.speed)


    def move_down(self):
        self.speed=[0,5]
        if self.rect.bottom>=450:
            self.rect.bottom=450
        else:
            self.rect=self.rect.move(self.speed)