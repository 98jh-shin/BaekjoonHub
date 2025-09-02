import sys
from collections import deque

sys.stdin = open('../../../input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))

bfs(0, 0)
print(graph[n - 1][m - 1])