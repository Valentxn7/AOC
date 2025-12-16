import math


class box:
    def __init__(self, x: int, y: int, z: int):
        from junction_class import junction
        self.x: int = x
        self.y: int = y
        self.z: int = z
        self.connected: bool = False
        self.junction: junction | None = None

    def distance(self, other_box):
        return math.sqrt((self.x - other_box.x) ** 2 + (self.y - other_box.y) ** 2 + (self.z - other_box.z) ** 2)

    def is_solitaire(self):
        return self.junction is None or self.junction.taille() == 1

    def __repr__(self):
        return f"<box x={self.x}, y={self.y}, z={self.z}>"
