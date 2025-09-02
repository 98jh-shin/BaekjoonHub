import sys
from collections import deque
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
out_degree = [0] * (n + 1)
res = [0] * (n + 1)

for i in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    graph[x].append((y, k))
    out_degree[y] += 1

q = deque([n])

res[n] = 1
while q:
    v= q.popleft()
    v = 1 * v
    for (y, k) in graph[v]:
        res[y] += res[v] * k
        out_degree[y] -= 1
        if out_degree[y] == 0:
            q.append(y)

for i in range(1, n + 1):
    if not graph[i]:
        print(i, res[i])



