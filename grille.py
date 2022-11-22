from sudoku import Cell

class Grille:


    def __str__(self):
        return print(Cell)



    def __init__(self):
        x=0
        y=0
        size = 9

        board = []
        for i in range(0, size*size):
            board.append(Cell(x_coords= x, y_coords=y))
            x +=1
            if x > 8:
                x = 0
                y += 1
        print(board)

Grille()
