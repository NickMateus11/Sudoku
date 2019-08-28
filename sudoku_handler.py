from sudokuBoardClass import Board
import random
import math


def create_sudoku_from_file(filename):
    with open(filename, 'r') as raw_text:
        contents = raw_text.readlines()
    linearized_list = []
    for i in range(len(contents)):
        if len(contents[i]) == 0: # blank line
            continue
        stripped_line = contents[i].strip().replace(' ', '')
        linearized_list += [(int(val) if val is not '*' else None) for val in stripped_line]
    return Board(linearized_list) # validation?
    
g1 = create_sudoku_from_file('example_3x3.txt')
g1.draw_board()

base_dim = 2

dim = base_dim ** 2
pool = list(range(1, dim+1)) + [None]*dim
a = [pool[random.randint(0,len(pool)-1)] for _ in range(base_dim**4)]
g2 = Board(a)
# g2.draw_board()