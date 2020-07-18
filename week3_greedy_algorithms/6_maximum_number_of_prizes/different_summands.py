# Uses python3
import sys


def optimal_summands(n):
    summands = []
    sumn = 0
    curr = 1
    while sumn + curr <= n:
        summands.append(curr)
        sumn += curr
        curr += 1
    if sumn < n:
        summands[-1] += (n - sumn)
    # write your code here
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
