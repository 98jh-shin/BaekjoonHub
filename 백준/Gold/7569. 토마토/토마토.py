import sys
from collections import deque

m, n, h= map(int, sys.stdin.readline().split())

graph = [[[] for _ in range(n)] for _ in range(h)]

for i in range(h):
    for j in range(n):
        graph[i][j] = list(map(int, sys.stdin.readline().split()))

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i, j, k))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
dz = [-1, 1]
def bfs(q):
    day = 0
    tmp = []

    while q:
        z, x, y = q.popleft()

        for j in range(2):
            nz = z + dz[j]
            if 0 <= nz < h:
                if graph[nz][x][y] == 0:
                    graph[nz][x][y] = 1
                    tmp.append((nz, x, y))

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[z][nx][ny] == 0:
                    graph[z][nx][ny] = 1
                    tmp.append((z, nx, ny))

        if not q and tmp:
            q.extend(tmp)
            tmp.clear()
            day += 1

    return day
max_day = bfs(q)
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit()

print(max_day)