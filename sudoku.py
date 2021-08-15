import time
import copy
start = time.time()

OKBLUE = '\033[94m'
OKGREEN = '\033[32m'
FAIL = '\033[91m'
ENDC = '\033[0m'

class solve_board:
    def __init__(self, board):
        self.board = board
        self.originalboard = copy.deepcopy(board)
        self.subtract_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def board_to_data(self):
        for num_row, row in enumerate(board):
            for num_square, square in enumerate(row):
                if square == 0:
                    self.board[num_row][num_square] = set(self.subtract_set)
                elif type(square) == int:
                    self.board[num_row][num_square] = {square,}
                else:
                    raise ValueError(f'Incorrect character inserted in row {num_row} in column {num_square}')
    def check_row(self, num_row):
        n = []
        for square in self.board[num_row]:
            if len(square) == 1:
                n.append(next(iter(square)))
        return n

    def check_column(self, num_col):
        column = []
        for row in self.board:
            if len(row[num_col])  == 1:
                column.append(next(iter(row[num_col])))
        return column

    def check_cage(self, num_row, num_col):
        cage = []
        l = [3*(num_col//3), 3*(num_row//3)]
        for col_l in [l[0], l[0]+1, l[0]+2]:
            for row_l in [l[1], l[1]+1, l[1]+2]:
                if len(self.board[row_l][col_l]) == 1:
                    cage.append(next(iter(self.board[row_l][col_l])))
        return cage

    def check_option(self):
        counter = 0
        for num_row, row in enumerate(self.board):
            for num_col, square in enumerate(row):

                if len(square) > 1:
                    exist = set(self.check_row(num_row)) | set(self.check_column(num_col)) | set(self.check_cage(num_row, num_col))
                    before = len(square)
                    square-=exist
                    if len(square) < before:
                        counter += 1
                if len(square) == 0:
                    raise RuntimeError("Cannot solve board")
        if counter == 0:
            return False
        return True

    def print_board(self):
        for num_row, row in enumerate(self.board):
            print("\n--+---+---+---+---+---+---+---+---|")
            for num_col, square in enumerate(row):
                options = list(square)
                if len(options) == 1 :
                    if self.originalboard[num_row][num_col] == 0:
                        print(OKGREEN + str(square)[1] +  ENDC , end='')
                    else:
                        print(str(square)[1], end='')
                print( ' | ', end='')
        print("\n--+---+---+---+---+---+---+---+---|")

    def solve(self):
        while self.check_option():
            pass


    def find_min_option(self):
        min_l = (0,0)
        min_v = range(100)
        for num_row, row in enumerate(board):
            for num_col,col  in enumerate(row):
                num_options = len(self.board[num_row][num_col])
                if num_options < len(min_v) and num_options > 1:
                    min_l = (num_row, num_col)              #tuple  E.G. (0,3)
                    min_v = self.board[num_row][num_col]    #set  E.G. {1,4}
        return min_l

    def check_solved(self):
        for row in board:
            for square in row:
                if len(square) != 1:
                    return False
        return True

    def solve_hard_sudoku(self):
        self.solve()
        if self.check_solved():
            return True
        else:
            min_l = self.find_min_option()
            options = copy.deepcopy(self.board[min_l[0]][min_l[1]])
            if len(options) == 1:
                return True
            for val in options:
                former_board = copy.deepcopy(self.board)
                self.board[min_l[0]][min_l[1]] = {val,}
                try:
                    if self.solve_hard_sudoku():
                        return True
                except RuntimeError:
                    pass
                self.board = former_board
        return False

board =[[7,6,2,0,9,3,0,1,0],
        [8,0,0,0,7,0,0,3,6],
        [5,3,9,0,6,0,7,2,0],
        [0,2,1,6,0,0,0,0,5],
        [3,0,0,4,0,9,1,0,0],
        [6,0,0,0,1,2,0,9,0],
        [0,0,0,5,0,0,4,0,3],
        [2,5,0,7,0,1,0,0,0],
        [0,7,8,0,0,0,2,0,0]]

board =[[0,0,0,3,0,0,0,2,0],
        [0,0,0,9,1,8,0,3,0],
        [9,0,7,0,0,0,0,6,0],
        [7,0,6,0,0,0,0,0,0],
        [0,0,0,4,5,0,0,0,2],
        [0,0,0,0,0,0,8,9,4],
        [3,1,0,0,0,0,0,0,0],
        [2,0,0,6,0,9,5,0,0],
        [6,0,0,0,0,3,7,0,9]]

board =[[6,0,0,0,0,4,0,0,0],
        [0,7,3,0,0,0,9,0,0],
        [0,4,0,8,3,0,0,5,7],
        [0,3,0,0,4,7,0,0,0],
        [7,0,0,1,0,9,0,0,4],
        [0,0,0,3,5,0,0,1,0],
        [4,8,0,0,1,5,0,2,0],
        [0,0,2,0,0,0,5,7,0],
        [0,0,0,2,0,0,0,0,1]]

board =[[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

board =[[7,0,0,0,0,0,0,0,5],
        [1,0,0,0,0,8,0,0,0],
        [6,0,0,7,5,2,4,0,3],
        [0,7,8,5,3,0,0,0,0],
        [0,0,0,0,0,0,3,6,0],
        [0,0,0,2,4,9,0,5,0],
        [0,4,0,6,0,3,1,9,0],
        [0,2,0,4,7,0,0,0,0],
        [0,1,0,0,2,0,0,0,0]]

sudoku = solve_board(board)
sudoku.board_to_data()
sudoku.solve_hard_sudoku()
sudoku.print_board()

print(OKBLUE + '\n\nThat took' , time.time() - start , 'seconds!\n' + ENDC)
