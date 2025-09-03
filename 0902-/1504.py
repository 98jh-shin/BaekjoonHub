import sys
import heapq

INF = float('inf')

N, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# 반드시 거쳐야 하는 서로 다른 정점 2개
v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(start):
    dist = [INF] * (N + 1)
    hq = []


    dist[start] = 0
    heapq.heappush(hq, (0, start)) # (비용, 정점)
    # 정점의 개수 -1 만큼 반복 = 모든 간선 확인

    while hq:
        cost, current = heapq.heappop(hq)

        if dist[current] < cost:
            continue

        for nxt, weight in graph[current]:
            next_cost = cost + weight

            if dist[nxt] > next_cost:
                dist[nxt] = next_cost
                heapq.heappush(hq, (next_cost, nxt))

    return dist

dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

result = min(path1, path2)
if result >= INF:
    print(-1)
else:
    print(result)