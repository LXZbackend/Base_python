#coding=utf-8

import pygame
from pygame.locals import *
import random
from sys import exit
import time

# 定义导弹类
class Bullet:
	def __init__(self,planeName,x,y):

		print('Bullet----->>>')

		if planeName == 'enemy':
			imageName = './image/bullet-1.gif'
			self.directioin = 'down'
		elif planeName == 'hero':
			imageName = './image/bullet-3.gif'
			self.directioin = 'up'



		self.image = pygame.image.load(imageName).convert()
		self.x = x
		self.y = y

	def draw(self,screen):
		if self.directioin == 'down':
			self.y += 2
		elif self.directioin == 'up':
			self.y -= 2

		screen.blit(self.image, (self.x, self.y))

# 定义一个飞机基类
class Plane:

	def __init__(self):
		#导弹的发射时间间隔(单位为:s)
		self.bulletSleepTime = 1
		self.lastShootTime = time.time()
		#存储导弹列表
		self.bulletList = []

	def draw(self,screen):
		screen.blit(self.planeImage, (self.x, self.y))

	# 发射导弹
	def shoot(self):
		if time.time()-self.lastShootTime>self.bulletSleepTime:
			if random.randint(1,6)>=3:
				self.bulletList.append(Bullet(self.planeName,self.x,self.y))
				self.lastShootTime = time.time()


# 定义一个玩家的飞机类
class Hero(Plane):

	def __init__(self):

		Plane.__init__(self)

		planeImageName = './image/hero.gif'

		self.planeImage = pygame.image.load(planeImageName).convert()

		self.x = 230
		self.y = 600

		self.speed = 5

		self.planeName = 'hero'

	def keyHandle(self,keyValue):
		if keyValue=='left':
			self.x -= 20
		elif keyValue == 'right':
			self.x += 20
		elif keyValue == 'space':
			self.bulletList.append(Bullet('hero',self.x+40,self.y))

# 定义敌人飞机类
class Enemy(Plane):

	def __init__(self):

		Plane.__init__(self)

		randomImageNum = random.randint(1,3)

		planeImageName = './image/enemy-' + str(randomImageNum) + '.gif'

		self.planeImage = pygame.image.load(planeImageName).convert()

		self.x = 0
		self.y = 0
		self.directioin = 1 # 1表示向右  0表示向左

		self.speed = random.randint(1,5)

		self.planeName = 'enemy'

	def move(self):

		if self.directioin == 1:
			self.x += self.speed
		elif self.directioin == 0:
			self.x -= self.speed

		if self.x>480:
			self.directioin = 0
		elif self.x<0:
			self.directioin = 1


class GameInit:

	# 类属性
	# 默认为 简单
	gameLevel = 1

	g_enemyList = []

	hero = object

	# 显示等级提示
	@classmethod
	def showMenu(cls):
		# 提示用户选择，游戏难度等级
		print('='*40)
		print('      python 飞机大战\n\n')
		print('难度等级：1: 简单 2: 中等 3: 困难')
		print('='*40)

	@classmethod
	def getMenuNum(cls):
		cls.gameLevel = input("请输入要难度等级的序号:")


	@classmethod
	def createEnemys(cls):

		# 将创建出来的敌人对象添加到列表中
		for i in range(cls.gameLevel):
			cls.g_enemyList.append(Enemy())

	@classmethod
	def createHero(cls):
		cls.hero = Hero()

	# 更新飞机的位置
	@classmethod
	def setXY(cls):

		# 更新位置
		for i in cls.g_enemyList:
			i.move()

	@classmethod
	def draw(cls,screen):

		# 更新位置
		for i in cls.g_enemyList:
			i.draw(screen)

			delBulletList = []

			k = 0
			for j in i.bulletList:
				j.draw(screen)

				# 记录已经移动到屏幕外边的子弹下标
				if j.y>890:
					delBulletList.append(k)
				k+=1

			# 以下代码,把已经移动到屏幕外边的子弹给删除掉
			for m in delBulletList:
				del i.bulletList[m]

		cls.hero.draw(screen)
		k = 0
		delBulletList = []
		for j in cls.hero.bulletList:
			j.draw(screen)
			if j.y<0:
				delBulletList.append(k)
			k+=1
		# 以下代码,把已经移动到屏幕外边的子弹给删除掉
		for m in delBulletList:
			del cls.hero.bulletList[m]


	@classmethod
	def gameInit(cls):
		cls.showMenu()
		cls.getMenuNum()
		cls.createEnemys()
		cls.createHero()

	@classmethod
	def heroPlaneKey(cls, keyValue):
		cls.hero.keyHandle(keyValue)

	@classmethod
	def shoot(cls):
		for i in cls.g_enemyList:
			i.shoot()


if __name__ == '__main__':

	
	pygame.init()

	screen = pygame.display.set_mode((480,890),0,32)

	bgImageFile = './image/background.png'

	background = pygame.image.load(bgImageFile).convert()

	pygame.display.update()


	# 1. 初始化飞机
	GameInit.gameInit()


	while True:

		screen.blit(background,(0,0))

		#判断是否是点击了退出按钮
		for event in pygame.event.get():
			# print(event.type)
			if event.type == QUIT:
				exit()
			elif event.type == KEYDOWN:
				if event.key == K_a or event.key == K_LEFT:
					print('left')
					GameInit.heroPlaneKey('left')
				
				elif event.key == K_d or event.key == K_RIGHT:
					print('right')
					GameInit.heroPlaneKey('right')

				elif event.key == K_SPACE:
					print('space')
					GameInit.heroPlaneKey('space')


		#敌人发射导弹
		GameInit.shoot()

		#更新敌人的位置
		GameInit.setXY()
		GameInit.draw(screen)

		#把修改位置后的图片，重新更新
		pygame.display.update()


		# time.sleep(0.05)