import pygame as pg
import random
WIDTH = 800  # Bredden til vinduet
HEIGHT = 600 # Høyden til vinduet
screen = pg.display.set_mode((WIDTH, HEIGHT))

class Player():
    def __init__(self, x, y, surface):
        self.rect = pg.Rect((x, y, 40, 40))
        self.surface = surface
        self.encumbered = False
        self.speed = 10
        self.score = 0
        
        
        
    def draw(self, surface):
        pg.draw.rect(surface, (255, 0, 0), self.rect)
        
    
    def move(self, screen_width, screen_height):
        dx = 0
        dy = 0
        
        if self.encumbered == False:
            for sheep in sheepList:
                if self.rect.colliderect(sheep.shp):
                    sheepList.remove(sheep)
                    self.encumbered = True
                    
        if len(sheepList) < 3:
            self.speed = 5
        
        if self.encumbered == True and self.rect.left <= 100:
            self.encumbered = False
            sheep = generateSheep()
            obstacle = generateObst()
            ghost = generateGhost()
            self.speed = 10
            self.score += 1
            
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            dx = -self.speed
        if key[pg.K_d]:
            dx = self.speed
        if key[pg.K_w]:
            dy = -self.speed
        if key[pg.K_s]:
            dy = self.speed
        
        if self.rect.left + dx < 0 or self.rect.right + dx > screen_width:
            dx = 0
        if self.rect.top + dy < 0 or self.rect.bottom + dy > screen_height:
            dy = 0
        
        for obstacle in obstList:
            if self.rect.right + dx >= obstacle.obst.left and self.rect.left + dx <= obstacle.obst.right and self.rect.top <= obstacle.obst.bottom and self.rect.bottom >= obstacle.obst.top:
                dx = 0
            if self.rect.top + dy <= obstacle.obst.bottom and self.rect.bottom + dy >= obstacle.obst.top and self.rect.right >= obstacle.obst.left and self.rect.left <= obstacle.obst.right:
                dy = 0

            
        self.rect.x += dx
        self.rect.y += dy


class Obstacle():
    def __init__(self, x, y):
        self.obst = pg.Rect((x, y, 40, 40))
    def draw(self, surface):
        pg.draw.rect(surface, (0, 0, 255), self.obst)
        

obstList = []
def generateObst():
    obstacle = Obstacle(random.randint(100,660),random.randint(0,560))
    while any(obstacle.obst.colliderect(existing_obstacle.obst) for existing_obstacle in obstList):
        obstacle = Obstacle(random.randint(100,660),random.randint(0,560))
    obstList.append(obstacle)
    return obstacle


class Sheep():
    def __init__(self, x, y):
        self.shp = pg.Rect((x, y, 40, 40))
    def draw(self, surface):
        pg.draw.rect(surface, (200, 200, 200), self.shp)
        
sheepList = []
def generateSheep():
    sheep = Sheep(random.randint(700,760),random.randint(0,560))
    while any(sheep.shp.colliderect(existing_sheep.shp) for existing_sheep in sheepList):
        sheep = Sheep(random.randint(700,760),random.randint(0,560))
    sheepList.append(sheep)
    return sheep
    
class Ghost():
    def __init__(self, x, y, dx, dy):
        self.dx = dx
        self.dy = dy
        self.ghst = pg.Rect((x, y, 40, 40))
    def draw(self, surface):
        self.ghst.x += self.dx
        self.ghst.y += self.dy
        
        if self.dx + self.ghst.left <= 100 or self.dx + self.ghst.right >= 700:
            self.dx = -self.dx
        if self.dy + self.ghst.top <= 0 or self.dx + self.ghst.bottom >= 600:
            self.dy = -self.dy

        pg.draw.rect(surface, (255, 255, 255), self.ghst)
        
ghostList = []
def generateGhost():
    ghost = Ghost(random.randint(100,660),random.randint(0,560), random.randint(-8,8), random.randint(-8,8))
    ghostList.append(ghost)
    return ghost

ghost = generateGhost()

for i in range(3):
    obstacle = generateObst()

for i in range(3):
    sheep = generateSheep()
