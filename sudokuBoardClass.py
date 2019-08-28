from cellClass import Cell
import math
import random
class Board:
    def __init__(self, init_vals):
        if not math.sqrt(len(init_vals)).is_integer():
            raise ValueError
        self.nums_per_line = int(math.sqrt(len(init_vals)))
        self.base_dim = int(math.sqrt(self.nums_per_line))
        self.cells = [Cell(val) for val in init_vals]

        self.number_spacing = 2
        self.horizontal_spacing = (self.number_spacing + 1) * (self.base_dim + 1) - 1

    def get_all_cell_vals(self):
        return [cell.value for cell in self.cells]

    def draw_board(self):
        iter_cells = iter(self.get_all_cell_vals())
        self.h_segment = f'+{"-"*self.horizontal_spacing}'*self.base_dim + '+'
        for _ in range(self.base_dim):
            print(self.h_segment)
            for _ in range(self.base_dim):
                print(self.__inject_grid_row(iter_cells))
        print(self.h_segment)
    
    def __inject_grid_row(self, iter_vals):
        row = '|'
        for i in range(1, self.nums_per_line + self.base_dim + 1):
            if i%(self.base_dim+1) == 0:
                insert_char = '|'
            else:
                insert_char = next(iter_vals)
                if insert_char is None:
                    insert_char = ' '
            row += f'{" "*self.number_spacing}{insert_char}'
        return row

pool = [1,2,3,4,5,6,7,8,9] + [None]*9
a = [pool[random.randint(0,len(pool)-1)] for _ in range(81)]
g = Board(a)
g.draw_board()

# a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] * 16
# g = grid(4, a)
'''
[1 2 3  4 5 6  7 8 9 
 1 2 3  4 5 6  7 8 9 
 1 2 3  4 5 6  7 8 9 
 
 1 2 3  4 5 6  7 8 9 
 1 2 3  4 5 6  7 8 9 
 1 2 3  4 5 6  7 8 9 

 1 2 3  4 5 6  7 8 9 
 1 2 3  4 5 6  7 8 9 
 1 2 3  4 5 6  7 8 9]

[[1,2,3,1,2,3,1,2,3],[4,5,6,4,5,6,4,5,6],[7,8,9,7,8,9,7,8,9],
 [1,2,3,1,2,3,1,2,3],[4,5,6,4,5,6,4,5,6],[7,8,9,7,8,9,7,8,9],
 [1,2,3,1,2,3,1,2,3],[4,5,6,4,5,6,4,5,6],[7,8,9,7,8,9,7,8,9]]


[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]



'''

