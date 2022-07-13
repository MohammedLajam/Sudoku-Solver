import numpy as np


def solver(sudoku, solutions):
    """
    The Conditions of Sudoku:
    This task consists of solving a 6x6 sudoku grid using python. In this variation, each 2x3 block has to contain
    uniquely the numbers from 1 to 6, in such a way that on every row and column there are no repeated numbers.
    """
    # function for creating the conditions:
    def exist(row, column, number):
        for i in range(0, 6):  # checking if the number appears in a specific row:
            if sudoku[row][i] == number:
                return False
        for i in range(0, 6):  # checking if the number appears in a specific column:
            if sudoku[i][column] == number:
                return False
        x = (column // 3) * 3  # checking if the number appears in a specific square (2 * 3):
        y = (row // 2) * 2
        for i in range(0, 2):
            for j in range(0, 2):
                if sudoku[y+i][x+j] == number:
                    return False
        return True

    # checking if the cell is empty (searching for ZEROS):
    for row in range(0, 6):
        for column in range(0, 6):
            if sudoku[row][column] == 0:
                for number in range(1, 7):
                    if exist(row, column, number):
                        sudoku[row][column] = number
                        solver(sudoku, solutions)
                        sudoku[row][column] = 0
                return
    solutions.append(np.array(sudoku))
    pass

# The Sudoku puzzle to be tested:
if __name__ == "__main__":
    s = np.array(
            [0, 0, 3, 0, 0, 0,
             5, 6, 0, 3, 2, 0,
             0, 5, 4, 2, 0, 0,
             2, 0, 6, 0, 5, 0,
             0, 1, 2, 0, 4, 0,
             0, 0, 0, 1, 0, 0]
        ).reshape([6, 6])
    print('The Sudoku puzzle')
    print(f'{s}\n')

    solutions_list = list()
    solver(s, solutions_list)
    for solution in solutions_list:
        print('One possible solution:')
        print(f'{solution}\n')

    assert len(solutions_list) == 3, "Make sure there three are solutions to the problem"
    one_solution = np.array(
            [4, 2, 3, 5, 1, 6,
             5, 6, 1, 3, 2, 4,
             1, 5, 4, 2, 6, 3,
             2, 3, 6, 4, 5, 1,
             3, 1, 2, 6, 4, 5,
             6, 4, 5, 1, 3, 2]
        ).reshape([6, 6])
    assert any(np.array_equal(sol, one_solution) for sol in solutions_list), "Make sure one of the solutions match"