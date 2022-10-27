

class Map():
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width
        self.quadrants = self.generate_quadrants()

    def generate_quadrants(self):
        quadrants = []
        quadrants.append()

class Quadrant():
    def __init__(self) -> None:
        self.