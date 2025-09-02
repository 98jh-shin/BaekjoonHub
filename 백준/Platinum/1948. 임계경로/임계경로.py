import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
rgraph = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)

for i in range(m):
    s, e, cost = map(int, sys.stdin.readline().split())
    graph[s].append((e, cost))
    rgraph[e].append((s, cost))
    in_degree[e] += 1

start, end = map(int, sys.stdin.readline().split())

q = deque([start])
dist = [0] * (n + 1)

while q:
    v = q.popleft()
    for (nxt, cost) in graph[v]:

        in_degree[nxt] -= 1
        if in_degree[nxt] == 0:
            q.append(nxt)

        now_cost = dist[v] + cost
        if dist[nxt] < now_cost:
            dist[nxt] = now_cost

max_dist = dist[end]
print(max_dist)

visited = [False] * (n + 1)
q = deque([end])

count = 0
while q:
    v = q.popleft()
    for nxt, cost in rgraph[v]:
        if dist[v] == dist[nxt] + cost:
            count += 1
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True

print(count)