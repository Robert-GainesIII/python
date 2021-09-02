import pygame

class Jigger(pygame.sprite.Sprite):
    def __init__(self,width, height):
        self.liqW, self.liqH = 20,20
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("jigger.jpeg").convert()
        self.image = pygame.transform.scale(self.image, (width,height))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def clicked(self):
        pygame.draw.ellipse(self.image, BLUE, (self.rect.w/2-self.liqW, self.rect.h/2 - self.liqH - 10, 40, 20))
        
        

class Drink(pygame.sprite.Sprite):

    def __init__(self, ingredients, price, text, size, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.w = width
        self.h = height
        self.font = pygame.font.SysFont("Arial", size)
        self.textSurf = self.font.render(text, 1, color)
        self.textW = self.textSurf.get_width()
        self.textH = self.textSurf.get_height()
        print ("text W: {} given W: {}".format(self.textW, width))
        if self.textW > self.w:
            self.w = self.textW
        self.ingredients = []
        self.price = price
        
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/ 2)

        
        self.image.blit(self.textSurf, [self.w/2 - self.textW/2, self.h/2 - self.textH/2])

    def clicked(self):
        self.image.fill(RED)

        self.image.blit(self.textSurf, [self.w/2 - self.textW/2, self.h/2 - self.textH/2])

pygame.init()

BLACK = (0,0,0)

WHITE = (255,255,255)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
j = Jigger(100,100)
vodkaLem = Drink(["El Jimador Silver - 2oz", "Lemon Juice - 2oz", "Lemon Wedge"], 14, "Vodka Lemonade", 14, BLACK, 50,50)
all_sprites = pygame.sprite.Group()
all_sprites.add(vodkaLem)
all_sprites.add(j)
screen.fill(GREEN)

pygame.display.update()

running = True
while running:

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    ev = pygame.event.get()
    for e in ev:
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
        
            clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(pos)]

            print(clicked_sprites)
            for sprite in clicked_sprites:
                sprite.clicked()

    pygame.display.update()


#END of Program