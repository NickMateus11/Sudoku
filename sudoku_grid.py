from math import sqrt
class sud_grid():
    def __init__(self, div=3, seperation=1):
        # TODO: check if div is int
        if div <= 0:
            print('Invalid dimensions')
            raise ValueError
        else:
            self.div = int(div)
            self.nums_per_line = self.div**2
            self.vertical_spacing = seperation
            self.number_spacing = self.vertical_spacing * 2
            self.horizontal_spacing = self.vertical_spacing * self.div * 3 + self.number_spacing
            print(f'{self.nums_per_line} x {self.nums_per_line} grid created!')

            self.grid = iter([1,2,3,4,5,6,7,8,9]*80)
    
    def draw_grid(self):
        for _ in range(self.div):
            print(self.horizintal_seperator())
            for _ in range(self.div*self.vertical_spacing):
                print(self.inject_grid_row())
        print(self.horizintal_seperator())

    def horizintal_seperator(self):
        h_segment = f'+{"-"*self.horizontal_spacing}'*self.div + '+'
        return h_segment
    
    def inject_grid_row(self):
        row = ['|'] + ([" "]*self.horizontal_spacing + ['|']) * self.div
        for i in range(0, ((self.number_spacing*(self.div+1)+self.div)*self.div)+(self.div+1), self.number_spacing + 1):
            if row[i] is not ' ':
                i -= 1
                continue
            row[i] = str(next(self.grid))

        return ''.join(row)

s = sud_grid()
s.draw_grid()
"""
+-----------+---------+---------+
|  1  2  3  |         |         |
|  1  2  3  |         |         |
|  1  2  3  |         |         |
+-----------+---------+---------+
| 1  2  3 |         |         |
| 3  1  6 |         |         |


+------------+------------+------------+------------+
| 2  6  3  4 |            |            |            |
| 2  6  3  4 |            |            |            |
| 2  6  3  4 |            |            |            |
| 2  6  3  4 |            |            |            |
+------------+------------+------------+------------+
|            |            |            |            |

+--------------+--------------+--------------+--------------+
|  2  6  3  4  |              |              |              |
|  2  6  3  4  |              |              |              |
|  2  6  3  4  |              |              |              |
|  2  6  3  4  |              |              |              |
+--------------+--------------+--------------+--------------+

+-----------------+-----------------+-----------------+
|   2    3    4   |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
+-----------------+-----------------+-----------------+

"""