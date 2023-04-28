#!/bin/python3

# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#


def jumpingOnClouds(c):
    # Write your code here
    jumps = 0
    i = 0
    while i < len(c):
        if i+2 < len(c):
            if c[i+2] == 0:
                i = i + 2
                jumps += 1
                continue
        elif i+1 == len(c):
            break
        i = i + 1
        jumps += 1
    return jumps


if __name__ == '__main__':

    c_ok = [0, 0, 0, 1, 0, 0]
    c_bug = [0, 0, 1, 0, 0, 1, 0]

    result = jumpingOnClouds(c_bug)
    print(result)
