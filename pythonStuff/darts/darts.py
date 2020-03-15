import pygame


from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

gameDisplay = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Darts V1.0')

clock = pygame.time.Clock()

gameOver = False

class board:

    path = 'board.png'
    bwidth = 200
    bheight = 200
    image = pygame.image.load(path)
    sizedImage = pygame.transform.scale(image, (bwidth,bheight))

    def __init__(self, width = 200, height = 200):
        self.bwidth = width
        self.bheight = height
    
    def display(self,x,y):
        gameDisplay.blit(self.sizedImage, (x,y))

    
gameBoard = board()

offsetW = (SCREEN_WIDTH/2) - gameBoard.bwidth/2
offsetH = (SCREEN_HEIGHT/2)- gameBoard.bheight/2

    
while not gameOver:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
                gameOver = True


    pygame.display.update()

    gameBoard.display(offsetW, offsetH)

    clock.tick(60)

pygame.quit()
quit()
