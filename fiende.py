from figur import Figur


class Fiende (Figur):
    def __init__(self, bildesti: str) -> None:
        super().__init__("bilder/fiende-lilla.png")
        super().__init__("bilder/fiende-gul.png")
        super().__init__("bilder/fiende-hvit.png")

    def __init__(self, bildesti: str) -> None:
        super().__init__("bilder/fiende-gul.png")