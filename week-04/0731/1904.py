n = int(input())

if n < 3:
    print(n)
    exit()

length = (n // 2) + 1 # 11
dp = [0] * (length + 2)

dp[0] = 1
dp[1] = 1

for i in range(2, length + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

# 6 4 5 3
result = (dp[length] * dp[(n - length)]) + (dp[length - 1] * dp[(n - length - 1)])

print(result % 15746)