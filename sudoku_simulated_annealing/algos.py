import random
import numpy as np


def fill3x3(row, column, array):
    """Checks which numbers are missing in a 3x3 block"""
    checklist = [False] * 9
    for i in range(row, row + 3):
        for j in range(column, column + 3):
            if array[i][j] != 0:
                checklist[array[i][j] - 1] = True

    """Adds them to a list"""
    addlist = []
    for i in range(len(checklist)):
        if not checklist[i]:
            addlist.append(i + 1)

    """Fill the 3x3 box without repeating any numbers"""
    for i in range(len(addlist)):
        breakcheck = False
        index = random.randint(0, len(addlist) - 1)
        for j in range(row, row + 3):
            for k in range(column, column + 3):
                if array[j][k] == 0:
                    number = addlist[index]
                    array[j][k] = number
                    addlist.remove(number)
                    breakcheck = True
                    break

            if breakcheck:
                break


def correctness(array):
    score = score1d(array) + score1d(array.transpose())

    return score


def score1d(array):
    score = 0
    for i in range(9):
        checklist = [False] * 9
        for j in range(9):
            if not checklist[array[i][j] - 1]:
                checklist[array[i][j] - 1] = True
            else:
                score += 1
    return score


def randomswap(empty_array, array):
    x, y = random.randint(0, 2), random.randint(0, 2)


    zero_counter = 0

    for i in range(3 * x, 3 * x + 3):
        for j in range(3 * y, 3 * y + 3):
            if empty_array[i][j] == 0:
                zero_counter += 1


    if zero_counter > 1:

        sample1, sample2 = random.sample(range(1, zero_counter + 1), k=2)

        i1, i2, j1, j2 = 0, 0, 0, 0

        for i in range(3 * x, 3 * x + 3):
            for j in range(3 * y, 3 * y + 3):
                if empty_array[i][j] == 0:
                    sample1 -= 1
                    sample2 -= 1
                if sample1 == 0:
                    i1, j1 = i, j
                    sample1 -= 1
                if sample2 == 0:
                    i2, j2 = i, j
                    sample2 -= 1

        array[i1][j1], array[i2][j2] = array[i2][j2], array[i1][j1]



