#!/bin/python3

# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    # Write your code here
    alt = 0
    valleys = 0
    for step in path:
        if step == 'U':
            alt += 1
        elif step == 'D':
            if alt == 0:
                valleys += 1
                alt -= 1
            else:
                alt -= 1
    return valleys


if __name__ == '__main__':

    path = ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U']
    steps = len(path)
    result = countingValleys(steps, path)
    print(result)
