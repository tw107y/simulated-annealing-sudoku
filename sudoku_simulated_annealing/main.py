"""
Parts of this code is from @kushagra77 and @rohitash-chandra on github
"""


import numpy as np
import algos
import simulated_annealing as sa


def main():

    # Reading in the file to store the initial puzzle
    with open("puzzle.txt") as puzzle:
        linelist = puzzle.readlines()

    sudoku = np.zeros((9, 9), dtype=int)
    for i in range(9):
        for j in range(9):
            sudoku[i][j] = linelist[i][j]

    empty_sudoku = sudoku.copy()

    for i in range(0, 9)[::3]:
        for j in range(0, 9)[::3]:
            algos.fill3x3(i, j, sudoku)

    sudoku = sa.solve(empty_sudoku, sudoku)

    print(sudoku)


if __name__ == '__main__':
    main()


