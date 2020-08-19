import pygame

image = pygame.image.load('images/rpgGuyS.png')

class player(object):

	def __init__(self, name, path, surface, h, f, speed, jump):

		self.name = name
		self.path = path
		self.image = image
		self.surface = surface
		self.x = 50
		self.y = 50
		self.width = 60
		self.height = 64
		self.dx = 0
		self.dy = 0
		self.isJumping = False
		self.doubleJump = False
		self.timeSinceJump = 0
		self.onPlatform = False
		self.hasPlatform = False
		self.screenH = h
		self.myBottom = h
		self.collisionFunction = f
		self.speed = speed
		self.jump = jump
		
	def setPlatform(self, plat):
		self.platform = plat
		self.hasPlatform = True
		self.myBottom = self.platform.y
	
	def setOnPlatform(self, bool):
		self.onPlatform = bool
		
	def setLastJump(self, time):
		self.timeSinceJump = time

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
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
	def changeY(self, deltay):
		self.dy += deltay
	
	def changeX(self, deltax):
		self.dx += deltax
		
	def move(self):
		self.moveX()
		self.moveY()
		
	def physics(self):
		

		self.move()
	
		if self.hasPlatform:
			if self.collisionFunction(self, self.platform) != True:
				self.hasPlatform = False
				self.onPlatform = False
				self.myBottom = self.screenH
		#elif self.y < myBottom-self.height and self.onPlatform and self.hasPlatform:
		#	if checkCollisions(self, self.platform) == False:
		#		self.onPlatform = False
		#		self.hasPlatform = Fals
		
		#VERTICAL MOVEMENT PHYSICS
		if self.y < self.myBottom-self.height and self.onPlatform != True:
			self.changeY(10)
		elif self.y < self.myBottom-self.height and self.hasPlatform:
			self.changeY(10)
		else:
			self.isJumping = False
			self.doubleJump = False
			self.setdY(0)
			self.setY(self.myBottom-self.height)
	
		#MOVEMENT CODE FOR HORIZONTAL DIRECTION
		if self.dx > 0:
			self.dx -= self.speed
		elif self.dx < 0:
			self.dx += self.speed
		else:
			self.setdX(0)
			
		