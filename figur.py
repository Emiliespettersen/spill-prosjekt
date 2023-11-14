import pygame

class Figur ():
    def __init__(self, bildesti: str) -> None:
        self.bilde = pygame.image.load(bildesti).convert_alpha()
        self.ramme = self.bilde.get_rect()
        self.liv = 0
        self.navn = "d"
    
    def tegn(self, vindu: pygame.Surface):
        vindu.blit(self.bilde, self.ramme)

    def skyt(self):
        pass

    def dø(self):
        pass