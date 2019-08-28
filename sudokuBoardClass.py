from cellClass import Cell
import math

class Board:
    def __init__(self, init_vals, expand=False):
        if not (len(init_vals)**0.25).is_integer() or (len(init_vals)**0.25) >= 4:
            raise ValueError

        self.nums_per_line = int(math.sqrt(len(init_vals)))
        self.base_dim = int(math.sqrt(self.nums_per_line))
        self.cells = [Cell(val) for val in init_vals]

        self.number_spacing = 2 if expand else 1
        self.horizontal_spacing = (self.number_spacing + 1) * (self.base_dim + 1) - 1

    def get_cell_vals_list(self):
        return [cell.value for cell in self.cells]

    def draw_board(self):
        iter_cells = iter(self.get_cell_vals_list())
        self.h_segment = f'+{"-"*self.horizontal_spacing}'*self.base_dim + '+'
        for _ in range(self.base_dim):
            print(self.h_segment)
            for _ in range(self.base_dim):
                print(self.__inject_cell_vals(iter_cells))
        print(self.h_segment)
    
    def __inject_cell_vals(self, iter_vals):
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

