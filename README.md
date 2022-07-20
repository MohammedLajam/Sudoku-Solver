# Sudoku-Solver
The code in this repository implemented the conditions of a Sudoku game and how to solve it.
The first python file consists of the code to solve a SUdoku game (6x6 grid)
The second Python file consists of the code to solve a SUdoku game (9x9 grid)

## Introduction:
it is a logic-based combinatorial number-placement puzzle. In classic Sudoku, the objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contain all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution.

## Roles of Sudoku Game:
The Target is to fill the empty cells with number between 1 to 9 and keeping the roles of Sudoku into consideration:
  1. Each row consists of 9 cells, where all of them has a uniqie number between 1 to 9
  2. Each column consists of 9 cells, where all of them has a uniqie number between 1 to 9
  3. Each subgrid consists 9 cells, where all of them has a uniqie number between 1 to 9

## Implementation of Python code:
Libraries: NumPy
Sudoku example:
![alt text](https://static.techspot.com/images2/downloads/topdownload/2019/09/2019-09-19-ts3_thumbs-15a.png)

1. We first go for each 0 (empty cell), and check the rows, cloumns and a square (3*3).
2. If the number fulfills the conditions of Sudoku, then we replace 0 with the number. if not, then we go for the next number.
3. If there is no possible number at any cell in the Sudoku, then we use the Back Tracking by going back to the previous cell and check different number.
4. It go until all empty cells are filled in a way it applies all the condition of the Sudoku and this means the end of the game.
5. The code will display all the possible solutions, if there are more than one solution in the provided sudoku game.

## Note:
In the python file, there is already an example of unsolved Sudoku game. it is also possible to find yourself another example to test the code.
There are many example on the internet and it is not recommended to invent your own grid because it has to be lead to an prospect solution.
