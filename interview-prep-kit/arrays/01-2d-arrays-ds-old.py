#!/bin/python3

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    # Write your code here
    index_map = list()
    for i, line in enumerate(arr):
        hcount = 0
        for j, el in enumerate(line):
            if el != 0:
                if (i, j) not in index_map:
                    index_map.append((i, j))
                hcount += 1
            if hcount == 3:
                hcount = 0
                mid_i, mid_j = index_map[1]
                if mid_i + 1 >= len(arr[0]):
                    continue
                elif arr[mid_i + 1][mid_j] != 0:
                    if (mid_i + 1, mid_j) not in index_map:
                        index_map.append((mid_i + 1, mid_j))
                    for k in range(3):
                        i, j = index_map[k]
                        i += 2
                        if arr[i][j] != 0:
                            if (i, j) not in index_map:
                                index_map.append((i, j))
                        else:
                            continue
                else:
                    continue
    print(index_map)


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
