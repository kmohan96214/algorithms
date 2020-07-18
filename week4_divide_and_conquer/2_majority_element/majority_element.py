# Uses python3
import sys


def get_majority_element(a, left, right):
    votes = {}
    for i in a:
        if i in votes:
            votes[i] += 1
        else:
            votes[i] = 1
    for i in votes.values():
        if i > len(a) // 2:
            return 1
    return -1


if __name__ == '__main__':
    n = input()
    a = list(map(int, input().strip().split(' ')))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
