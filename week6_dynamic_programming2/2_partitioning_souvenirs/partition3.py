# Uses python3
import sys
import itertools


def partition3(A):
    sumn = sum(A)
    if sumn % 3 != 0:
        return 0

    n = len(A)
    dp = [[False for i in range(sumn)] for i in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(n + 1):
        for j in range(sumn):
            if j - A[i - 1] >= 0:
                dp[i][j] = dp[i - 1][j - A[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][sumn // 3] and dp[n][sumn * 2 // 3]


if __name__ == '__main__':
    n = input()
    A = list(map(int, input().strip().split(' ')))
    if partition3(A):
        print(1)
    else:
        print(0)
