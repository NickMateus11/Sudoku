import cell_class

class cell_group:
    def __init__(self, num_cells, init_vals=None):
        if num_cells <= 0:
            raise ValueError
        self.num_cells = num_cells
        if init_vals is None:
            self.cells = [cell_class.cell()] * self.num_cells
        else:
            self.cells = [cell_class.cell(val) for val in init_vals]


    def list_cell_nums(self):
        return [cell.value for cell in self.cells]

    