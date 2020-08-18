import pygame

imageBaby = pygame.image.load("images/babycryingS.png")

class platform(object):

	def __init__(self, name, x, y, surface):

		self.name = name
		self.image = imageBaby
		self.surface = surface
		self.x = x
		self.y = y
		self.width = 60
		self.height = 60
		self.dx = 0
		self.dy = 0

	def draw(self):
		self.surface.blit(self.image, (self.x,self.y))
		pygame.draw.rect(self.surface, (255,0,0), (self.x, self.y, self.width, self.height), 2)

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
		
	def changeY(self, deltay):
		self.dy = deltay
	
	def changeX(self, deltax):
		self.dx = deltax
		
	def move(self):
		self.moveX()
		self.moveY()