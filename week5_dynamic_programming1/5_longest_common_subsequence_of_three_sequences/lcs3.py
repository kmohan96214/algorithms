# Uses python3

import sys


def lcs3(a, b, c):
    # write your code here
    dp = [[[0 for i in range(len(c) + 1)] for j in range(len(b) + 1)] for k in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            for k in range(1, len(c) + 1):
                if a[i - 1] == b[j - 1] and b[j - 1] == c[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1], dp[i - 1][j - 1][k],
                                      dp[i - 1][j][k - 1], dp[i][j - 1][k - 1])

    return dp[len(a)][len(b)][len(c)]


if __name__ == '__main__':
    n = input()
    a = list(map(int, input().strip().split(' ')))
    m = input()
    b = list(map(int, input().strip().split(' ')))
    l = input()
    c = list(map(int, input().strip().split(' ')))
    print(lcs3(a, b, c))
