from sudokuBoardClass import Board
import random
import math


def create_sudoku_from_file(filename):
    with open(filename, 'r') as raw_text:
        contents = raw_text.readlines()
    linearized_list = []
    for i in range(len(contents)):
        stripped_line = contents[i].strip().replace(' ', '')
        linearized_list += [(int(val) if (val is not '*' and val is not '0') else None) for val in stripped_line]
    return Board(linearized_list)
    
def solve(board):
    while(Board.is_valid_board(board)):
        return True

folder = 'puzzles/'
sudoku_file = 'example_3x3.txt'

s = create_sudoku_from_file(folder+sudoku_file)

response = None
moves = 0
s.draw_board()
while response is None:
    response = s.make_move()
    s.draw_board()
    moves+=1
print(moves-1)
