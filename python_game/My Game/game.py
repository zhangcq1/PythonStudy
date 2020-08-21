import pygame,sys
from pygame.locals import *
import game_1
import game_2
def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('bgm5.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)

    bg=pygame.image.load('bg.jpg')
    bgpos=bg.get_rect()
    rw=pygame.image.load('bg.jpg')
    rwpos=rw.get_rect()
    size=width,height=960,500
    screen=pygame.display.set_mode(size)
    pygame.display.set_caption('My Game')

    role=game_1.Player()
    i=0
    group=pygame.sprite.Group()

    state=True
    while state:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        key=pygame.key.get_pressed()
        if key[K_a]:
            role.move_left()
        if key[K_d]:
            role.move_right()
        if key[K_w]:
            role.move_up()
        if key[K_s]:
            role.move_down()


        screen.blit(bg, bgpos)
        screen.blit(role.img,role.rect)

        i=i+1
        if i%60==0:
            enemy=game_2.Enemy()
            group.add(enemy)
        for p in group.sprites():
            p.move()
            screen.blit(p.img,p.rect)
            if pygame.sprite.collide_mask(role,p):
                state=False
                pause()
        pygame.display.flip()
        pygame.time.Clock().tick(60)

def pause():
    bg_go=pygame.image.load('GameOver.jpg')
    bg_gopos=bg_go.get_rect()
    size=x,y=800,500
    screen=pygame.display.set_mode(size)
    pygame.display.set_caption('Game Over')
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        img_src='replay1.png'
        img=pygame.image.load(img_src)
        img_srcpos=img.get_rect()


        mouse_press=pygame.mouse.get_pressed()
        mouse_pos=pygame.mouse.get_pos()

        left=img_srcpos.left
        right=img_srcpos.right
        top=img_srcpos.top
        bottom=img_srcpos.bottom

        if left<mouse_pos[0]<right and top<mouse_pos[1]<bottom:
            img_src = 'replay2.png'
            img = pygame.image.load(img_src)
            if mouse_press[0]:
                main()

        screen.blit(bg_go,bg_gopos)
        screen.blit(img,img_srcpos)
        pygame.display.flip()
main()
