import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()


def LCS(a, b):
    len_a = len(a)
    len_b = len(b)

    dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]

    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[i][j]


print(LCS(a, b))