from sudokuBoardClass import Board
import random
import math

base_dim = 2

dim = base_dim ** 2
pool = list(range(1, dim+1)) + [None]*dim
a = [pool[random.randint(0,len(pool)-1)] for _ in range(base_dim**4)]
g = Board(a)
g.draw_board()