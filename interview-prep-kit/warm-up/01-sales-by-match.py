#!/bin/python3

# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    # Write your code here
    pairs = 0
    paired_idx = list()
    for i in range(n):
        sock = ar[i]
        for j in range(n):
            pair = ar[j]
            if j == i:
                continue
            elif sock == pair:
                if i not in paired_idx:
                    if j not in paired_idx:
                        pairs += 1
                        paired_idx.append(i)
                        paired_idx.append(j)
    return pairs


if __name__ == '__main__':

    ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
    n = len(ar)
    result = sockMerchant(n, ar)
    print(result)
