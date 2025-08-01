import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

smaller_list = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    smaller_list[a].append(b)
    in_degree[b] += 1

q = deque()

for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)

result = []
while q:
    cur = q.popleft()
    result.append(cur)
    for nxt in smaller_list[cur]:
        in_degree[nxt] -= 1
        if in_degree[nxt] == 0:
            q.append(nxt)

print(*result)


