# Uses python3
import sys


def get_change(m):
    # write your code here
    coins = [1, 3, 4]
    dp = [10000007 for i in range(m+1)]
    dp[0] = 0
    for i in range(1, m+1):
        for coin in coins:
            if i - coin >= 0:
                if dp[i] > dp[i-coin] + 1:
                    dp[i] = dp[i-coin] + 1
    return dp[m]


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
