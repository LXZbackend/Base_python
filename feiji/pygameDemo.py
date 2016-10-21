#coding=utf-8

#导入pygame库
import pygame

#向sys模块借一个exit函数用来退出程序
from sys import exit

#初始化pygame,为使用硬件做准备
pygame.init()


#创建了一个窗口,窗口大小和背景图片大小一样
screen = pygame.display.set_mode((600, 170), 0, 32)


#设置窗口标题
pygame.display.set_caption("Hello, World!")


#加载并转换图像
background = pygame.image.load('bg.jpg').convert()


#游戏主循环
while True:


    for event in pygame.event.get():

    	#接收到退出事件后退出程序
        if event.type == pygame.QUIT:

            pygame.quit()

            exit()

	#将背景图画上去
    screen.blit(background, (0,0))

    
	#刷新一下画面
    pygame.display.update()

