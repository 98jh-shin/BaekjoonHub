import sys

n = int(sys.stdin.readline())

if n < 2:
    print(n)
    exit()

dp = [0] * (n + 1)

dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])