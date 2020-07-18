# Uses python3
import sys


def binary_search(a, x):
    left, right = 0, len(a) - 1

    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
    # write your code here


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    data = list(map(int, input().strip().split(' ')))
    n = data[0]
    a = data[1:]
    query = list(map(int, input().strip().split(' ')))
    for x in query[1:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end=' ')
