#!/bin/python3

# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeatedString(s, n):
    init_count = s.count('a')
    full_copy = n // len(s)
    mid_count = full_copy * init_count
    leftovers = ''
    for i in range(n % len(s)):
        leftovers += s[i]

    final_count = leftovers.count('a')+mid_count
    return final_count


if __name__ == '__main__':
    s = 'a'

    n = 10000000000000000000000000000000

    result = repeatedString(s, n)
    print(result)
