import numpy as np


class Cell:

    def __init__(self, x_coords: int, y_coords : int):
        self.y_coords = y_coords
        self.value : int = 0
        self.x_coords = x_coords
        self.group : int = ((x_coords//3) * 3) + y_coords//3

    def __str__(self) -> str:
        return print(self.value)
