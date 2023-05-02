#!/bin/python3

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    # Write your code here
    filter = [
        [1, 1, 1],
        [0, 1, 0],
        [1, 1, 1]
    ]
    hglasses = list()

    print('--- step 1 ----')
    print(arr[0][0:3])
    print(arr[1][0:3])
    print(arr[2][0:3])
    print('--- step 2 ---')
    print(arr[0][1:4])
    print(arr[1][1:4])
    print(arr[2][1:4])


if __name__ == '__main__':

    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]

    result = hourglassSum(arr)
