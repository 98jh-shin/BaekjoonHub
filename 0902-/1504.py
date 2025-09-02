import sys
import heapq

INF = int(1e9)

N, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# 반드시 거쳐야 하는 서로 다른 정점 2개
v1, v2 = map(int, sys.stdin.readline().split())




