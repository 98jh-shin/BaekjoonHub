import sys
import heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
out_degree = [0] * (n + 1)
res = [0] * (n + 1)

for i in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    graph[x].append((y, k))
    out_degree[y] += 1

q = []
for i in range(1, n + 1):
    if out_degree[i] == 0:
        heapq.heappush(q, (-i, 1))

while q:
    v, cnt = heapq.heappop(q)
    v = -1 * v
    for (y, k) in graph[v]:
        out_degree[y] -= 1
        if out_degree[y] == 0:
            if graph[y]:
                heapq.heappush(q, (-y, k * cnt + res[y]))
                res[y] = 0
            else:
                res[y] += cnt * k
        else:
            res[y] += cnt * k

for i in range(1, n + 1):
    if res[i] > 0:
        print(i, res[i])



