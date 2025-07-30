import sys

n = int(sys.stdin.readline())

graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().strip()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False] * n for _ in range(n)]


def dfs(x, y, cnt):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                cnt = dfs(nx, ny, cnt + 1)
    return cnt


res = []
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if graph[i][j] == 1:
                visited[i][j] = True
                res.append(dfs(i, j, 1))

res.sort()
print(len(res))
for i in res:
    print(i)
