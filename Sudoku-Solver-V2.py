import numpy as np


def solver(sudoku, solutions):
    """
    The Conditions of Sudoku:
    This task consists of solving a 6x6 sudoku grid using python. In this variation, each 2x3 block has to contain
    uniquely the numbers from 1 to 6, in such a way that on every row and column there are no repeated numbers.
    """
    # checking if the cell is empty (searching for ZEROS):
    for row in range(0, 9):
        for column in range(0, 9):
            if sudoku[row][column] == 0:
                for number in range(1, 10):
                    # applying sudoku conditions
                    # checking if the iterated number in a specific row, column or square (2*3)
                    x = row // 3  # 0, 0, 0, 1, 1, 1, 2, 2, 2 for every row iteration
                    y = column // 3  # 0, 0, 0, 1, 1, 1, 2, 2, 2 for every column iteration
                    if number not in sudoku[row, :] \
                        and number not in sudoku[:, column] \
                            and number not in sudoku[x * 3:(x + 1) * 3, y * 3:(y + 1) * 3]:
                        sudoku[row][column] = number
                        solver(sudoku, solutions)
                        sudoku[row][column] = 0
                return
    solutions.append(np.array(sudoku))
    pass


# The Sudoku puzzle to be tested:
if __name__ == "__main__":
    s = np.array(
        [7, 8, 0, 4, 0, 0, 1, 2, 0,
         6, 0, 0, 0, 7, 5, 0, 0, 9,
         0, 0, 0, 6, 0, 1, 0, 7, 8,
         0, 0, 7, 0, 4, 0, 2, 6, 0,
         0, 0, 1, 0, 5, 0, 9, 3, 0,
         9, 0, 4, 0, 6, 0, 0, 0, 5,
         0, 7, 0, 3, 0, 0, 0, 1, 2,
         1, 2, 0, 0, 0, 7, 4, 0, 0,
         0, 4, 9, 2, 0, 6, 0, 0, 7]).reshape([9, 9])

    solutions_list = list()
    solver(s, solutions_list)
    for solution in solutions_list:
        print(solution)