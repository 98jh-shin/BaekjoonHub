import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

def dp(arr, n):
    dp = [1] * n
    dp[0] = 1
    max_len = 1
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                if dp[i] > max_len:
                    max_len = dp[i]
    return max_len


print(dp(arr, n))