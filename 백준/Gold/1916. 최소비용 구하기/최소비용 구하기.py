import sys
import heapq

n = int(sys.stdin.readline().rstrip()) # 도시의 개수
m = int(sys.stdin.readline().rstrip()) # 버스의 개수

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, cost))

start, end = map(int, sys.stdin.readline().rstrip().split())

def dijkstra(start):
    dist = [10 ** 9] * (n + 1)
    hq = [(0, start)]
    while hq:
        cost, cur = heapq.heappop(hq)
        if cost > dist[cur]:
            continue
        for nxt, nxt_cost in graph[cur]:
                if cost + nxt_cost < dist[nxt]:
                    dist[nxt] = cost + nxt_cost
                    heapq.heappush(hq, (dist[nxt], nxt))
    return dist[end]

print(dijkstra(start))

