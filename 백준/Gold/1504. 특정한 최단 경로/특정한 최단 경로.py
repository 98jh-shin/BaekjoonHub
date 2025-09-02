import sys
import heapq

input = sys.stdin.readline
INF = float('inf')


def dijkstra(start):
    dist = [INF] * (N + 1)
    pq = []

    dist[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        cost, here = heapq.heappop(pq)

        if dist[here] < cost:
            continue

        for there, weight in graph[here]:
            next_cost = cost + weight
            if dist[there] > next_cost:
                dist[there] = next_cost
                heapq.heappush(pq, (next_cost, there))

    return dist


N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

v1, v2 = map(int, input().split())

dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]

path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

answer = min(path1, path2)

if answer >= INF:
    print(-1)
else:
    print(answer)
