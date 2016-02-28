"""Exercise 3.3, p.27"""
# At this point in the book, neither return statements nor looping have
# been introduced, so they cannot be used in this solution.

BEAM_ROW = '+ ' + '- ' * 4
ROW = '| ' + '  ' * 4

def do_two(func, arg):
    func(arg)
    func(arg)

def do_four(func, arg):
    do_two(func, arg)
    do_two(func, arg)

def print_row(n, row_string, row_end):
    print(row_string * n, row_end, sep='')

def print_beam_row(n):
    print_row(n, BEAM_ROW, '+')

def print_standard_row(n):
    print_row(n, ROW, '|')

def print_grid_row(n):
    print_beam_row(n)
    do_four(print_standard_row, n)

def print_2_by_2_grid():
    do_two(print_grid_row, 2)
    print_beam_row(2)

def print_4_by_4_grid():
    do_four(print_grid_row, 4)
    print_beam_row(4)

if __name__ == "__main__":
    print_4_by_4_grid()
    print()
    print_2_by_2_grid()
