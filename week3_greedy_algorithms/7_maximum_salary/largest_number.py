# Uses python3

from functools import cmp_to_key


def cmp(x, y):
    if int(x + y) > int(y + x):
        return -1
    if int(x + y) < int(y + x):
        return 1
    return 0


def largest_number(a):
    # write your code here
    a.sort(key=cmp_to_key(cmp))
    return ''.join(a)


if __name__ == '__main__':
    n = int(input())
    a = input().strip().split(' ')
    print(largest_number(a))
