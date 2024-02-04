import pygame as pg
import sys
import random
from maniacCaracters import Player, Obstacle, obstList, Sheep, sheepList, Ghost, ghostList

# Konstanter
WIDTH = 800  # Bredden til vinduet
HEIGHT = 600 # Høyden til vinduet
screen = pg.display.set_mode((WIDTH, HEIGHT))
# Størrelsen til vinduet
SIZE = (WIDTH, HEIGHT)

# Frames Per Second (bilder per sekund)
FPS = 60

# Farger (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHTBLUE = (100, 100, 255)
GREY = (142, 142, 142)
LIGHTRED = (255, 100, 100)


# Initiere pygame
pg.init()

# Lager en overflate (surface) vi kan tegne på
surface = pg.display.set_mode(SIZE)

# Lager en klokke
clock = pg.time.Clock()


# Variabel som styrer om spillet skal kjøres
run = True


# Henter font
font = pg.font.SysFont("Arial", 32)

# Funksjon som viser tekst på skjermen
def displayText(text):
    textImg = font.render(text, True, BLACK)
    surface.blit(textImg, (10, 10))

player = Player(30, 300, screen)
# Spill-løkken
while run:
    # Sørger for at løkken kjører i korrekt hastighet
    clock.tick(FPS)
    
    surface.fill(GREY)
    pg.draw.rect(surface, BLACK, [100,0,WIDTH-200,HEIGHT])
        
    for obstacle in obstList:
        obstacle.draw(screen)
    
    for sheep in sheepList:
        sheep.draw(screen)
        if player.rect.colliderect(sheep.shp) and player.encumbered == True:
            run = False
        
    for ghost in ghostList:
        ghost.draw(screen)
        if player.rect.colliderect(ghost.ghst):
            run = False

    player.draw(screen)
    player.move(WIDTH, HEIGHT)

    displayText(f"{player.score}")
    
    # Går gjennom hendelser (events)
    for event in pg.event.get():
        # Sjekker om vi ønsker å lukke vinduet
        if event.type == pg.QUIT:
            run = False # Spillet skal avsluttes
    

    # "Flipper" displayet for å vise hva vi har tegnet
    pg.display.flip()
    


# Avslutter pygame
pg.quit()
#sys.exit() # Dersom det ikke er tilstrekkelig med pg.quit()