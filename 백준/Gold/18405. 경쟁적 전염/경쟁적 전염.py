import sys
from collections import deque
import heapq
n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
hq = []

s, x, y = map(int, sys.stdin.readline().split())

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            heapq.heappush(hq, (graph[i][j], i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
tmp = []
sec = 0

while hq:
    if sec == s: ## 목표 시간이 되면
        print(graph[x - 1][y - 1])
        break

    v, cur_x, cur_y = heapq.heappop(hq)

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = v
                heapq.heappush(tmp, (v, nx, ny))

    if not hq and tmp: # 정렬이 풀리고 있어서 틀림
        while tmp:
            heapq.heappush(hq, heapq.heappop(tmp))
        sec += 1
else:
    print(graph[x - 1][y - 1])