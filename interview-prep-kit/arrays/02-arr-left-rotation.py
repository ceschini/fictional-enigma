#!/bin/python3

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#


def rotLeft(a, d):
    # Write your code here
    for _ in range(d):
        a.append(a.pop(0))
    return a


if __name__ == '__main__':

    d = 10

    a = [41, 73, 89, 7, 10, 1, 59, 58, 84, 77,
         77, 97, 58, 1, 86, 58, 26, 10, 86, 51]

    result = rotLeft(a, d)
    print(' '.join(map(str, result)))
