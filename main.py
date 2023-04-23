import time

# Grids 1-4 are 2x2
grid1 = [
    [1, 0, 4, 2],
    [4, 2, 1, 3],
    [2, 1, 3, 4],
    [3, 4, 2, 1]]

grid2 = [
    [1, 0, 4, 2],
    [4, 2, 1, 3],
    [2, 1, 0, 4],
    [3, 4, 2, 1]]

grid3 = [
    [1, 0, 4, 2],
    [4, 2, 1, 0],
    [2, 1, 0, 4],
    [0, 4, 2, 1]]

grid4 = [
    [1, 0, 4, 2],
    [0, 2, 1, 0],
    [2, 1, 0, 4],
    [0, 4, 2, 1]]

grid5 = [
    [1, 0, 0, 2],
    [0, 0, 1, 0],
    [0, 1, 0, 4],
    [0, 0, 0, 1]]

grid6 = [
    [0, 0, 6, 0, 0, 3],
    [5, 0, 0, 0, 0, 0],
    [0, 1, 3, 4, 0, 0],
    [0, 0, 0, 0, 0, 6],
    [0, 0, 1, 0, 0, 0],
    [0, 5, 0, 0, 6, 4]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2)]
'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''


def check_section(section, n):
    print('called check_section')
    if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n + 1)]):
        return True
    return False


def get_squares(grid, n_rows, n_cols):
    print('called get_squares')
    squares = []
    for i in range(n_cols):
        rows = (i * n_rows, (i + 1) * n_rows)
        for j in range(n_rows):
            cols = (j * n_cols, (j + 1) * n_cols)
            square = []
            for k in range(rows[0], rows[1]):
                line = grid[k][cols[0]:cols[1]]
                square += line
            squares.append(square)
    return squares


def get_square(grid, n_rows, n_cols, row, col):
    print('called get_square')
    i = row // n_rows
    j = col // n_cols
    rows = (i * n_rows, (i + 1) * n_rows)
    cols = (j * n_cols, (j + 1) * n_cols)
    square = []
    for k in range(rows[0], rows[1]):
        line = grid[k][cols[0]:cols[1]]
        square += line
    return square


def find_empty(grid):
    print('called find_empty')
    '''
    This function returns the index (i, j) to the first zero element in a sudoku grid
    If no such element is found, it returns None

    args: grid
    return: A tuple (i,j) where i and j are both integers, or None
    '''

    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            col = []
            if grid[i][j] == 0:
                for k in grid:
                    col.append(k[j])
                return (i, j, row, col)
    return None


class empty_atts:
    def __init__(self, i, j, possible_numbers):
        self.i = i
        self.j = j
        self.possible_numbers = possible_numbers


dict_numbers = {}
empty_obj_list = []

def sort_list(obj):
    return len(obj.possible_numbers)
def possible_vals(grid, n_rows, n_cols):
    local_grid = grid
    print('called possible_vals')
    a = 0
    while find_empty(local_grid):
        i, j, row_atts, col_atts = find_empty(local_grid)
        square_atts = get_square(grid, n_rows, n_cols, i, j)
        all_atts = row_atts + col_atts + square_atts
        possible_numbers = []
        for cycle in range(1, (n_rows * n_cols)):
            if cycle in all_atts:
                pass
            else:
                possible_numbers.append(cycle)
        empty_obj_list.append(empty_atts(i, j, possible_numbers))
        local_grid[i][j] = -1
    sorted_vals = sorted(empty_obj_list, key=sort_list)
    return sorted_vals

"""
def sorted_possible_vals(grid, n_rows, n_cols):
    dict_numbers = possible_vals(grid, n_rows, n_cols)
    sorted_atts = sorted(dict_numbers.values(), key=lambda x: len(x.possible_numbers))
    return sorted_atts
"""
cycle_number = 0

def solver(grid, n_rows, n_cols):
    empty = find_empty(grid)
    print(type(grid))
    if not empty:
        if check_solution(grid, n_rows, n_cols):
            return grid
        else:
            return None

    print('called solver')


    cycle_number = 0
    possible_numbers = sorted_vals_global[cycle_number].possible_numbers
    print(sorted_vals_global[cycle_number].possible_numbers)
    i = sorted_vals_global[cycle_number].i
    j = sorted_vals_global[cycle_number].j
    for chosen_number in possible_numbers:
        print('chosen number is ', chosen_number)
        # Place the value into the grid
        grid[i][j] = chosen_number
        print(grid)
        # Recursively solve the grid
        cycle_number =+ 1
        ans = solver(grid, n_rows, n_cols)
        if ans:
            cycle_number = 0
            return ans
         # If we couldn't find a solution, that must mean this value is incorrect.
         # Reset the grid for the next iteration of the loop
        grid[row][col] = 0





# To complete the first assignment, please write the code for the following function
def check_solution(grid, n_rows, n_cols):
    print('called check_solution')
    '''
    This function is used to check whether a sudoku board has been correctly solved
    args: grid - representation of a suduko board as a nested list.
    returns: True (correct solution) or False (incorrect solution)
    '''
    n = n_rows * n_cols

    for row in grid:
        if check_section(row, n) == False:
            return False

    for i in range(n_rows ** 2):
        column = []
        for row in grid:
            column.append(row[i])

        if check_section(column, n) == False:
            return False

    squares = get_squares(grid, n_rows, n_cols)
    for square in squares:
        if check_section(square, n) == False:
            return False

    return True



def solve(grid, n_rows, n_cols):
    sorted_vals_global = possible_vals(grid, n_rows, n_cols)
    '''
    Solve function for Sudoku coursework.
    Comment out one of the lines below to either use the random or recursive solver
    '''

    # return random_solve(grid, n_rows, n_cols)
    return solver(grid, n_rows, n_cols)


'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''


def main():
    points = 0

    print("Running test script for coursework 1")
    print("====================================")

    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        print("Solving grid: %d" % (i + 1))
        start_time = time.time()
        solution = solve(grid, n_rows, n_cols)
        elapsed_time = time.time() - start_time
        print("Solved in: %f seconds" % elapsed_time)
        print(solution)
        if check_solution(solution, n_rows, n_cols):
            print("grid %d correct" % (i + 1))
            points = points + 10
        else:
            print("grid %d incorrect" % (i + 1))

    print("====================================")
    print("Test script complete, Total points: %d" % points)


if __name__ == "__main__":
    main()
