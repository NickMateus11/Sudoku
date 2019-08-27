import cell_group_class

class grid:
    def __init__(self, dim, init_vals=None):
        if dim <= 0:
            raise ValueError
        self.dim = dim
        self.groups = [cell_group_class.cell_group(self.dim, init_vals)] * self.dim

    def linearize_cell_nums(self):
        val_list = []
        for group in self.groups:
            val_list += group.list_cell_nums()
        return val_list

