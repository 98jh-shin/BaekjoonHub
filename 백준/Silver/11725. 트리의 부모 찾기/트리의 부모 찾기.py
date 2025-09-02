import sys
sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline())

con = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
visited = [False] * (n + 1)
for _ in range(n - 1):
    i, j = map(int, sys.stdin.readline().split())
    con[i].append(j)
    con[j].append(i)

def dfs(x):
    visited[x] = True
    for t in con[x]:
        if not visited[t]:
            parent[t] = x
            dfs(t)


dfs(1)
for i in range(2, n + 1):
    print(parent[i])