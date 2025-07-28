import sys
sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline().rstrip())

inout = list(map(int, sys.stdin.readline().rstrip()))
graph = [[] for _ in range(n + 1)]
res = 0
for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if inout[a - 1] == 1 and inout[b - 1] == 1:
        res += 2
    else:
        graph[a].append(b)
        graph[b].append(a)

def dfs(cur, visited):
    visited[cur] = True
    count = 0
    for nxt in graph[cur]:
        if not visited[nxt]:
            if inout[nxt - 1] == 1: # 실내라면
                count += 1
            else: # 실외라면
                count = count + dfs(nxt, visited)
    return count

visited = [False] * (n + 1)

for i in range(1, n + 1):
    if inout[i - 1] == 0 and not visited[i]:
        count = dfs(i, visited)
        res += count * (count - 1)

print(res)