from sudoku import Cell

class Grille:
    def __init__(self):
        self.x=0
        self.y=0
        self.board = []
        self.size = 9
        # self.values = [8, 0, 7, 0, 0, 0, 0, 0, 0,
        #                0, 3, 1, 0, 0, 2, 4, 0, 0,
        #                0, 4, 0, 0, 0, 0, 0, 5, 2,
        #                9, 6, 0, 4, 1, 0, 8, 7, 0,
        #                1, 0, 0, 7, 0, 3, 9, 2, 0,
        #                0, 0, 4, 9, 0, 8, 1, 0, 0,
        #                4, 0, 6, 1, 0, 7, 2, 3, 0,
        #                7, 5, 3, 0, 0, 0, 0, 9, 1,
        #                0, 1, 0, 0, 0, 6, 5, 0, 0]
        self.values = [8, 1, 3, 9, 2, 5, 7, 4, 6,
                       9, 5, 6, 8, 4, 7, 3, 1, 2,
                       4, 7, 2, 3, 6, 1, 8, 9, 5,
                       6, 2, 4, 7, 1, 9, 5, 3, 8,
                       7, 9, 5, 6, 3, 8, 4, 2, 1,
                       3, 8, 1, 4, 5, 2, 9, 6, 7,
                       2, 3, 8, 1, 7, 4, 6, 5, 9,
                       5, 4, 9, 2, 9, 6, 1, 7, 3,
                       1, 6, 7, 5, 9, 3, 2, 8, 4]
        self.possible_values = [*range(1,10)]

    def create_board(self):
        for i in range(0, self.size*self.size):
            self.board.append(Cell(x_coords= self.x, y_coords=self.y, value= self.values[i]))
            self.x +=1
            if self.x > 8:
                self.x = 0
                self.y += 1
        # print(self.board)

        # print(self.possible_values)
        # self.board2 = self.board.pop(Cell(x_coords=4, y_coords=2, value=6))
        # print(self.board2)
        # print(self.board)


    def sudoku_checker_lines(self):

        is_valid = []
        cell : Cell

        for i in range(0, self.size):
            current_y = i
            row = []
            for cell in self.board:
                if cell.y_coords == current_y:
                    row.append(int(cell))
            print(row)
            row.sort()
            print(row)
            is_valid.append(row == self.possible_values)
            print(is_valid)
        return is_valid

    def sudoku_checker_columns(self):
        is_valid = []
        cell : Cell


        for i in range(0, self.size):
            current_x = i
            columns = []
            for cell in self.board:
                if cell.x_coords == current_x:
                    columns.append(int(cell))
                    #print(columns)
            columns.sort()
            #print(columns)
            is_valid.append(columns == self.possible_values)
        return is_valid

    def sudoku_checker_group(self):
        is_valid = []
        cell : Cell


        for i in range(0, self.size):
            current_grp = i
            group = []
            for cell in self.board:
                if cell.groupe == current_grp:
                    group.append(int(cell))
                    #print(group)
            group.sort()
            #print(group)
            is_valid.append(group == self.possible_values)
        return is_valid


    def sudoku_checker(self):
        self.create_board()
        columns = self.sudoku_checker_columns()
        rows = self.sudoku_checker_lines()
        group = self.sudoku_checker_group()
        all_checkers = []
        for i in range(0, self.size):
            all_checkers.append(rows[i])
            all_checkers.append(columns[i])
            all_checkers.append(group[i])
        print(all_checkers)
        return all_checkers

    def count_errors(self):
        all_checkers = self.sudoku_checker()
        nbroffalse = 0
        for i in all_checkers:
            if i == False:
                nbroffalse += 1
                print(nbroffalse)
        if nbroffalse == 0:
            print("perfect grid")
            print(nbroffalse)
        else:
            print(f"There are {nbroffalse//3} errors")
            print(nbroffalse)

    # def solver(self):
    #     board = self.create_board()
    #     cell : Cell

    #     same_col = []
    #     same_group = []
    #     current_row = 0
    #     current_col = 0
    #     current_grp = 0
    #     values_to_remove = []
    #     for cell in self.board:
    #         same_row = []
    #         if cell.y_coords == current_row:
    #             same_row.append(cell)
    #             for cell in same_row:
    #                 if cell.value == 0:
    #                     same_row.remove(cell)
    #                     for cell in same_row:
    #                         values_to_remove.append(int(cell))
    #             for i in values_to_remove:
    #                 cell.possible_values.remove(i)
    #     print(cell.possible_values)
    #     print(values_to_remove)
    #     print(same_row)

        #     if cell.x_coords == current_col:
        #         same_col.append(self.board[cell])
        #     if cell.groupe == current_grp:
        #         same_group.append(self.board[cell])
        # print(same_row, same_col, same_group)

grille = Grille()
grille.count_errors()
