import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tiles = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

max_height = max(map(max, tiles))
min_height = min(map(min, tiles))

def bfs(sx, sy, h, visited):
    q = deque([(sx, sy)])
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()
        for nx, ny in zip((x+1, x-1, x, x), (y, y, y+1, y-1)):
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and tiles[nx][ny] > h:
                    visited[nx][ny] = True
                    q.append((nx, ny))

result = 0

for h in range(min_height-1, max_height+1):
    visited = [[False] * n for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(n):
            if tiles[i][j] > h and not visited[i][j]:
                bfs(i, j, h, visited)
                count += 1
    
    result = max(result, count)

print(result)
