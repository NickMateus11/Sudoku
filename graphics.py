class sud_grid():
    def __init__(self, div=3, nums=[]):
        # TODO: check if div is int
        if div <= 0:
            print('Invalid dimensions')
            raise ValueError
        else:
            self.div = int(div)
            self.nums_per_line = self.div**2
            self.vertical_spacing = 1
            self.number_spacing = self.vertical_spacing * 2
            self.horizontal_spacing = (self.number_spacing + 1) * (self.div + 1) - 1
            print(f'{self.nums_per_line} x {self.nums_per_line} grid created!')

            self.grid = iter([1,2,3,4,5,6,7,8,9]*80)
    
    def draw_grid(self):
        self.h_segment = f'+{"-"*self.horizontal_spacing}'*self.div + '+'
        for _ in range(self.div):
            print(self.h_segment)
            for _ in range(self.div*self.vertical_spacing):
                print(self.inject_grid_row())
        print(self.h_segment)
    
    def inject_grid_row(self):
        row = '|'
        for i in range(1, self.nums_per_line + self.div + 1):
            if i%(self.div+1) == 0:
                insert_char = '|'
            else:
                insert_char = next(self.grid)
            row += f'{" "*self.number_spacing}{insert_char}'
        return row

s = sud_grid(2)
s.draw_grid()