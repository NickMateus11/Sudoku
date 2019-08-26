from math import sqrt
class sud_grid():
    def __init__(self, div=3, seperation=1):
        # TODO: check if div is int
        if div <= 0:
            print('Invalid dimensions')
            raise ValueError
        else:
            self.div = int(div)
            self.size = int(self.div**2)
            print(f'{self.size} x {self.size} grid created!')
            self.vertical_spacing = 1
            self.horizontal_spacing = self.vertical_spacing * 3
    
    def draw_grid(self):
        for i in range(self.div):
            print(self.horizintal_seperator())
            for j in range(self.div*self.vertical_spacing):
                print(self.vertical_seperator())
        print(self.horizintal_seperator())

    def horizintal_seperator(self):
        h_segment = f'+{"-"*self.horizontal_spacing*3}'*self.div + '+'
        return h_segment
    
    def vertical_seperator(self):
        v_segment = f'|{" "*self.horizontal_spacing*3}'*self.div + '|'
        return v_segment

s = sud_grid()
s.draw_grid()
"""
+---------+---------+---------+
| 1  2  3 |         |         |
| 3  1  6 |         |         |
| 1  2  3 |         |         |
+---------+---------+---------+
| 1  2  3 |         |         |
| 3  1  6 |         |         |
| 1  2  3 |         |         |
+---------+---------+---------+
|         |         |         |
|         |         |         |
|         |         |         |
+---------+---------+---------+

+---+
|   |
+---+

+------+
|      |
|      |
+------+
"""