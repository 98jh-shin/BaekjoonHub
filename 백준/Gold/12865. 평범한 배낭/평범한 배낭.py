import sys

n, k = map(int, sys.stdin.readline().split())

dp = [0] * (k + 1)
objs = []

for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    objs.append((w, v))

for w, v in objs:
    for i in range(k, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)
        
print(dp[k])

