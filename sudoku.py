import numpy as np


class Cell():

    def __init__(self, x_coords: int, y_coords : int):
        self.y_coords = y_coords
        self.value : int = 0
        self.x_coords = x_coords
        self.group : int = ((x_coords//3) * 3) + y_coords//3
        self.possible_values = [1,2,3,4,5,6,7,8,9]

    def __str__(self) -> str:
        return f'value={self.value},x= {self.x_coords}, y={self.y_coords}'

    def __repr__(self) -> str:
        return self.__str__()
