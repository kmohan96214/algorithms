# Uses python3
import sys


def merge(a, b, left, right):
    i = left
    ave = (left + right) // 2
    j = ave
    curr = left
    number_of_inversions = 0
    while i < ave and j < right:
        if a[i] <= a[j]:
            b[curr] = a[i]
            i += 1
        else:
            number_of_inversions += (ave - i)
            b[curr] = a[j]
            j += 1
        curr += 1
    while i < ave:
        b[curr] = a[i]
        i, curr = i + 1, curr + 1
    while j < right:
        b[curr] = a[j]
        j, curr = j + 1, curr + 1

    for i in range(left, right):
        a[i] = b[i]
    return number_of_inversions


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions

    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    # write your code here
    number_of_inversions += merge(a, b, left, right)
    return number_of_inversions


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split(' ')))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
