# Uses python3
import sys
import random


def partition3(a, l, r):
    # write your code here
    x = a[l]
    smaller, equal = l, l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            smaller += 1
            equal += 1
            a[i], a[equal] = a[equal], a[i]
            a[equal], a[smaller] = a[smaller], a[equal]
        elif a[i] == x:
            equal += 1
            a[i], a[equal] = a[equal], a[i]
    a[l], a[smaller] = a[smaller], a[l]
    return smaller, equal


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    # m = partition2(a, l, r)
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split(' ')))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
