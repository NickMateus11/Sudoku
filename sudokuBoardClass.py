from cellClass import Cell
from functools import reduce
import math

class Board:
    def __init__(self, init_vals, expand=False):
        if not Board.is_valid_board(init_vals):
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

    @staticmethod
    def is_valid_board(lin_cells):
        len_lin_cells = len(lin_cells)**0.25
        if not len_lin_cells.is_integer() or len_lin_cells >= 4:
            return False
        return Board.check_rows(lin_cells) and \
            Board.check_cols(lin_cells) and \
            Board.check_groups(lin_cells)

    @staticmethod
    def check_rows(lin_cells):
        rows = int(len(lin_cells) ** 0.5)
        for i in range(rows):
            row = lin_cells[i*rows : i*rows+rows]
            if Board._check_rule_violation(row):
                return False
        return True

    @staticmethod
    def check_cols(lin_cells):
        cols = int(len(lin_cells) ** 0.5)
        for i in range(cols):
            col = [lin_cells[row*cols + i] for row in range(cols)]
            if Board._check_rule_violation(col):
                return False
        return True

    @staticmethod
    def check_groups(lin_cells):
        nums_per_group = int(len(lin_cells) ** 0.5)
        group_width = int(nums_per_group ** 0.5)
        group_row_offset = group_width ** 3
        for row in range(group_width): # row of groups
            for col in range(group_width): # each group per row
                group_list = []
                for i in range(nums_per_group): # individual group
                    index = (group_row_offset * row) + (group_width * col) + i%group_width + (i//group_width)*nums_per_group
                    group_list.append(lin_cells[index]) 
                if Board._check_rule_violation(group_list):
                    return False
        return True

    @staticmethod
    def _check_rule_violation(val_list): # no violations are present
        track_dict = {val: val_list.count(val) for val in range(1,len(val_list)+1)}
        return reduce(
            lambda a,b: a or b, 
            [count is None or count > 1 for count in track_dict.values()]
        )