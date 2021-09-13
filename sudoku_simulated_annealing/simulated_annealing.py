from algos import randomswap, correctness, score1d
from numpy import exp
from numpy.random import rand


n_iterations = 100000
temp = 100

def solve(empty_array, array):

    best = correctness(array)
    curr = best
    counter = 0

    for i in range(n_iterations):
        if best == 0:
            break
        if counter > 1000:
            break
        temp_array = array.copy()
        randomswap(empty_array, temp_array)
        candidate = correctness(temp_array)

        if candidate < best:
            array = temp_array
            print('correctness has increased from {} to {}'.format(best, candidate))

            best = candidate
            counter += 1

        diff = candidate - curr

        t = temp/float(i + 1)

        metropolis = exp(-diff/t)

        if diff < 0 or rand() < metropolis:
            curr = candidate

    return array
