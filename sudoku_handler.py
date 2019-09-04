from sudokuBoardClass import Board
import random
import math


def create_sudoku_from_file(filename):
    with open(filename, 'r') as raw_text:
        contents = raw_text.readlines()
    linearized_list = []
    for i in range(len(contents)):
        stripped_line = contents[i].strip().replace(' ', '')
        linearized_list += [(int(val) if val is not '*' else None) for val in stripped_line]
    return Board(linearized_list)
    
def solve(board):
    while(Board.is_valid_board(board)):
        return True

sudoku_file = 'example_3x3.txt'
s = create_sudoku_from_file(sudoku_file)
# print([cell.possible_vals for cell in s.cells])
# print(s.is_win_state())
# print(s.is_stalemate())
