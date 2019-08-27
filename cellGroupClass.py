from cellClass import Cell

class CellGroup:
    def __init__(self, num_cells, init_vals=None):
        if num_cells <= 0:
            raise ValueError
        self.num_cells = num_cells
        if init_vals is None:
            self.cells = [Cell()] * self.num_cells
        else:
            self.cells = [Cell(val) for val in init_vals]


    def list_cell_nums(self):
        return [cell.value for cell in self.cells]

    