from cellClass import Cell
from functools import reduce
import math
from copy import deepcopy

class Board:
    def __init__(self, init_vals, expand=False):
        if not Board.is_valid_board(init_vals):
            raise ValueError
        self.nums_per_line = int(math.sqrt(len(init_vals)))
        self.base_dim = int(math.sqrt(self.nums_per_line))
        self.number_spacing = 2 if expand else 1
        self.horizontal_spacing = (self.number_spacing + 1) * (self.base_dim + 1) - 1

        self.cells = [Cell(val) for val in init_vals]
        self._populate_possible_cell_vals()
        self.cells_state_stack = []
        self.forked_cells_index_stack = []

    def _populate_possible_cell_vals(self):
        for cell in self.cells:
            if cell.val is None:
                cell.possible_vals = list(range(1,self.nums_per_line+1))
            else:
                cell.possible_vals = [cell.val]
        self.update_possible_cell_vals()

    def update_possible_cell_vals(self):
        for i in range(len(self.cells)):
            curr_cell = self.cells[i]
            if curr_cell.val is not None:
                continue
            temp_list = self.get_cell_vals_list()

            curr_cell.possible_vals = []
            for val in list(range(1,self.nums_per_line+1)):
                temp_list[i] = val
                if self.is_val_valid(temp_list, i) and val not in curr_cell.black_listed_vals:
                    curr_cell.possible_vals.append(val) # this is reappending the value that led to stalemate - fix this

        return [cell.possible_vals for cell in self.cells]

    def get_cell_vals_list(self):
        return [cell.val for cell in self.cells]

    def make_move(self, draw_backtracking=True):
        if self.is_win_state():
            return True
        while self.is_stalemate(): #if stuck, restore last fork
            if len(self.cells_state_stack) > 0:
                self.cells = self.cells_state_stack.pop()
                for i in range(len(self.cells)):
                    prev_cell = self.cells[i]
                    if i not in self.forked_cells_index_stack:
                        prev_cell.black_listed_vals = [] # reset blacklisted vals
                    
                error_cell_index = self.forked_cells_index_stack.pop()
                self.cells[error_cell_index].black_listed_vals.append(self.cells[error_cell_index].val)
                self.cells[error_cell_index].val = None
                    
                if draw_backtracking:
                    self.draw_board()
            else:
                return False      
      
        cell_index = self.find_cell_index_with_least_possibilties()
        current_cell = self.cells[cell_index]
        if len(current_cell.possible_vals) > 1: # Fork here
            current_cell.val = current_cell.possible_vals[0]
            self.cells_state_stack.append(deepcopy(self.cells))
            self.forked_cells_index_stack.append(cell_index)
        else: # only 1 option (can't be 0)
            current_cell.val = current_cell.possible_vals[0] # just set val
    
    def find_cell_index_with_least_possibilties(self):
        cell_val_possibilities_list = self.update_possible_cell_vals()
        smallest_len = self.nums_per_line
        index = None
        for i in range(len(cell_val_possibilities_list)):
            p_vals = cell_val_possibilities_list[i]
            if len(p_vals) > 0 and len(p_vals) < smallest_len and not self.cells[i].val:
                smallest_len = len(p_vals)
                index = i
        return index

    # ----- Stop Conditions ----- #
    def is_win_state(self):
        current_cell_values = self.get_cell_vals_list()
        return current_cell_values.count(None) is 0 and \
            Board.is_valid_board(current_cell_values)

    def is_stalemate(self):
        self.update_possible_cell_vals()
        
        return reduce(
            lambda a,b: a or b, 
            [len(cell.possible_vals) == 0 \
                for cell in self.cells]
        )
    # ----- \Stop Conditions ----- #

    # ----- Drawing ----- #
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
    # ----- \Drawing ----- #

    def is_val_valid(self, lin_cells, index):
        row = index // self.nums_per_line
        col = index % self.nums_per_line
        # group = row // self.base_dim + col // self.base_dim
        # print(index, row, col, group)

        row_list = lin_cells[row*self.nums_per_line : (row+1)*self.nums_per_line]
        if self._check_rule_violation(row_list):
            return False

        col_list = [lin_cells[r*self.nums_per_line + col] for r in range(self.nums_per_line)]
        if self._check_rule_violation(col_list):
            return False
            
        group_list = []
        group_row_offset = self.base_dim ** 3
        for i in range(self.nums_per_line): # individual group
            ind = (group_row_offset * (row//self.base_dim)) + \
                (self.base_dim * (col//self.base_dim)) + \
                i%self.base_dim + \
                (i//self.base_dim)*self.nums_per_line
            group_list.append(lin_cells[ind]) 
        if self._check_rule_violation(group_list):
            return False

        return True

    # ----- Static methods ----- # TODO: allow validation for indiv row/col/groups
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
        for group_row in range(group_width): # row of groups
            for group_col in range(group_width): # each group per row
                group_list = []
                for i in range(nums_per_group): # individual group
                    index = (group_row_offset * group_row) + \
                        (group_width * group_col) + \
                        i%group_width + \
                        (i//group_width)*nums_per_group
                    group_list.append(index) 
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
    # ----- \Static methods ----- #