# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


int_max = 100000000000000007
int_min = -100000000000000007


def min_max(min_dp, max_dp, i, j, ops):
    mini, maxi = int_max, int_min
    for k in range(i, j):
        a = evalt(max_dp[i][k], max_dp[k + 1][j], ops[k])
        b = evalt(max_dp[i][k], min_dp[k + 1][j], ops[k])
        c = evalt(min_dp[i][k], min_dp[k + 1][j], ops[k])
        d = evalt(min_dp[i][k], max_dp[k + 1][j], ops[k])
        mini = min(mini, a, b, c, d)
        maxi = max(maxi, b, c, d)
    return mini, maxi


def get_maximum_value(dataset):
    ops = [dataset[i] for i in range(len(dataset)) if i % 2 == 1]
    ds = [dataset[i] for i in range(len(dataset)) if i % 2 == 0]

    n = len(ds)
    min_dp = [[int_max for i in range(len(ds))] for i in range(len(ds))]
    max_dp = [[int_min for i in range(len(ds))] for i in range(len(ds))]

    for i in range(n):
        min_dp[i][i] = int(ds[i])
        max_dp[i][i] = int(ds[i])

    for s in range(n - 1):
        for i in range(n - s - 1):
            j = i + s + 1
            min_dp[i][j], max_dp[i][j] = min_max(min_dp, max_dp, i, j, ops)

    return max_dp[0][n - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
