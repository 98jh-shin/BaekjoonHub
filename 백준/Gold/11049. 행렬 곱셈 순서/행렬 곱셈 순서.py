import sys

n = int(sys.stdin.readline()) # 행렬의 개수

arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for length in range(2, n + 1): # 구하려는 행렬들의 길이
    for i in range(1, (n - length) + 2): # 1, 행렬의 숫자 - 구하려는 행렬들의 길이 + 1 (1부터 시작해서) + 1 (0 base index)
        j = i + length - 1 # 시작위치 + 길이를 통해 이번 행렬들의 길이의 마지막 위치값
        dp[i][j] = sys.maxsize
        for k in range(i, j): # 마지막 위치값 - 1 까지 ABCD의 경우 ABC까지 곱한 후 D를 곱한 경우와 같기 때문에
            cost = dp[i][k] + dp[k + 1][j] + arr[i - 1][0] * arr[k - 1][1] * arr[j - 1][1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[1][n])