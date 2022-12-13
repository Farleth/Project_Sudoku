valid_grid = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [9, 1, 2, 3, 4, 5, 6, 7, 8],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 2, 3, 4]]

def is_grid_valid(grid):
    for line in grid:
            if not len(set(line)) == 9:
                return False

    for x in range(9):
        column = []
        for y in range(9):
            column.append(grid[x][y])
        if not len(set(column)) == 9:
            return False

    for x_index in [0, 3, 6]:
        for y_index in [0, 3, 6]:
            subgrid = []
            for x in range(0, 3):
                for y in range(0, 3):
                    if grid[x + x_index][y + y_index] in subgrid:
                        return False
                    subgrid.append(grid[x_index + x][y_index + y])
    return True
