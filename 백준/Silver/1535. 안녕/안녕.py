import sys

n = int(sys.stdin.readline())

damage = list(map(int, sys.stdin.readline().split()))
happy = list(map(int, sys.stdin.readline().split()))


dp = [0] * 101

for i in range(n):
    for j in range(100, damage[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - damage[i]] + happy[i])

print(dp[99])