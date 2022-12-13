import numpy as np


class Cell():

    def __init__(self, x_coords: int, y_coords : int):
        self.y_coords = y_coords
        self.value : int = 0
        self.x_coords = x_coords
        self.group : int = ((y_coords//3) * 3) + x_coords//3
        self.possible_values = [1,2,3,4,5,6,7,8,9]

    def __str__(self) -> str:
        return f'{self.group}'

    def __repr__(self) -> str:
        return self.__str__()
