# Uses python3
import sys


def optimal_sequence(n):
    sequence = []
    sequence.append(n)
    dp = [1000000007 for i in range(n + 1)]
    dp[1] = 0

    for i in range(2, n + 1):
        if i // 2 >= 1 and i % 2 == 0 and dp[i // 2] < dp[i]:
            dp[i] = dp[i // 2] + 1
        if i // 3 >= 1 and i % 3 == 0 and dp[i // 3] < dp[i]:
            dp[i] = dp[i // 3] + 1
        if i - 1 >= 1 and dp[i - 1] < dp[i]:
            dp[i] = dp[i - 1] + 1

    while n > 1:
        x = 1000000007
        newn = n
        if n % 2 == 0 and n // 2 >= 1 and dp[n // 2] < x:
            x = dp[n // 2]
            newn = n // 2
        if n % 3 == 0 and n // 3 >= 1 and dp[n // 3] < x:
            x = dp[n // 3]
            newn = n // 3
        if n - 1 >= 1 and dp[n - 1] < x:
            x = dp[n - 1]
            newn = n - 1
        n = newn
        sequence.append(newn)
    # sequence.append(1)
    return list(reversed(sequence))

n = int(input())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
