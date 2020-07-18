# Uses python3
def edit_distance(s, t):
    # write your code here
    dp = [[1000000007 for i in range(len(t) + 1)] for i in range(len(s) + 1)]
    for i in range(len(s)):
        dp[i][0] = i
    for i in range(len(t)):
        dp[0][i] = i

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i - 1][j - 1]
                continue
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[len(s)][len(t)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
