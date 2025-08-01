import sys
import heapq

n = int(sys.stdin.readline())

graph = [[] for _ in range(n)]
for i in range(n):
    input_row = sys.stdin.readline().strip()
    for room in input_row:
        graph[i].append(0 if room == "1" else 1)


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dijkstra(x, y):
    dist = [[2500] * n for _ in range(n)]
    dist[x][y] = 0
    q = []
    heapq.heappush(q, (0, x, y))
    while q:
        cost, cur_x, cur_y = heapq.heappop(q)

        if cost > dist[cur_x][cur_y]:
            continue

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if not 0 <= nx < n or not 0 <= ny < n: # 리스트 범위 넘는거 방지
                continue
            new_cost = cost + graph[nx][ny]

            if dist[nx][ny] > new_cost:
                dist[nx][ny] = new_cost
                heapq.heappush(q, (new_cost, nx, ny))

    return dist[n - 1][n - 1]

print(dijkstra(0, 0))



