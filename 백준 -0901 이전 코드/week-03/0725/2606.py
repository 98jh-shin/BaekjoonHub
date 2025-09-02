import sys

sys.stdin = open('../../../input.txt', 'r')

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

con = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    con[i].append(j)
    con[j].append(i)

visited = [False] * (n + 1)

count = 0
def dfs(x):
    visited[x] = True
    global count
    count += 1
    for com in con[x]:
        if not visited[com]:
            dfs(com)


dfs(1)
print(count - 1)