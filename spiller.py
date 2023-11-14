from figur import Figur

class Spiller(Figur):
    def __init__(self, vindu_bredde: int, vindu_høyde: int) -> None:
        super().__init__("bilder/spiller.png")

        #setter spilleren i startposisjonen
        self.ramme.centerx = vindu_bredde / 2
        self.ramme.bottom = vindu_høyde
    
    def flytt(self, dx:int):
        self.ramme.x += dx

    def mist_liv ():
        pass