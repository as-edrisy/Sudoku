from copy import copy

array = []

puzzle = """9......48
.17.4...5
8....17..
.....6.8.
..8...2..
.5.3.....
..97....6
7...2.53.
52......4"""
for line in puzzle.splitlines():
    l = []
    for char in line:
        if char == '.':
            l.append(0)
        else:
            l.append(int(char))
    array.append(l)
        
array_orig = copy(array)

# Return true if n is not in row
def not_in_row(row, n):
    for i in range(9):
        if array[row][i] == n:
            return False
    return True

def not_in_column(col, n):
    for i in range(9):
        if array[i][col] == n:
            return False
    return True

def not_in_zone(row, col, n):
    zone = (row/3, col/3)
    # Top row, col of zone
    tr = zone[0]*3
    tc = zone[1]*3
    
    for r in range(3):
        for c in range(3):
            if array[tr+r][tc+c] == n:
                return False    
    return True

def valid(row, col, n):
    return not_in_row(row, n) and not_in_column(col, n) and not_in_zone(row, col, n)
def solved():
    for i in range(9):
        for j in range(9):
            if array[i][j] == 0:
                return False
    return True

def next_empty_square(row, col):
    for i in range(9):
        for j in range(9):
            if array[i][j] == 0:
                return (i, j)
    return False

def restore_value(row, col):
    array[row][col] = array_orig[row][col]

def solve(row, col):
    next_square = next_empty_square(0, 0)
    if not(next_square):
        return True
    row = next_square[0]
    col = next_square[1]
    for val in range(1, 10):
        if valid(row, col, val):
            array[row][col] = val
            if solve(row, col):
                return True
            else:
                array[row][col] = 0
    return False

def print_solution():
    for row in range(9):
        for col in range(9):
            if col % 3 == 0:
                print '|',
            print array[row][col],
        print '|',
        if row % 3 == 2:
            print
            print "-----------------------"
        else:
            print
            
    
solve(0, 0)
print_solution()
