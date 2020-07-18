# Uses python3
import sys


def optimal_weight(W, weights):
    # write your code here
    n = len(weights)
    dp = [[0 for i in range(n + 1)] for j in range(W + 1)]
    for i in range(1, W + 1):
        for j in range(1, n + 1):
            if i - weights[j - 1] >= 0:
                dp[i][j] = max(dp[i - weights[j - 1]][j - 1] + weights[j - 1], dp[i][j - 1])
            else:
                dp[i][j] = dp[i][j - 1]
    return dp[W][n]


if __name__ == '__main__':
    W, n = map(int, input().strip().split(' '))
    weights = list(map(int, input().strip().split(' ')))
    print(optimal_weight(W, weights))
