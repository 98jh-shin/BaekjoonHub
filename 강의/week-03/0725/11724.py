import sys

sys.stdin = open('../../../input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

con = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    con[i].append(j)
    con[j].append(i)

visited = [False] * (n + 1)
def dfs(x):
    visited[x] = True
    for com in con[x]:
        if not visited[com]:
            dfs(com)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)