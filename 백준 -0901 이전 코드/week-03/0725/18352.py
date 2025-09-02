import sys
from collections import deque
sys.stdin = open('../../../input.txt', 'r')

n, m, k, x = map(int, sys.stdin.readline().split())


citys = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    citys[i].append(j)

visited = [False] * (n + 1)
res_city = []
dist = [-1] * (n + 1)

def bfs(x):
    visited[x] = True
    dist[x] = 0
    q = deque()
    q.append(x)
    while q:
        i = q.popleft()
        for city in citys[i]:
            if not visited[city]:
                visited[city] = True
                dist[city] = dist[i] + 1
                if dist[city] == k:
                    res_city.append(city)
                q.append(city)

bfs(x)

if res_city:
    for city in sorted(res_city):
        print(city)
else:
    print(-1)