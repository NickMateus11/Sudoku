import argparse


def create_template_file(base_dim, filename): # names must match parser tags
    if filename is None:
        filename = f'example_{base_dim}x{base_dim}.txt'
    with open(filename, 'w') as new_file:
        one_row = f'{"* "*base_dim}{" "*base_dim}'*base_dim + '\n'
        group_row = one_row * base_dim + '\n'
        whole_board = group_row * base_dim
        new_file.write(whole_board)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Creates file with a sudoku template of some given base dimension')
    parser.add_argument('base_dim', type=int, help='Dimension to base grid size on')
    parser.add_argument('-f', '--filename', type=str, default=None, help='Filename to write to (default: example_{n}x{n}.txt)')
    
    kwargs = vars(parser.parse_args())
    create_template_file(**kwargs)