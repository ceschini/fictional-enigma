#!/bin/python3

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    # Write your code here
    a = list(range(1, len(q)+1))
    bribes = 0
    single_bribe = 0
    
    for i in range(len(a)):
        if a[i] == q[i]:
            continue
        else:
            while a[i] != q[i]:
                single_bribe += 1
                if single_bribe > 2:
                    print('Too chaotic')
                    return -1
                idx = a.index(q[i])
                a[idx], a[idx-1] = a[idx-1], a[idx]
                bribes += 1
            single_bribe = 0
    print(bribes)


if __name__ == '__main__':
    q = [1, 2, 5, 3, 7, 8, 6, 4]
    minimumBribes(q)
