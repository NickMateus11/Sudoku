import sudoku_grid_class
import sudoku_grid

g = sudoku_grid_class.grid(4,[1,2,3,4]*4)
# print(g.linearize_cell_nums())
s = sudoku_grid.sud_grid(2,1,nums=g.linearize_cell_nums())
s.draw_grid()
