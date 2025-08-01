import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, k = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

s, x, y = map(int, sys.stdin.readline().split())

v_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            v_list.append((graph[i][j], i, j)) #

v_list.sort()
dq = deque(v_list)

while dq:
    v, cur_x, cur_y, sec = dq.popleft()

    if sec == s:
        break

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = v
                dq.append((v, nx, ny, sec + 1))

print(graph[x - 1][y - 1])