import pygame
from obstacle import platform as plat
from player import player as P


pygame.init()

SCREEN_W = 600
SCREEN_H = 600

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

background = pygame.image.load("images/bg.png")

pygame.display.set_caption("Rpg")

playingGame = True

p1 = P("bobby", "spellsword", screen)
obstacles = []
obstacles.append(plat("platform 1 is a baby", 200, 500, screen))

def redraw():
	screen.blit(background, (0,0))
	for o in obstacles:
		o.draw()
	p1.draw()
	pygame.display.update()

	
def checkCollisions(thing1, thing2):
	if(abs(thing1.x - thing2.x) < 25 and abs(thing1.y - thing2.y < 25)):
		return True
	else:
		return False
	

def physics():
	p1.move()
	if p1.dx > 0:
		p1.dx -= 2
	elif p1.dx < 0:
		p1.dx += 2
	else:
		p1.setdX(0)
	for o in obstacles:
		if checkCollisions(p1, o):
			p1.setdY(0)
			p1.setOnPlatform(True)
			p1.isJumping = False
			p1.doubleJump = False
	if p1.getY() < 400 and p1.onPlatform != True:
		p1.changeY(10) 
	else:
		p1.isJumping = False
		p1.doubleJump = False
		p1.setdY(0)
		p1.setY(400)
	

while playingGame:

	clock.tick(30)

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			playingGame = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_a]:
		p1.changeX(-4)
	if keys[pygame.K_d]:
		p1.changeX(4)
	if keys[pygame.K_SPACE] and p1.isJumping != True:
		p1.changeY(-60)
		p1.setLastJump(pygame.time.get_ticks())
		p1.isJumping = True
	elif keys[pygame.K_SPACE] and p1.isJumping == True and p1.doubleJump == False and (pygame.time.get_ticks()- p1.timeSinceJump > 200):
		p1.changeY(-60)
		p1.doubleJump = True
	physics()
	redraw()

pygame.quit()

