import sys

input = sys.stdin.readline

N, M = map(int, input().split())
max_jump = int((2 * N) ** 0.5) + 2
INF = 10 ** 9
small = set(int(input()) for _ in range(M))
dp = [[INF] * max_jump for _ in range(N + 1)] # 돌 번호, 직전 점프 크키

dp[1][0] = 0
dx = [-1, 0, 1]
for i in range(1, N):
    if i in small:
        continue

    for j in range(max_jump):
        if dp[i][j] == INF:
            continue

        for k in range(3):
            nxt_jump = j + dx[k]
            if nxt_jump > 0:
                nxt_stone = i + nxt_jump

                if nxt_stone <= N and nxt_stone not in small and nxt_jump < (N * 2):
                    if dp[nxt_stone][nxt_jump] > dp[i][j] + 1:
                        dp[nxt_stone][nxt_jump] = dp[i][j] + 1

res = min(dp[N])
if res == INF:
    print(-1)
else:
    print(res)


