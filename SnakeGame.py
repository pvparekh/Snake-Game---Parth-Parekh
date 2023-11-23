import pygame, sys, random
from pygame.math import Vector2

class SNAKE: 
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
    def draw_snake(self):
        for block in self.body:
            #create rectangle
            xpos = int(block.x*cellsize)
            ypos = int(block.y*cellsize)
            blockrect = pygame.Rect(xpos, ypos,cellsize,cellsize)
            #draw rectangle
            pygame.draw.rect(screen,(10,16,110),blockrect)
    
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]
    
    def add_block(self):
        self.new_block = True

class FRUIT:
    def __init__(self):
        self.randomize()

    def drawfruit(self):
        #create rectangle
        fruitrect = pygame.Rect(self.pos.x*cellsize, self.pos.y*cellsize,cellsize,cellsize)
        #draw rectangle
        pygame.draw.rect(screen,(125,164,115),fruitrect)

    def randomize(self):
        self.x = random.randint(0,cellnumber-1)
        self.y = random.randint(0,cellnumber-1)
        self.pos = Vector2(self.x,self.y)

class MAIN:
    def __init__(self): 
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.fruit.drawfruit()
        self.snake.draw_snake()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            #respawn the fruit
            self.fruit.randomize()
            #increase snake size
            self.snake.add_block()



pygame.init() 
cellsize = 40 
cellnumber = 20
screen = pygame.display.set_mode((cellnumber*cellsize,cellnumber*cellsize))
clock = pygame.time.Clock()



Screen_Update = pygame.USEREVENT
pygame.time.set_timer(Screen_Update,150)

main_game = MAIN()

while True: #draw all our items
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == Screen_Update:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1,0)

    screen.fill((135,220,72))
    main_game.draw_elements()
    pygame.display.update() 
    clock.tick(60)