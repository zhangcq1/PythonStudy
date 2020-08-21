#调用pygame,sys
import pygame,sys
from pygame.locals import*
pygame.init()#初始化操作
windows=pygame.display.set_mode((500,400))#生成一个500X400的窗口
pygame.display.set_caption('hello world')#窗口名字命名为'hello world'

pygame.


while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    color=pugame.Color(255,128,0)
