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

    path = 'darts/board.png'
    bwidth = 400
    bheight = 400
    image = pygame.image.load(path)
    sizedImage = pygame.transform.scale(image, (bwidth,bheight))

    def __init__(self, width = 400, height = 400):
        self.bwidth = width
        self.bheight = height
    
    def display(self,x,y):
        gameDisplay.blit(self.sizedImage, (x,y))
        
    def update(self, offsetW, offsetH):
        self.display(offsetW, offsetH)
        



class bar:
    value = 0
    sliderX = 0
    sliderY = 0
    data = pygame.image.load('darts/bar.png')
    slider = pygame.image.load('darts/slider.png')
    image = pygame.transform.scale(data, (300, 50))
    increasing = True
    
    def update(self):
        if self.increasing:
            if self.sliderX > 100:
                self.increasing = False
            else:
                self.sliderX += 1
        else:
            if self.sliderX < 1:
                self.increasing = True
            else:
                self.sliderX -= 1
         

    
gameBoard = board()
xInput = bar()


offsetW = (SCREEN_WIDTH/2) - gameBoard.bwidth/2
offsetH = (SCREEN_HEIGHT/2)- gameBoard.bheight/2

def update(offsetW, offsetH):
    xInput.update()
    gameDisplay.fill((0,0,0))
    gameBoard.update(offsetW, offsetH)
    gameDisplay.blit(xInput.image, (0,0))
    gameDisplay.blit(xInput.slider, (xInput.sliderX, xInput.sliderY))

   
while not gameOver:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
                gameOver = True


    pygame.display.update()

    update(offsetW, offsetH)

    clock.tick(60)

pygame.quit()
quit()
