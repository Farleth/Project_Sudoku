from sudoku import Cell

class Grille:

    def __init__(self, values):
        self.x=0
        self.y=0
        self.board = []
        self.size = 9
        self.values = values
        self.init_sudoku_grid()

    def init_sudoku_grid(self):
        #initialisation of the grid
        for i in range(0, self.size * self.size):
            #checking if the provided list of falues has the correct number of values
            if len(self.values) == self.size*self.size:
                #instantiating all cells in a list
                self.board.append(Cell(value=self.values[i], x_coords=self.x, y_coords=self.y))
                self.x += 1
                #not forgeting the line breaks for x and y
                if self.x == self.size:
                    self.x = 0
                    self.y += 1
            else: return f"The list of values doesn't match a sudoku grid. Please provide a list of 81 values"

    def all_unique(self, list_of_cells):
            # check that all the values in a list of cells are unique
        return len(set(list_of_cells)) == len(list_of_cells)

    def check_row(self):
        cell : Cell
        for y in range(self.size):
            row = []
            for x in range(self.size):
                cell = self.board[x + y*self.size]
                row.append(int(cell))
            if not self.all_unique(row):
                print(f"pb row at y={y}")
                return False


    def check_column(self):
        cell : Cell
        for x in range(self.size):
            column = []
            for y in range(self.size):
                cell = self.board[x + y*self.size]
                column.append(int(cell))
            if not self.all_unique(column):
                print(f"pb col at x={x}")
                return False

    def check_groups(self):
        cell : Cell
        for group in range(self.size):
            group_row = []
            for cell in self.board:
                if cell.group == group:
                    group_row.append(int(cell))
            if not self.all_unique(group_row):
                print(f"pb group at g={group}")
                return False

    def check_grid(self):
        if self.check_row() == False or self.check_column() == False or self.check_groups() == False:
            return print("your sudoku is incorrect")
        else:
            return print("your sudoku is correct")

    def display_grid(self):
        for y in range(self.size):
            for x in range(self.size):
                print(self.board[y * self.size + x].value, end=" ")
            print()

#////////////////////////////////////////////////////////////////////

    def find_empty(self):
        cell : Cell
        for cell in self.board:
            if cell.value == 0:
                return cell
        return False


    def solver_check_row(self, checking_cell : Cell):
        #check row
        cells_same_row : Cell
        for cells_same_row in self.board:
            if cells_same_row.y_coords == checking_cell.y_coords and cells_same_row.x_coords != checking_cell.x_coords and cells_same_row.value == checking_cell.value:
                return False

    def solver_check_column(self, checking_cell : Cell):
        #check column
        cells_same_column : Cell
        for cells_same_column in self.board:
            if cells_same_column.x_coords == checking_cell.x_coords and cells_same_column.y_coords != checking_cell.y_coords and cells_same_column.value == checking_cell.value:
                return False

    def solver_check_groups(self, checking_cell : Cell):
        #check group
        cells_same_group : Cell
        for cells_same_group in self.board:
            if cells_same_group.group == checking_cell.group and cells_same_group.value == checking_cell.value:
                if cells_same_group.x_coords != checking_cell.x_coords or cells_same_group.y_coords != checking_cell.y_coords:
                    return False


    def solver_check_valid(self, cell):
        if self.solver_check_row(cell) == False or self.solver_check_column(cell) == False or self.solver_check_groups(cell) == False:
            return False
        else:
            return True

    def solve(self):

        empty_cell = self.find_empty()
        if not self.find_empty():
            self.display_grid()
            return True

        for possible_num in range(1, self.size + 1):
            empty_cell.value = possible_num
            if self.solver_check_valid(empty_cell):

                if self.solve():
                    self.display_grid()
                    return True
            empty_cell.value = 0
        return False


values = [
     0, 7, 0, 0, 8, 6, 0, 0, 2,
     0, 6, 0, 4, 0, 7, 0, 0, 8,
     8, 0, 0, 9, 1, 0, 7, 0, 0,
     7, 8, 0, 0, 4, 0, 0, 0, 5,
     3, 1, 0, 8, 6, 0, 0, 0, 0,
     0, 0, 2, 7, 9, 0, 6, 0, 3,
     5, 4, 0, 6, 2, 9, 0, 0, 0,
     0, 2, 0, 1, 5, 8, 0, 4, 9,
     1, 0, 0, 0, 0, 4, 0, 0, 0
]
grid = Grille(values)

print(grid.solve())
print(grid.check_grid())
grid.display_grid()
