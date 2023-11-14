import pygame
from spiller import Spiller
from fiende import Fiende

#1. oppsett
pygame.init()
BREDDE = 700
HOYDE = 600
FPS = 60

vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

spiller = Spiller (BREDDE, HOYDE)
fiende = Fiende (BREDDE)

while True:
    #2. Håndter input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    taster = pygame.key.get_pressed()
    if taster [pygame.K_LEFT]:
        spiller.flytt(-1)
    if taster[pygame.K_RIGHT]:
        spiller.flytt(1)
        
    #3. Oppdater spill
    #4. tegn
    vindu.fill("black")
    spiller.tegn(vindu)
    fiende.tegn(vindu)

    pygame.display.flip()
    klokke.tick(FPS)