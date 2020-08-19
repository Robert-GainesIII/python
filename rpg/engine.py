import pygame
from obstacle import platform as plat
from player import player as P


def checkCollisions(thing1, thing2):
	if(abs(thing1.x -thing2.x) < thing1.width and thing1.y < thing2.y):
		print("True")
		return True
	else:
		return False

pygame.init()

SCREEN_W = 1100
SCREEN_H = 600
PLAYERSPEED = 10
PLAYERJUMP = 60

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

background = pygame.image.load("images/bg.png")
	
pygame.display.set_caption("Rpg")

playingGame = True

p1 = P("bobby", "spellsword", screen, SCREEN_H, checkCollisions, PLAYERSPEED, PLAYERJUMP)
print(p1.name)
obstacles = []
obstacles.append(plat("platform 1 is a baby", 200, 300, screen))

def redraw():
	screen.blit(background, (0,0))
	for o in obstacles:
		o.draw()
	p1.draw()
	pygame.display.update()
	

def physics():
		
	for o in obstacles:
		if checkCollisions(p1, o) and p1.dx >=-1:
			p1.setPlatform(o)
			p1.setOnPlatform(True)
			break
			
	p1.physics()
	


while playingGame:

	clock.tick(30)

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			playingGame = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_a]:
		p1.changeX(-PLAYERSPEED)
	if keys[pygame.K_d]:
		p1.changeX(PLAYERSPEED)
	if keys[pygame.K_SPACE] and p1.isJumping != True:
		p1.changeY(-PLAYERJUMP)
		p1.setLastJump(pygame.time.get_ticks())
		p1.isJumping = True
	elif keys[pygame.K_SPACE] and p1.isJumping == True and p1.doubleJump == False and (pygame.time.get_ticks()- p1.timeSinceJump > 200):
		p1.changeY(-PLAYERJUMP)
		p1.doubleJump = True
	physics()
	redraw()

pygame.quit()

