class Cell:

    def __init__(self, value : int, x_coords : int, y_coords):
            self.value = value
            self.x_coords = x_coords
            self.y_coords = y_coords
            self.groupe  : int = ((y_coords//3) * 3) + x_coords//3
            self.possible_values = [*range(1,10)]

    def __str__(self) -> str:
        return f'x={self.x_coords}, y={self.y_coords}, g={self.groupe}, v={self.value}'

    def __repr__(self) -> str:
        return self.__str__()

    def __int__(self):
        return self.value

    def __index__(self):
        cellidx = self.x_coords + 9 * self.y_coords
        return cellidx

    def __getitem__(self):
        return self
