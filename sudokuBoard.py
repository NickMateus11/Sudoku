from cellClass import Cell
import math
class Board:
    def __init__(self, dim, init_vals=None):
        if dim <= 0:
            raise ValueError
        self.dim = dim
        self.init_vals = init_vals
        if init_vals is None:
            self.formatted_init_vals = [[None]*(self.dim**2)]*(self.dim**2)
        else:
            self.formatted_init_vals = [list() for _ in range(self.dim**2)]
            for i in range(len(init_vals)):
                index = (i//self.dim)%self.dim + self.dim*(i//(self.dim**3))
                self.formatted_init_vals[index].append(init_vals[i])

    def get_all_cell_nums(self):
        return self.init_vals

    def get_cell_nums_rows(self):
        pass

a = [1,2,3,4,5,6,7,8,9] * 9
g = Board(3, a)

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

