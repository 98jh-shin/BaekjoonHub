import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

n = int(input())

tiles = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


max_height = 0
for i in range(n):
    for j in range(n):
        if max_height < tiles[i][j]:
            max_height = tiles[i][j]
result = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x,y, h, visited):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
             if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
                if not visited[x + dx[i]][y + dy[i]] and tiles[x + dx[i]][y + dy[i]] > h:
                    visited[x+ dx[i]][y + dy[i]] = True
                    queue.append((x+ dx[i], y + dy[i]))

for h in range(0, max_height + 1):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if tiles[i][j] > h and not visited[i][j]:
                bfs(i, j, h, visited)
                count += 1

    if result < count:
        result = count

print(result)

