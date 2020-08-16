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
		self.dx = 0
		self.dy = 0
		self.isJumping = False
		self.doubleJump = False
		self.timeSinceJump = 0
		self.onPlatform = False
	
	def setOnPlatform(self, bool):
		self.onPlatform = bool
		
	def setLastJump(self, time):
		self.timeSinceJump = time

	def draw(self):
		self.surface.blit(self.image, (self.x,self.y))

	def moveX(self):
		self.x += self.dx

	def moveY(self):
		self.y += self.dy
		
	def setX(self, x):
		self.x = x
		
	def setY(self, y):
		self.y = y
		
	def setdX(self, dx):
		self.dx = dx
		
	def setdY(self, dy):
		self.dy = dy
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
	def changeY(self, deltay):
		self.dy += deltay
	
	def changeX(self, deltax):
		self.dx += deltax
		
	def move(self):
		if self.y >= 390:
			self.onPlatform = False
		self.moveX()
		self.moveY()