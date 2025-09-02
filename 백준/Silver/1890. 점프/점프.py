from collections import deque
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

q = deque()

for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            continue
        if i == n - 1 and j == n - 1:
            continue

        jump = graph[i][j]

        if j + jump < n:
            dp[i][j + jump] += dp[i][j]

        if i + jump < n:
            dp[i + jump][j] += dp[i][j]

# while q:
#     x, y = q.popleft()
#     start = graph[x][y]
#     if start == 0:
#         continue
#     for i in range(2):
#         nx = x + (dx[i] * graph[x][y])
#         ny = y + (dy[i] * graph[x][y])
#         if 0 <= nx < n and 0 <= ny < n:
#             dp[nx][ny] += 1
#             q.append((nx, ny))

print(dp[n - 1][n - 1])