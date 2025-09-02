import sys

def matrix_mul():
    n = int(sys.stdin.readline())  # 행렬의 개수

    r = [0] * n
    c = [0] * n
    for i in range(n):
        r[i], c[i] = map(int, sys.stdin.readline().split())

    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):  # 구하려는 행렬들의 길이
        for i in range((n - length) + 1):  # 1, 행렬의 숫자 - 구하려는 행렬들의 길이 + 1 (1부터 시작해서) + 1 (0 base index)
            j = i + length - 1  # 시작위치 + 길이를 통해 이번 행렬들의 길이의 마지막 위치값
            best = sys.maxsize
            for k in range(i, j):  # 마지막 위치값 - 1 까지 ABCD의 경우 ABC까지 곱한 후 D를 곱한 경우와 같기 때문에
                cost = dp[i][k] + dp[k + 1][j] + r[i] * c[k] * c[j]
                if best > cost:
                    best = cost
            dp[i][j] = best

    return dp[0][n - 1]


res = matrix_mul()
print(res)