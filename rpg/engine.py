import pygame
from player import player as P

pygame.init()

screen = pygame.display.set_mode((500,500))

background = pygame.image.load("images/bg.png")

pygame.display.set_caption("Rpg")

playingGame = True

p1 = P("bobby", "spellsword", screen)

def redraw():
    screen.blit(background, (0,0))
    p1.draw()
    pygame.display.update()


while playingGame:

    pygame.time.delay(50)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            playingGame = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        p1.moveY(-5)
    elif keys[pygame.K_a]:
        p1.moveX(-5)
    elif keys[pygame.K_s]:
        p1.moveY(5)
    elif keys[pygame.K_d]:
        p1.moveX(5)


    redraw()

pygame.quit()
