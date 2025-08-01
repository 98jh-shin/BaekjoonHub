import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    coins = list(map(int, sys.stdin.readline().split()))
    total = int(sys.stdin.readline())

    dp = [0] * (total + 1)

    for coin in coins:
        dp[0] = 1
        for x in range(coin, total + 1):
            dp[x] += dp[x - coin]

    print(dp[total])