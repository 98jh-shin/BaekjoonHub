n = int(input())

if n < 3:
    print(n)
    exit()

length = (n // 2) + 1
dp = [0] * (length + 2)

dp[0] = 1
dp[1] = 1

for i in range(2, length + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

result = (dp[length] * dp[(n - 1) - (length - 1)]) + (dp[length - 1] * dp[(n - 1) - length])

print(result % 15746)