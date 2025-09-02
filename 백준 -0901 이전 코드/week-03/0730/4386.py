import sys
import heapq

n = int(sys.stdin.readline())

stars = []
visited = [False] * n
dist = [10 ** 7] * n

for i in range(n):
    x, y = map(float, sys.stdin.readline().split())
    stars.append((x, y))

total = 0.0
dist[0] = 0
hq = [(0.0, 0)]

while hq:
    cost, cur = heapq.heappop(hq)
    if visited[cur]:
        continue
    visited[cur] = True
    total += cost

    cur_x, cur_y = stars[cur]
    for i in range(n):
        if visited[i]:
            continue
        nx, ny = stars[i]
        dx = nx - cur_x
        dy = ny - cur_y
        new_cost = (dx ** 2 + dy ** 2) ** 0.5
        heapq.heappush(hq, (new_cost, i))

print(f"{total:.2f}")






